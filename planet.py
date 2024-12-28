import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
lmx=1
fig,ax=plt.subplots(1,lmx)
if lmx==1:
    ax=np.array([ax])
for i in range(lmx):
    ax[i].set_xlim(-5e11,5e11)
    ax[i].set_ylim(-5e11,5e11)
    ax[i].set_aspect(1)
G=6.67430e-11
class planet:
    def __init__(self,name,mass,r,x,y,z,vx,vy,vz):
        self.name=name
        self.pos=np.array([float(x),float(y),float(z)])
        self.v=np.array([float(vx),float(vy),float(vz)])
        self.a=0
        self.f=0
        self.m=mass
        self.r=r
        self.t=[]

    def update_location(self,other):
        r_val=np.linalg.norm(np.array(self.pos-np.array(other.pos)))
        self.f=G*self.m*other.m/(r_val**2)
        self.a=self.f/self.m
        self.v[0]+=self.a/r_val*(other.pos[0]-self.pos[0])
        self.v[1]+=self.a/r_val*(other.pos[1]-self.pos[1])
        self.v[2]+=self.a/r_val*(other.pos[2]-self.pos[2])
        
    def update_loc(self,time):
        self.pos+=self.v*time
        self.t.append(self.pos.tolist())
        if len(self.t)>0.5e3:
            self.t.pop(0)
pl=[]
tr=[[],[],[]]
c=[[],[],[]]
g=[[0,1],[2,1],[0,2]]
col=["red","blue","green","black"]
pl.append(planet(name="p1",mass=1e30 ,r=1e10 ,x=1e11 ,y=-1e11 ,z=0    ,vx=0 ,vy=0 ,vz=0 ))
pl.append(planet(name="p2",mass=5e29 ,r=1e10 ,x=0    ,y=1e11  ,z=0    ,vx=-8,vy=8 ,vz=1 ))
pl.append(planet(name="p3",mass=1e10 ,r=1e10 ,x=1e11 ,y=0     ,z=1e11 ,vx=3 ,vy=6 ,vz=1 ))
#pl.append(planet(name="p4",mass=1e10 ,r=1e10 ,x=1e11 ,y=1e11 ,z=1e11 ,vx=-4,vy=3 ,vz=2 ))
for i in range(len(pl)):
    for j in range(lmx):
        tr[j].append(ax[j].plot([],[],color=col[i]))
        #c.append(plt.Circle(pl[i].pos,pl[i].r,color=col[i]))
        #ax.add_patch(c[i])
        c[j].append(ax[j].plot([pl[i].pos[0]],[pl[i].pos[1]],'o',color=col[i])[0])#
def update(f):
    for i in range(50):
        for x in pl:
            for y in pl:
                if x!=y:
                    x.update_location(y)
                    y.update_location(x)
        for x in pl:
            x.update_loc(1e6)
        for j in range(len(pl)):
            for k in range(lmx):
                tr[k][j][0].set_data([x[g[k][0]] for x in pl[j].t],[x[g[k][1]] for x in pl[j].t])
    #for j in pl:
        #print(j.name,j.pos)
    for j in range(len(pl)):
        for k in range(lmx):
            #c[j]=plt.Circle(pl[j].pos,pl[j].r,color=col[j])
            #ax.add_patch(c[j])
            c[k][j].set_data([pl[j].pos[g[k][0]]],[pl[j].pos[g[k][1]]])#
ani=FuncAnimation(fig,update,frames=np.arange(0,3600*24),interval=1)
plt.show()
#It is just for play.

    
   
    
    

