#!/usr/bin/python
import sys
import math

filename=r'C:\\tomcat-9\\webapps\\down\\files\\'+sys.argv[1]
filesave=sys.argv[1][0:-4]
localfn =open(filename,'r',encoding='utf-8-sig')
localf=localfn.readlines()
localfn.close()
from numpy import genfromtxt, zeros

x = genfromtxt(localf,delimiter=',',usecols=(0),dtype=str)
y = genfromtxt(localf,delimiter=',',usecols=(1),dtype=str)
xname = x[0]
yname = y[0]
x = x[1:]
y = y[1:]
y = list(map(float,y))
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#线图
fig=plt.figure(dpi=125,figsize=(15,6))
plt.plot(x,y)
plt.xlabel(xname)
plt.ylabel(yname)
plt.title('')
plt.savefig(r'C:\\tomcat-9\\webapps\\down\\resources\\'+filesave+'-折线图.png')
#散点图
fig=plt.figure(dpi=125,figsize=(15,6))
plt.scatter(x,y)
plt.xlabel(xname)
plt.ylabel(yname)
plt.title('')
plt.savefig(r'C:\\tomcat-9\\webapps\\down\\resources\\'+filesave+'-散点图.png')

#柱状图
fig=plt.figure(dpi=125,figsize=(15,6))
plt.bar(x,y)
plt.xlabel(xname)
plt.ylabel(yname)
plt.title('')
plt.savefig(r'C:\\tomcat-9\\webapps\\down\\resources\\'+filesave+'-柱状图.png')
