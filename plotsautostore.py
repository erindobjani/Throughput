import math
import matplotlib.pyplot as plt
import numpy as np

vmax=3.1
aa=0.8
ad=0.8
nx=200
lx=0.4

if ad<=0:
    ad=ad
else:
    ad=-ad

alpha=1/aa-1/ad

xlim=vmax*vmax*alpha/2
nlimx=math.floor(xlim/lx)

axx=[]
axy=[]

for i in range(1,nx, 1):

    if i*lx>=xlim:
        tavgx = vmax / 4 * alpha * (3 - nlimx / 3 / i) + (i * lx) / 2 / vmax * (1 - nlimx / i)
    else:
        tavgx = 2/3*math.sqrt(2*i*lx*alpha)

    if i*lx/2>=xlim:
        tavgxh = vmax / 4 * alpha * (3 - nlimx / 3 / i*2) + (i * lx/2) / 2 / vmax * (1 - nlimx / i*2)
    else:
        tavgxh = 2/3*math.sqrt(2*i*lx*alpha/2)

    rep=tavgxh/tavgx
    axx.append(i)
    axy.append(rep)


plt.plot(axx, axy)
plt.xlabel('Number of cells')
plt.ylabel('t\'/t')
plt.show()