import math
import matplotlib.pyplot as plt
#inputs

vmax=3.1
vz=1.6
aa=0.8
ad=0.8
nx=75
ny=95
nz=14
lx=0.4
ly=0.6
hz=0.31
hio=1
fr=1


if ad<=0:
    ad=ad
else:
    ad=-ad

allx=lx*nx
ally=ly*ny

#step 1
nf=nz*fr
nr=math.ceil(nf/2)
nl=math.ceil(nz-nf)
hzz=nz*hz
alpha=1/aa-1/ad

#step 2
xlim=vmax*vmax*alpha/2
nlimx=math.floor(xlim/lx)
nlimy=math.floor(xlim/ly)

#step 3
if nx*lx>=xlim:
    tavgx = vmax / 4 * alpha * (3 - nlimx / 3 / nx) + (nx * lx) / 2 / vmax * (1 - nlimx / nx)
else:
    tavgx = 2/3*math.sqrt(2*nx*lx*alpha)

if ny*ly>=xlim:
    tavgy = vmax / 4 * alpha * (3 - nlimy / 3 / ny) + (ny * ly) / 2 / vmax * (1 - nlimy / ny)
else:
    tavgy = 2/3*math.sqrt(2*ny*ly*alpha)

print('tavgx= ', tavgx)
print('tavgy= ', tavgy)

#step 5
sumo=int(0)
for i in range(0,nr,1):
    sumo=sumo+(nl+i)
tztot=2*hz/vz*sumo

sumo=int(0)
for j in range(1,nr,1):
    sumo=sumo+math.sqrt(j)
thtot=2*math.sqrt(2*ly*alpha)*sumo

tzin=(nl-1)*hz/vz
tzio=(hzz-hio)/vz

print('tztot=', tztot)
print('thtot=', thtot)
print('tzin= ', tzin)
print('tzio=', tzio)

#step 6
tin=2*tzio+2*(tavgx+tavgy)+2*tzin
tout=2*tzio+2*(tavgx+tavgy)+thtot+tztot
tcomb=4*tzio+2.66*(tavgx+tavgy)+thtot+tztot

print('tin= %.2f s' % tin)
print('tout= %.2f s' % tout)
print('tcomb= %.2f s' % tcomb)
print()

tavgxsup=nx*lx/2/vmax
