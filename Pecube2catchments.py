#!/usr/bin/env python3
"""
Merges topometric data and Pecube output into a single file.
"""

# Import libraries
#from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.interpolate import interp2d,RectBivariateSpline

#--- Pecube model details -----------------------------------------------------#
region='W'
resolution='250m'
pecuberes='1km'
writenumpts=False
writecsvheader=True
makeplot=False
converttokm=False

#--- Pecube model calculations ------------------------------------------------#
# if region=='W':
#     if pecuberes=='1km':
#         infile='DWW01_1km/VTK/Ages001.vtk'
#         nskip=4.0
#     elif pecuberes=='500m':
#         infile='DWW01_500m/VTK/Ages001.vtk'
#         nskip=2.0
#     xlon=89.0
#     xlat=26.5
#     nx0=652.0
#     ny0=870.0
#     dx=0.0023
#     dy=0.0023
#     zthick=50.0
#     catchments=['BH27','BH389','BH398','BH402','BH403','BH404','BH414','BH420','BH435']
#     if resolution=='250m':
#         catchfilesin=['BH27_merged_250m.csv','BH389_merged_250m.csv','BH398_merged_250m.csv','BH402_merged_250m.csv','BH403_merged_250m.csv','BH404_merged_250m.csv','BH414_merged_250m.csv','BH420_merged_250m.csv','BH435_merged_250m.csv']
#     elif resolution=='500m':
#         catchfilesin=['BH27_merged_500m.csv','BH389_merged_500m.csv','BH398_merged_500m.csv','BH402_merged_500m.csv','BH403_merged_500m.csv','BH404_merged_500m.csv','BH414_merged_500m.csv','BH420_merged_500m.csv','BH435_merged_500m.csv']
if region=='W':
    if pecuberes=='1km':
        #infile='WB009-1km/VTK/Ages001.vtk'
        #pecube_model='_WB009-1km'
        infile='WB012-1km/VTK/Ages001.vtk'
        pecube_model='_WB012-1km'
        #infile='WB014-1km/VTK/Ages001.vtk'
        #pecube_model='_WB014-1km'
        nskip=10.0
        #nskip=4.0
    xlon=88.25
    xlat=26.25
    nx0=3900
    ny0=3300
    dx=0.0008333
    dy=0.0008333
    #dx=0.0023
    #dy=0.0023
    zthick=50.0
    catchments=['BH27','BH389','BH398','BH402','BH403','BH404','BH414','BH435','SK075']
    if resolution=='250m':
        catchfilesin=['BH27_merged_250m.csv','BH389_merged_250m.csv','BH398_merged_250m.csv','BH402_merged_250m.csv','BH403_merged_250m.csv','BH404_merged_250m.csv','BH414_merged_250m.csv','BH435_merged_250m.csv','Torsa_merged_250m.csv']
    elif resolution=='500m':
        catchfilesin=['BH27_merged_500m.csv','BH389_merged_500m.csv','BH398_merged_500m.csv','BH402_merged_500m.csv','BH403_merged_500m.csv','BH404_merged_500m.csv','BH414_merged_500m.csv','BH435_merged_500m.csv','Torsa_merged_500m.csv']
elif region=='CW':
    if pecuberes=='1km':
        infile='DWCW1_1km/VTK/Ages001.vtk'
        nskip=4.0
    elif pecuberes=='500m':
        infile='DWCW1_500m/VTK/Ages001.vtk'
        nskip=2.0
    xlon=90.0
    xlat=26.5
    nx0=652.0
    ny0=870.0
    dx=0.0023
    dy=0.0023
    zthick=50.0
elif region=='CE':
    if pecuberes=='1km':
        infile='DWCE1_1km/VTK/Ages002.vtk'
        nskip=4.0
    elif pecuberes=='500m':
        infile='DWCE1_500m/VTK/Ages002.vtk'
        nskip=2.0
    xlon=90.0
    xlat=26.5
    nx0=652.0
    ny0=1087.0
    dx=0.0023
    dy=0.0023
    zthick=50.0
    catchments=['BH354','BH364','BH365','BH369','BH370','BH382']
    if resolution=='250m':
        catchfilesin=['BH354_merged_250m.csv','BH364_merged_250m.csv','BH365_merged_250m.csv','BH369_merged_250m.csv','BH370_merged_250m.csv','BH382_merged_250m.csv']
    elif resolution=='500m':
        catchfilesin=['BH354_merged_500m.csv','BH364_merged_500m.csv','BH365_merged_500m.csv','BH369_merged_500m.csv','BH370_merged_500m.csv','BH382_merged_500m.csv']
