import random
import matplotlib.pyplot as plt
"""
def show():
    for i in range(20):
        for j in range(20):
            if a[i][j]==1:
                print("■",end="")
            else:
                print(" ",end="")
        print()
"""
a=[]
tmp=[]
n=150
d=2
ch=0
fig=plt.figure()
if ch:
    for i in range(n):
        a.append([])
        tmp.append([])
        for j in range(n):
            a[i].append(0)
            tmp[i].append(0)
    a[0][0]=1
    a[0][1]=1
    a[1][1]=1
    a[1][2]=1
    a[2][0]=1
else:
    for i in range(n):
        a.append([])
        tmp.append([])
        for j in range(n):
            a[i].append((random.randint(1,d)==1))
            tmp[i].append(0)

plt.imshow(a)
plt.draw()
st=-1
while st!=0:
    for i in range(n):
        for j in range(n):
            s=a[(i-1)%n][(j-1)%n]+a[(i-1)%n][j]+a[(i-1)%n][(j+1)%n]+a[i][(j-1)%n]+a[i][(j+1)%n]+a[(i+1)%n][(j-1)%n]+a[(i+1)%n][j]+a[(i+1)%n][(j+1)%n]
            if a[i][j]==1 and (s>=4 or s<=1):
                tmp[i][j]=-1
            if a[i][j]==0 and s==3:
                tmp[i][j]=1
    st=0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]!=0:
                st+=1
            a[i][j]+=tmp[i][j]
            tmp[i][j]=0
    plt.pause(0.2)
    fig.clear()
    plt.imshow(a)
    plt.draw()
    
