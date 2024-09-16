import math
import random
import numpy as np
import xlsxwriter

'''Check shuffling time!!!!!!!!!!!!!!!'''


vmax=3.1
vz=1.6
aa=0.8
ad=-0.8
nx=75
ny=95
nz=14
lx=0.4
ly=0.6
hz=0.31
hio=1
fr=0.1

alpha=1/aa-1/ad

xlim=vmax*vmax*alpha/2




#create empty grid
grid=np.zeros((nx, ny), dtype=int)

#randomly fill grid
for i in range(0, nx, 1):
    for j in range(0, ny, 1):
        grid[i, j] = random.randint(0, nz)

gridsum=grid.sum()

while gridsum != fr*nx*ny*nz:
    if gridsum >= fr*nx*ny*nz:
        randx = random.randint(0, nx-1)
        randy = random.randint(0, ny-1)
        if grid[randx][randy]!=0:
            grid[randx][randy]=grid[randx][randy]-1

    elif gridsum < fr*nx*ny*nz:
        randx = random.randint(0, nx-1)
        randy = random.randint(0, ny-1)
        if grid[randx][randy]!=nz:
            grid[randx][randy]=grid[randx][randy]+1
    gridsum = grid.sum()

print(grid)
print(grid.sum())
avginc=0
avgouc=0
avgcoc=0

ting=[]
toug=[]
tcog=[]
i=0
while i<1000:

    tzio=2*vz/(nz*hz-hio)

    #Put bin into grid
    check1=0
    while check1==0:
        rax = random.randint(0, nx-1)
        ray = random.randint(0, ny-1)

        #dropoff time horizontal
        if grid[rax][ray]!=nz:
            #Travel to x
            if rax * lx <= xlim:
                tix = math.sqrt(2 * rax * lx * alpha)
            else:
                tix = 0.5 * vmax * alpha + rax * lx / vmax

            #Travel to y
            if ray * ly <= xlim:
                tiy = math.sqrt(2 * ray * ly * alpha)
            else:
                tiy = 0.5 * vmax * alpha + ray * ly / vmax

            #Drop to z
            h=grid[rax][ray]
            tzin = vz/(nz-h)/hz
            check1=1

    #Remove bin from gird
    check2=0
    while check2!=2:
        check2 = 0
        prax = random.randint(0, nx-1)
        pray = random.randint(0, ny-1)

        if grid[prax][pray]!=0:
            praz=random.randint(1, int(grid[prax][pray]))    #select bin to remove
            # pickup time horizontal
            # Travel to x
            if prax * lx <= xlim:
                tax = math.sqrt(2 * prax * lx * alpha)
            else:
                tax = 0.5 * vmax * alpha + prax * lx / vmax

            # Travel to y
            if pray * ly <= xlim:
                tay = math.sqrt(2 * pray * ly * alpha)
            else:
                tay = 0.5 * vmax * alpha + pray * ly / vmax
            check2=check2+1


            # Travel to x new
            if abs(prax-rax) * lx <= xlim:
                tox = math.sqrt(2 * abs(prax-rax) * lx * alpha)
            else:
                tox = 0.5 * vmax * alpha + abs(prax-rax) * lx / vmax

            # Travel to y new
            if abs(pray-ray) * ly <= xlim:
                toy = math.sqrt(2 * abs(pray-ray) * ly * alpha)
            else:
                toy = 0.5 * vmax * alpha + abs(pray-ray) * ly / vmax

            #travel back to iox
            if prax * lx <= xlim:
                toxo = math.sqrt(2 * prax * lx * alpha)
            else:
                toxo = 0.5 * vmax * alpha + prax * lx / vmax

            # Travel to ioy
            if pray * ly <= xlim:
                toyo = math.sqrt(2 * pray * ly * alpha)
            else:
                toyo = 0.5 * vmax * alpha + pray * ly / vmax

            #horizontal travel time for shuffling
            sumh=0
            for counth in range(1, grid[prax][pray]-praz+1):
                sumh=sumh+math.sqrt(counth)
            tremh=2*math.sqrt(2*ly*alpha)*sumh

            # vertical travel time for shuffling
            sumv=0
            for countv in range(1, grid[prax][pray]-praz+2):
                sumv=sumv+(countv+nz-grid[prax][pray])
            tremv=2*hz/vz*sumv
            check2=check2+1

    tin=2*tzio+2*(tix+tiy)+2*tzin
    tout=2*tzio+2*(tax+tay)+tremv+tremh
    tcomb=2*tzio+tix+tiy+tax+tay+toxo+toyo+tremh+tremv

    ting.append(float(round(tin, 2)))
    toug.append(float(round(tout, 2)))
    tcog.append(float(round(tcomb, 2)))

    avginc=avginc+tin
    avgouc=avgouc+tout
    avgcoc=avgcoc+tcomb
    print('tin= %.2f' % tin)
    print('-----')
    print('tout= %.2f' % tout)
    print('-----')
    print('tcomb= %.2f' % tcomb)
    print('---------------')
    i=i+1
tavgin=avginc/i
tavgou=avgouc/i
tavgco=avgcoc/i

print('tavgin= %.2f' % tavgin)
print('tavgout= %.2f' % tavgou)
print('tavgcomb= %.2f' % tavgco)

workbook = xlsxwriter.Workbook('testout.xlsx')
worksheet = workbook.add_worksheet()
row = 2
column = 2

for item in ting:
    worksheet.write(row, column, item)
    row=row+1

row=2
column=3
for item in toug:
    worksheet.write(row, column, item)
    row=row+1

row=2
column=4
for item in tcog:
    worksheet.write(row, column, item)
    row=row+1

workbook.close()



'''for x in range(1,nx+1,1):
    if x*lx<=xlim:
        tx=math.sqrt(2*x*lx*alpha)
    else:
        tx=0.5*vmax*alpha+x*lx/vmax
    #print(tx)
    totx=totx+tx
tavgx=totx/x

#print('---------------------------')

toty=0
for y in range(1,ny+1,1):
    if y*ly<=xlim:
        ty=math.sqrt(2*y*ly*alpha)
    else:
        ty=0.5*vmax*alpha+y*ly/vmax
    #print(ty)
    toty=toty+ty
tavgy=toty/y

print(tavgx)
print(tavgy)
'''