elif region=='E':
    if pecuberes=='1km':
        infile='DWE01_1km/VTK/Ages002.vtk'
        nskip=4.0
    elif pecuberes=='500m':
        infile='DWE01_500m/VTK/Ages002.vtk'
        nskip=2.0
    xlon=91.0
    xlat=26.5
    nx0=652.0
    ny0=1087.0
    dx=0.0023
    dy=0.0023
    zthick=50.0
    catchments=['BH381','EasternBhutan']
    if resolution=='250m':
        catchfilesin=['BH381_merged_250m.csv','EasternBhutan_merged_250m.csv']
    elif resolution=='500m':
        catchfilesin=['BH381_merged_500m.csv','EasternBhutan_merged_500m.csv']
elif region=='MANAS':
    if pecuberes=='1km':
        infile='MAN14_1km/VTK/Ages001.vtk'
        nskip=1.0
    else:
        print('Invalid Pecube resolution ('+pecuberes+'). Exiting...')
        sys.exit(1)
    xlon=90.0
    xlat=26.5
    nx0=250.0
    ny0=250.0
    dx=0.01
    dy=0.01
    zthick=50.0
    catchments=['MAN14']
    if resolution=='250m':
        catchfilesin=['Manas_merged_250m.csv']
    elif resolution=='500m':
        catchfilesin=['Manas_merged_500m.csv']
elif region=='TORSA':
    if pecuberes=='1km':
        infile='SK075_1km/VTK/Ages001.vtk'
        nskip=2.0
    elif pecuberes=='500m':
        infile='DWE01_500m/VTK/Ages001.vtk'
        nskip=1.0
    xlon=88.5
    xlat=26.5
    nx0=300.0
    ny0=400.0
    dx=0.005
    dy=0.005
    zthick=50.0
    catchments=['SK075']
    if resolution=='250m':
        catchfilesin=['Torsa_merged_250m.csv']
    elif resolution=='500m':
        catchfilesin=['Torsa_merged_500m.csv']
else:
    print('Invalid region ('+region+'). Exiting...')
    sys.exit(1)

# Calculate topography parameters
nx=(nx0-1)/nskip+1
ny=(ny0-1)/nskip+1
nx = int(nx)
ny = int(ny)
xlon1=xlon
xlat1=xlat
xlon2=xlon+(nx-1)*dx*nskip
xlat2=xlat+(ny-1)*dy*nskip

# Open input age file
print('Reading input age file '+infile+'...',end='')
sys.stdout.flush()
reader = open(infile, 'r')

# Read in ASCII VTK header
for line in range(4):
    reader.readline()

# Read in x, y, z point coordinates
line=reader.readline().split()
numpts=int(line[1])
#x=np.zeros(numpts)
#y=np.zeros(numpts)
#z=np.zeros(numpts)

# Make data grids
if converttokm:
    xg=np.zeros(nx)
    yg=np.zeros(ny)
else:
    xg=np.linspace(xlon1,xlon2,nx)
    yg=np.linspace(xlat1,xlat2,ny)

# Create elevation array
zg=np.zeros([ny,nx])

nxcnt=0
nycnt=0
xlinecnt=0
for i in range(numpts):
    line=reader.readline().split()
    if converttokm and nycnt==0:
        xlinecnt+=1
        xg[i]=line[0]
    #x[i]=line[0]
    #y[i]=line[1]
    #z[i]=float(line[2])
    # Convert to latitude and longitude, and elevation in meters
    #x[i]=x[i]/(111.11*np.cos((xlat+(xlat2-xlat1)/2.)*np.pi/180.))+xlon1
    #y[i]=y[i]/111.11+xlat1
    zg[nycnt,nxcnt]=(float(line[2])-zthick)*1000.0
    nxcnt+=1
    if nxcnt == int(nx):
        if converttokm:
            yg[nycnt]=line[1]
        nxcnt=0
        nycnt+=1

