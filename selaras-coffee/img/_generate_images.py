from PIL import Image, ImageDraw, ImageFilter
import math, random
random.seed(7)
S=2  # supersample
def new(w,h,bg):
    return Image.new("RGB",(w*S,h*S),bg)
def fin(im,w,h,path):
    im.resize((w,h),Image.LANCZOS).save(path)
def circ(d,cx,cy,r,fill=None,outline=None,width=1):
    d.ellipse([ (cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S ],fill=fill,outline=outline,width=width*S)

SH=["#183830"]
ESP="#2B1D16"; PINE="#20443B"; AMB="#D68A1F"; PAPER="#FAF8F3"; SAGE="#B9C9B4"; MILK="#F1E6D2"; CREMA="#B7773A"

def rings(d,cx,cy,r0,n,step,col,w=2):
    for i in range(n):
        circ(d,cx,cy,r0+i*step,outline=col,width=w)

def cup_top(d,cx,cy,R,coffee,art=True):
    circ(d,cx+R*0.04,cy+R*0.07,R*1.02,fill=SH[0])
    circ(d,cx,cy,R,fill="#F6F3EC")
    circ(d,cx,cy,R*0.93,fill="#E6E0D3")
    circ(d,cx,cy,R*0.80,fill=coffee)
    circ(d,cx,cy,R*0.70,fill=CREMA)
    if art:
        # concentric "selaras" ripple latte art
        for i,(rr,c) in enumerate([(0.60,MILK),(0.46,CREMA),(0.34,MILK),(0.22,CREMA),(0.10,MILK)]):
            circ(d,cx,cy,R*rr,fill=c)
    # handle
    d.rounded_rectangle([(cx+R*0.95)*S,(cy-R*0.14)*S,(cx+R*1.35)*S,(cy+R*0.14)*S],radius=int(R*0.14*S),fill="#F6F3EC")
    d.rounded_rectangle([(cx+R*0.95)*S,(cy-R*0.06)*S,(cx+R*1.27)*S,(cy+R*0.06)*S],radius=int(R*0.06*S),fill="#E6E0D3")

# ---------- logo ----------
im=new(512,512,PAPER); d=ImageDraw.Draw(im)
circ(d,256,256,236,fill=PINE)
for i,r in enumerate([196,150,104,58]):
    circ(d,256,256,r,outline=AMB if i%2==0 else SAGE,width=10)
circ(d,256,256,26,fill=AMB)
fin(im,512,512,"img/logo.png")

# ---------- favicon ----------
im2=im.resize((64*S,64*S)); im2.resize((64,64),Image.LANCZOS).save("img/favicon.png")

# ---------- hero (4:5 portrait) ----------
W,H=900,1000
im=new(W,H,PINE); d=ImageDraw.Draw(im)
rings(d,450,470,120,9,62,"#2E5A4E",3)
rings(d,450,470,150,3,186,AMB,2)
cup_top(d,420,470,260,ESP)
# coffee beans scattered
def bean(cx,cy,a,sz=44,col="#3A261B"):
    b=Image.new("RGBA",(sz*2*S,sz*2*S),(0,0,0,0)); bd=ImageDraw.Draw(b)
    bd.ellipse([sz*0.35*S,sz*0.1*S,sz*1.65*S,sz*1.9*S],fill=col)
    bd.line([(sz*S,sz*0.15*S),(sz*0.85*S,sz*1.0*S),(sz*S,sz*1.85*S)],fill="#1C1009",width=int(5*S))
    b=b.rotate(a,resample=Image.BICUBIC)
    im.paste(b,(int((cx-sz)*S),int((cy-sz)*S)),b)
for (x,y,a) in [(120,160,30),(790,130,-40),(800,860,60),(110,850,-20),(700,980-60,15),(70,520,80),(840,520,-70)]:
    bean(x,y,a,48,"#3A261B" if random.random()>.4 else "#5A3A27")
fin(im,W,H,"img/hero.png")

SH[0]="#C3CFBE"
# ---------- products (800x600) ----------
def product(path,bg,draw_fn):
    im=new(800,600,bg); d=ImageDraw.Draw(im)
    draw_fn(im,d); fin(im,800,600,path)

def p1(im,d): # es kopi susu gula aren: glass side view
    rings(d,400,300,80,6,60,"#E3D7BE",2)
    # glass
    gx0,gx1,gt,gb=290,510,110,500
    d.polygon([(gx0*S,gt*S),(gx1*S,gt*S),((gx1-22)*S,gb*S),((gx0+22)*S,gb*S)],fill="#FFFFFF66",outline="#9AA89F",width=3*S)
    # layers
    def layer(y0,y1,col):
        t0=(y0-gt)/(gb-gt); t1=(y1-gt)/(gb-gt)
        xl0=gx0+22*t0+4; xr0=gx1-22*t0-4; xl1=gx0+22*t1+4; xr1=gx1-22*t1-4
        d.polygon([(xl0*S,y0*S),(xr0*S,y0*S),(xr1*S,y1*S),(xl1*S,y1*S)],fill=col)
    layer(150,230,"#EADFC9"); layer(230,330,"#C69865"); layer(330,495,"#5B3A22")
    # ice cubes
    for (x,y) in [(360,180),(430,200),(395,255),(340,300),(450,320)]:
        d.rounded_rectangle([x*S,y*S,(x+52)*S,(y+52)*S],radius=10*S,fill="#FFFFFF55",outline="#FFFFFFAA",width=2*S)
    # straw
    d.line([(455*S,40*S),(415*S,420*S)],fill=AMB,width=14*S)
    circ(d,400,520,0,fill=None)
product("img/produk-kopi-susu.png","#E8EFE4",p1)

def p2(im,d): # V60 pour-over top view cup
    rings(d,400,300,90,6,60,"#C9D6C3",2)
    cup_top(d,380,300,200,"#3B2517",art=False)
    # swirl pour
    for i,rr in enumerate([0.55,0.40,0.26,0.12]):
        circ(d,380,300,200*rr,outline="#8A5A33",width=4)
    # dripper cone
    d.polygon([(560*S,470*S),(740*S,470*S),(680*S,560*S),(620*S,560*S)],fill=AMB)
    d.rectangle([555*S,455*S,745*S,472*S],fill="#B06F10")
product("img/produk-v60.png","#DCE6D8",p2)

def p3(im,d): # beans bag
    rings(d,400,320,100,6,60,"#4A3228",2)
    # bag
    d.rounded_rectangle([270*S,90*S,530*S,520*S],radius=26*S,fill=PINE)
    d.rectangle([270*S,90*S,530*S,140*S],fill="#183830")
    for i in range(6): d.line([(280+i*42)*S,98*S,(280+i*42)*S,132*S],fill="#2E5A4E",width=3*S)
    circ(d,400,300,78,fill=PAPER)
    for i,r in enumerate([62,44,26]):
        circ(d,400,300,r,outline=AMB if i%2==0 else PINE,width=6)
    circ(d,400,300,10,fill=AMB)
    d.rounded_rectangle([320*S,410*S,480*S,424*S],radius=6*S,fill=SAGE)
    d.rounded_rectangle([340*S,440*S,460*S,452*S],radius=6*S,fill="#2E5A4E")
    # beans
    def bean(cx,cy,a):
        b=Image.new("RGBA",(120*S,120*S),(0,0,0,0)); bd=ImageDraw.Draw(b)
        bd.ellipse([22*S,6*S,98*S,114*S],fill="#6B4630")
        bd.line([(60*S,10*S),(52*S,60*S),(60*S,110*S)],fill="#2B1D16",width=5*S)
        b=b.rotate(a,resample=Image.BICUBIC); im.paste(b,(int((cx-60)*S),int((cy-60)*S)),b)
    for (x,y,a) in [(160,470,30),(230,540,-30),(640,500,50),(580,550,10),(660,130,-40),(130,150,70)]: bean(x,y,a)
product("img/produk-biji-kopi.png","#2B1D16",p3)

SH[0]="#98AC93"
# ---------- about / story (900x700) ----------
im=new(900,700,SAGE); d=ImageDraw.Draw(im)
rings(d,450,350,50,8,60,"#A3B89E",3)
# three cups in a row -> "selaras" = in harmony
for i,(cx,col) in enumerate([(230,"#3B2517"),(450,ESP),(670,"#5B3A22")]):
    cup_top(d,cx-30,350,100,col)
fin(im,900,700,"img/tentang.png")
print("ok")
