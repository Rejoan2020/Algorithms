def mpl(x1,y1,x2,y2):
    dy=y2-y1
    dx=x2-x1
    D=2*dy-dx
    NE=2*(dy-dx)
    E=2*dy
    x=x1
    y=y1
    t=[]
    while x<=x2:
        x+=1
        if D<0:
            y+=1
            D=D+NE
        else:
            D=D+E
    return t

def find_zone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        if dx>0 and dy>0 : zone=0
        elif dx<0 and dy>0 : zone=3
        elif dx<0 and dy<0 : zone=4
        elif dx>0 and dy<0 : zone=7
    else :
        if dx>0 and dy>0 : zone=1
        elif dx<0 and dy>0 : zone=2
        elif dx<0 and dy<0 : zone=5
        elif dx>0 and dy<0 : zone=6
    return zone

def convert_original_zone(a,b):
    x1=0
    y1=0
    if zone == 1:
        x1 = b
        y1 = a
    elif zone == 2:
        x1 = (-1*b)
        y1 = a
    elif zone == 3:
        x1 = -1*a
        y1 = b
    elif zone == 4:
        x1 = -a
        y1 = -b
    elif zone == 5:
        x1 = -b
        y1 = -a
    elif zone == 6:
        x1 = b
        y1 = -a
    elif zone == 7:
        x1 = a
        y1 = -b
    else:
        x1 = a
        y1 = b

    r=(x1,y1)
    return r

x1,y1=input("Enter the value of x1,y1 respectevely:").split(",")
x2,y2=input("Enter the value of x2,y2 respectevely:").split(",")
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)

zone = find_zone(x1,y1,x2,y2)
print("zone : ",zone)
converted_point=convert_original_zone(x1,y1)
x1=converted_point[0]
y1=converted_point[1]
print(x1,y1)
converted_point=convert_original_zone(x2,y2)
x2=converted_point[0]
y2=converted_point[1]
print(x2,y2)
tp=mpl(x1,y1,x2,y2)
print(tp)