# Read number of elements (cells), skip over them
line=reader.readline().split()
numelem=int(line[1])
for i in range(numelem):
    reader.readline()

# Read and skip over cell types
reader.readline()
for i in range(numelem):
    reader.readline()

# Read in point data header info
line=reader.readline().split()
datatype=line[0]

# Declare grid arrays
edotg=np.zeros([ny,nx])
AHeg=np.zeros([ny,nx])
ZHeg=np.zeros([ny,nx])
AFTg=np.zeros([ny,nx])
ZFTg=np.zeros([ny,nx])
KArg=np.zeros([ny,nx])
BArg=np.zeros([ny,nx])
MArg=np.zeros([ny,nx])
HArg=np.zeros([ny,nx])
meanFTLg=np.zeros([ny,nx])
ramang=np.zeros([ny,nx])

# Read in exhumation rates
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    edotg[nycnt,nxcnt]=line[0]
    #print(edotg[nycnt,nxcnt])
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in AHe ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    AHeg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in ZHe ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    ZHeg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in AFT ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    AFTg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in ZFT ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    ZFTg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in KAr ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    KArg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in BAr ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    BArg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in MAr ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    MArg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in HAr ages
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    HArg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in mean apatite fission track lengths
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    meanFTLg[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

# Read in peak raman T
reader.readline()
reader.readline()
nxcnt=0
nycnt=0
for i in range(numpts):
    line=reader.readline().split()
    ramang[nycnt,nxcnt]=line[0]
    nxcnt+=1
    if nxcnt == int(nx):
         nxcnt=0
         nycnt+=1

reader.close()
print('done.')

print('Creating interpolation functions...',end='')
sys.stdout.flush()
#interpelevPecube=interp2d(xg,yg,zg,kind='linear')
interpelevPecube=RectBivariateSpline(yg,xg,zg,kx=1,ky=1)
#interpedot=interp2d(xg,yg,edotg,kind='linear')
interpedot=RectBivariateSpline(yg,xg,edotg,kx=1,ky=1)
#interpAHe=interp2d(xg,yg,AHeg,kind='linear')
interpAHe=RectBivariateSpline(yg,xg,AHeg,kx=1,ky=1)
#interpZHe=interp2d(xg,yg,ZHeg,kind='linear')
interpZHe=RectBivariateSpline(yg,xg,ZHeg,kx=1,ky=1)
#interpAFT=interp2d(xg,yg,AFTg,kind='linear')
interpAFT=RectBivariateSpline(yg,xg,AFTg,kx=1,ky=1)
#interpZFT=interp2d(xg,yg,ZFTg,kind='linear')
interpZFT=RectBivariateSpline(yg,xg,ZFTg,kx=1,ky=1)
#interpKAr=interp2d(xg,yg,KArg,kind='linear')
interpKAr=RectBivariateSpline(yg,xg,KArg,kx=1,ky=1)
#interpBAr=interp2d(xg,yg,BArg,kind='linear')
interpBAr=RectBivariateSpline(yg,xg,BArg,kx=1,ky=1)
#interpMAr=interp2d(xg,yg,MArg,kind='linear')
interpMAr=RectBivariateSpline(yg,xg,MArg,kx=1,ky=1)
#interpHAr=interp2d(xg,yg,HArg,kind='linear')
interpHAr=RectBivariateSpline(yg,xg,HArg,kx=1,ky=1)
#interpmeanFTL=interp2d(xg,yg,meanFTLg,kind='linear')
interpmeanFTL=RectBivariateSpline(yg,xg,meanFTLg,kx=1,ky=1)
#interpraman=interp2d(xg,yg,ramang,kind='linear')
interpraman=RectBivariateSpline(yg,xg,ramang,kx=1,ky=1)
print('done.')

for i in range(len(catchments)):
    print('Processing basin '+catchments[i]+'...',end='')
    sys.stdout.flush()
    catchfileout=catchments[i]+pecube_model+'_Pecube_and_topometrics_'+resolution+'.csv'
    reader = open('table_'+resolution+'/'+catchfilesin[i], 'r')
    writer = open(catchfileout, 'w')
    data=reader.readlines()
    numlines=int(len(data))

    # Make arrays
    if makeplot==True:
        catchlatplot=np.zeros(numlines-1)
        catchlonplot=np.zeros(numlines-1)
        catchelevplot=np.zeros(numlines-1)
#         catchelevPecubeplot=np.zeros(numlines-1)
#         catchedotplot=np.zeros(numlines-1)
#         catchAHeplot=np.zeros(numlines-1)
#         catchZHeplot=np.zeros(numlines-1)
        catchAFTplot=np.zeros(numlines-1)
#         catchZFTplot=np.zeros(numlines-1)
#         catchKArplot=np.zeros(numlines-1)
#         catchBArplot=np.zeros(numlines-1)
#         catchMArplot=np.zeros(numlines-1)
#         catchHArplot=np.zeros(numlines-1)
#         catchmeanFTLplot=np.zeros(numlines-1)
#         catchramanplot=np.zeros(numlines-1)
#         catchGeolIDplot=np.zeros(numlines-1)
#         catchGlacIDplot=np.zeros(numlines-1)
#         catchMorIDplot=np.zeros(numlines-1)
#         catchRGIDplot=np.zeros(numlines-1)
        catchKsnplot=np.zeros(numlines-1)
#         catchKsn_t045plot=np.zeros(numlines-1)
#         catchKsn_t2plot=np.zeros(numlines-1)
#         catchKsn_t3plot=np.zeros(numlines-1)
#         catchKsn_t2mplot=np.zeros(numlines-1)
#         catchKsn_t3mplot=np.zeros(numlines-1)
#         catchKsn_t2t4plot=np.zeros(numlines-1)
#         catchKsn_t3t4plot=np.zeros(numlines-1)
#         catchKsn_t2mt4plot=np.zeros(numlines-1)
#         catchKsn_t3mt4plot=np.zeros(numlines-1)
#         catchsspplot=np.zeros(numlines-1)
#         catchssp_t2b31plot=np.zeros(numlines-1)
#         catchssp_t3b42plot=np.zeros(numlines-1)

    if writenumpts==True:
        writer.write(str(numlines-1)+'\n')
    if writecsvheader==True:
        writer.write('lat,lon,elev,Pecube elev,edot,AHe,ZHe,AFT,ZFT,KAr,BAr,MAr,HAr,Mean FTL,Raman,GeolID,GlacID,MorID,RGID,Ksn,Ksn_t045,Ksn_t2,Ksn_t3,Ksn_t2m,Ksn_t3m,Ksn_t2t4,Ksn_t3t4,Ksn_t2mt4,Ksn_t3mt4,ssp,ssp_t2b31,ssp_t3b42\n')
    for j in range(numlines-1):
#    for j in range(100):
        datalist=data[j+1].split(',')
        catchlatf=float(datalist[0])
        catchlonf=float(datalist[1])
        if converttokm:
            catchlatf=(catchlatf-xlat1)*111.11
            catchlonf=(catchlonf-xlon1)*111.11*np.cos((xlat+(xlat2-xlat1)/2.)*np.pi/180.)
        if makeplot==True:
            catchlatplot[j]=catchlatf
            catchlonplot[j]=catchlonf
        catchelev=datalist[2]
        #catchelevplot[j]=catchelev
        #catchtopometrics[i]=datalist[3]+','+datalist[4]+','+datalist[5]+','+datalist[6]+','+datalist[7]+','+datalist[8]+','+datalist[9]+','+datalist[10]+','+datalist[11]+','+datalist[12]+','+datalist[13]+','+datalist[14]+','+datalist[15]
        catchGeolID=datalist[3]
        catchGlacID=datalist[4]
        catchMorID=datalist[5]
        catchRGID=datalist[6]
        catchKsn=datalist[7]
        if makeplot==True:
            catchKsnplot[j]=catchKsn
        catchKsn_t045=datalist[8]
        catchKsn_t2=datalist[9]
        catchKsn_t3=datalist[10]
        catchKsn_t2m=datalist[11]
        catchKsn_t3m=datalist[12]
        catchKsn_t2t4=datalist[13]
        catchKsn_t3t4=datalist[14]
        catchKsn_t2mt4=datalist[15]
        catchKsn_t3mt4=datalist[16]
        catchssp=datalist[17]
        catchssp_t2b31=datalist[18]
        catchssp_t3b42=datalist[19]
        catchelevPecube=interpelevPecube(catchlatf,catchlonf)
        #catchelevPecubeplot[j]=catchelevPecube
        # Enforce minimum exhumation rate of 0.0
        catchedot=interpedot(catchlatf,catchlonf)
        catchedot=max(catchedot[0][0],0.0)
        #catchedotplot[j]=catchedot
        catchAHe=interpAHe(catchlatf,catchlonf)
        catchZHe=interpZHe(catchlatf,catchlonf)
        catchAFT=interpAFT(catchlatf,catchlonf)
        if makeplot==True:
            catchAFTplot[j]=catchAFT
        catchZFT=interpZFT(catchlatf,catchlonf)
        catchKAr=interpKAr(catchlatf,catchlonf)
        catchBAr=interpBAr(catchlatf,catchlonf)
        catchMAr=interpMAr(catchlatf,catchlonf)
        catchHAr=interpHAr(catchlatf,catchlonf)
        catchmeanFTL=interpmeanFTL(catchlatf,catchlonf)
        catchraman=interpraman(catchlatf,catchlonf)
        # write line to file...
#         print('start')
#         print(interpelevPecube(catchlatf,catchlonf))
#         print(catchelevPecube)
#         print(catchelevPecube[0])
#         print(str(catchelevPecube))
#         print(str(catchelevPecube[0]))
#         print(str(catchelevPecube[0][0]))
#         print('end')
        writer.write(str(catchlatf)+','+str(catchlonf)+','+catchelev+','
            +str(catchelevPecube[0][0])+','+str(catchedot)+','
            +str(catchAHe[0][0])+','+str(catchZHe[0][0])+','
            +str(catchAFT[0][0])+','+str(catchZFT[0][0])+','
            +str(catchKAr[0][0])+','+str(catchBAr[0][0])+','
            +str(catchMAr[0][0])+','+str(catchHAr[0][0])+','
            +str(catchmeanFTL[0][0])+','+str(catchraman[0][0])+','
            +catchGeolID+','+catchGlacID+','+catchMorID+','+catchRGID+','
            +catchKsn+','+catchKsn_t045+','+catchKsn_t2+','+catchKsn_t3+','
            +catchKsn_t2m+','+catchKsn_t3m+','+catchKsn_t2t4+','+catchKsn_t3t4
            +','+catchKsn_t2mt4+','+catchKsn_t3mt4+','+catchssp+','
            +catchssp_t2b31+','+catchssp_t3b42+'\n')

    reader.close()
    writer.close()
    print('done.')

    if makeplot==True:
        fig=plt.figure()
        cmap = plt.cm.get_cmap('jet',12)
        v=np.linspace(0.0,12.0,13,endpoint=True)
        #plt.contourf(xg,yg,AFTg,v,cmap=cmap)#,cmap=cmap,vmin=0.0,vmax=7000.0)
        #plt.colorbar()
        #plt.plot(catchlonplot[0:100],catchlatplot[0:100],'k.')
        #plt.scatter(catchlonplot[0:99],catchlatplot[0:99],c=catchedotplot[0:99],marker='o',cmap=cmap,vmin=-15.0,vmax=5.0)
        #plt.scatter(catchlonplot,catchlatplot,color=catchedotplot,edgecolor='none')
        #plt.scatter(catchlonplot,catchlatplot,c=catchAFTplot,marker='o',edgecolor='none',cmap=cmap,vmin=0.0,vmax=8.0)#,cmap=cmap,edgecolor='none',vmin=0.0,vmax=7000.0)
        plt.scatter(catchlonplot,catchlatplot,c=catchKsnplot,marker='o',edgecolor='none',cmap=cmap,vmin=0.0,vmax=10.0)#,cmap=cmap,edgecolor='none',vmin=0.0,vmax=7000.0)
        plt.colorbar()
        plt.savefig('test.png',transparent=True)
        plt.show()
