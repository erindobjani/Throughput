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
tlim=vmax*alpha
axx=[]
axy=[]

for i in range(1,nx, 1):

    if i*lx>=xlim:
        tavgx = vmax / 4 * alpha * (3 - nlimx / 3 / i) + (i * lx) / 2 / vmax * (1 - nlimx / i)
    else:
        tavgx = 2/3*math.sqrt(2*i*lx*alpha)

    if tavgx>=tlim:
        xavg = (tavgx - vmax / 2 * alpha) * vmax/lx
    else:
        xavg = tavgx * tavgx / 2 / alpha/lx

    axx.append(i)
    axy.append(xavg/i)


plt.plot(axx, axy)
plt.xlabel('Number of cells')
plt.ylabel('Cell approximating average time')
plt.show()