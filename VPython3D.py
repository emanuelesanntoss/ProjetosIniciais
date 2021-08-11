                               
from vpython import *           
import numpy as np              
                                

def axisArrows():                                                                                   

    al = 10.0 #arrow length                                                                           
    Xarrow = arrow(pos=vector(0,0,0), shaftwidth=.2,length=al, axis=vector(1,0,0), color=color.red)  
    Yarrow = arrow(pos=vector(0,0,0), shaftwidth=.2,length=al, axis=vector(0,1,0), color=color.green) 
    Zarrow = arrow(pos=vector(0,0,0), shaftwidth=.2,length=al, axis=vector(0,0,1), color=color.blue)  
    sphere(radius=0.5)                                                                                
    return                                                                                           


# Scene
#canvas(title='Triangles', background=vector(.8,.9,.05), x=350, y=0, width=2000, height=1100)
rodando = 1

def Pausar(b):	    
    global rodando
    rodando = 0
  
def Continuar(b):	    
    global rodando
    rodando = 1
    
def Reiniciar (b):    
    global rodando
    rodando = 2   
    
button( text='Pausar' , pos= scene.title_anchor , bind=Pausar) 
button( text='Continuar' , pos= scene.title_anchor , bind=Continuar) 
button( text='Reiniciar' , pos= scene.title_anchor , bind=Reiniciar )
# AxisArrows
axisArrows()

# Triangle Coords
va=vector(-5,7,-5)
vb=vector(7,-3,2)
vc=vector(5,7,0)
vd=vector(5,7,0)

# Convert coords to numpty array

p1 = np.array([va.x,va.y,va.z])
p2 = np.array([vb.x,vb.y,vb.z])
p3 = np.array([vc.x,vc.y,vc.z])

# normal (a vector)
N  = np.cross(p2-p1, p3-p1)
print("p1= ", p1, "N = ", N)
N=N/50
vn = vector(N[0],N[1],N[2])  # vector for normal arrow
print("    vn= ", vn)

# average (a vector)
average = (va+vb+vc+vd)/4
print("   Average = ", average)

sphere(radius=.5,pos=average)     #                           
    # Display the norm arrow                                  
N_arrow = arrow(pos=vector(average), shaftwidth=.2, length=4, axis=vector(0,0,2), color=color.blue)  
                                                                                                             

#                                                            vector(0,0,2) shows, vector(0,2,2) doesn't
# Create a triangle (quad with two vertices the same)         most value don't work

a = vertex(pos=va,color=color.red)
b = vertex(pos=vb,color=color.green)
c = vertex(pos=vc,color=color.blue)
d = vertex(pos=vd,color=color.white)

tr1 = quad(v0=a,v1=b,v2=c,v3=d)


