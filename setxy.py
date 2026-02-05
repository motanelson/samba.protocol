
import tkinter as tk
from PIL import Image, ImageTk
import random
STEP=50
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()
def loads(s):
    img = Image.open(s).convert("RGBA")
    data = img.getdata()
    new_data = []

    for pixel in data:
        # se for preto puro, fica transparente
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(pixel)

    img.putdata(new_data)

    return ImageTk.PhotoImage(img)
def setxy(xxxx,yyyy,arrays):
    
    xy=[]
    xxyy=[]
    xxx=0
    yyy=0
    counter=0
    for b in arrays:
        xxyy=[]
        for c in b:
            
            if xxxx==xxx and yyyy==yyy:
                xxyy=xxyy+[255]
            else:
                
                xxyy=xxyy+[c]
                counter=counter+1
            xxx=xxx+1
        xy=xy+[xxyy]
        yyy=yyy+1
        xxx=0         
                
    return xy

def getxy(s:str):
    h=[]
    xy=[]
    xxyy=[]
    xxx=0
    yyy=0
    counter=0
    f1=open(s,"r")
    ss=f1.read()
    f1.close()
    arr=ss.split("\n")
    for b in arr:
        xxyy=[]
        for c in b:
            d:int=ord(c)-65
            if d<0:
                u=0
            elif d==0:
                xxyy=xxyy+[255]
            else:
                h=h+[canvas.create_image(xxx*50, yyy*50, image=pic2)]
                xxyy=xxyy+[counter]
                counter=counter+1
            xxx=xxx+1
        xy=xy+[xxyy]
        yyy=yyy+1
        xxx=0         
                
    return xy,h
pic = loads("bit.png")
pic2 =loads("pin.png")
xy,h=getxy("level.txt")
xxx=100
yyy=100
xxxx=0
yyyy=0
score=0
lens=int(len(xy)//2)


rect = canvas.create_image(xxx, yyy, image=pic)
def move(event):
    global xxx,yyy,xxxx,yyyy,xy,lens,h,score
    if event.keysym == "Up":
        canvas.move(rect, 0, -STEP)
        yyy=yyy-STEP
    elif event.keysym == "Down":
        canvas.move(rect, 0, STEP)
        yyy=yyy+STEP
    elif event.keysym == "Left":
        canvas.move(rect, -STEP, 0)
        xxx=xxx-STEP
    elif event.keysym == "Right":
        canvas.move(rect, STEP, 0)
        xxx=xxx+STEP
    aaa=255
    if yyy//50>-1 and yyy//50<8 and xxx//50<12 and xxx>-1:
        aaa=xy[yyy//50][xxx//50]
    if aaa != 255:
            canvas.move(h[aaa], 0-xxx-300,0)
            xy=setxy(xxx//50,yyy//50,xy)
            score=score+10
            print("score : "+str(score))
# Capturar teclas
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()
