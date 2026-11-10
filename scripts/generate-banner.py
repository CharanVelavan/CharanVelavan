"""Rebuild the profile banner with Pillow (pip install Pillow)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
def font(size, bold=False):
    candidates = [FONT_DIR / ('Arial Bold.ttf' if bold else 'Arial.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
    return ImageFont.truetype(str(next(p for p in candidates if p.exists())), size)
W,H = 1280,440
base=Image.new('RGB',(W,H),'#11191c')
d=ImageDraw.Draw(base)
for x in range(784,1280,32): d.line((x,0,x,H),fill='#1c2b30')
for y in range(0,H,32): d.line((784,y,W,y),fill='#1c2b30')
d.line((56,58,106,58),fill='#74e0ca',width=4)
d.text((56,83),'BUILDER’S LAB',font=font(18),fill='#74e0ca')
d.text((52,141),'Charan Velavan',font=font(76,True),fill='#f2f0e7')
d.text((56,238),'Exploring ideas. Engineering systems.',font=font(24),fill='#b0c0c3')
d.text((56,359),'AI / SOFTWARE / SYSTEMS',font=font(16),fill='#9bb4b9')
cx,cy=1032,216
for r in [96,136]: d.ellipse((cx-r,cy-r,cx+r,cy+r),outline='#344d59',width=1)
def point(t,angle):
    x,y=163*math.cos(t),58*math.sin(t)
    return (cx+x*math.cos(angle)-y*math.sin(angle),cy+x*math.sin(angle)+y*math.cos(angle))
for angle,color in [(-.63,'#74e0ca'),(.63,'#7196a6')]:
    d.line([point(i*math.tau/180,angle) for i in range(181)],fill=color,width=2)
d.regular_polygon((cx,cy,46),6,rotation=30,fill='#1d3c43',outline='#74e0ca',width=2)
d.text((cx,cy-2),'</>',font=font(25),fill='#d6f7ef',anchor='mm')
frames=[]
for i in range(72):
    im=base.copy(); pen=ImageDraw.Draw(im)
    for phase,angle,color in [(i/72*math.tau,-.63,'#74e0ca'),(-i/72*math.tau+2,.63,'#b2cbd6')]:
        x,y=point(phase,angle)
        pen.ellipse((x-6,y-6,x+6,y+6),fill=color)
    frames.append(im.quantize(colors=64))
frames[0].save(ROOT/'assets/builders-lab.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=2)
frames[0].convert('RGB').save(ROOT/'assets/builders-lab-preview.png')
print('Generated 72-frame banner:',(ROOT/'assets/builders-lab.gif').stat().st_size,'bytes')
