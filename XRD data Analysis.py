import matplotlib as mpl
mpl.__version__
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import math
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

# plot xy fig
def plotxy(figname, x, y):
    plt.style.use('seaborn')
    mpl.rcParams['font.family'] = 'serif'
    # matplotlib inline
    #np.random.seed(1000)
    #y = np.random.standard_normal(20)
    #x = np.arange(len(y))
    #print(y)
    #print(x)
    plt.plot(x, y)
    plt.grid(False)
    plt.axis('equal')
    plt.axis('tight')
    plt.xlabel(r'2Theta/°')
    plt.ylabel("Intensity/conts")
    plt.savefig("XRD Rocking curve"+str(figname)+".jpg")

def plotrsm(figname, x, y, z):
    plt.style.use('seaborn')
    mpl.rcParams['font.family'] = 'serif'
    # matplotlib inline
    #np.random.seed(1000)
    #y = np.random.standard_normal(20)
    #x = np.arange(len(y))
    #print(y)
    #print(x)
    #print(z)
    xo = np.float16(x)
    yo = np.float16(y)
    zo = np.float16(z)
    print(xo)
    print(yo)
    xu = np.unique(xo)
    yu = np.unique(yo)
    xm, ym = np.meshgrid(xu, yu)
    zm = []
    for j in yu:
        zoo = []
        for i in xu:
            zoo_index = np.intersect1d(np.argwhere(xo == i), np.argwhere(yo == j))
            #print("zoo_index", zoo_index)
            #zoo = zoo.astype(np.float)
            zoo.append(float(zo[zoo_index[0]]))
        zm.append(zoo)
    #Zm = np.squeeze(Zm)
    #print(zm_index)
    #print(Zm)
    plt.contourf(xm, ym, zm)
#    plt.contour(x, y, z)
    plt.grid(False)
    plt.axis('equal')
    plt.axis('tight')
    plt.xlabel(r'2Theta/°')
    plt.ylabel("Intensity/conts")
    plt.savefig("XRD RSM"+str(figname)+".jpg")



def dataxy(filename):
    #data = pd.read_csv(filename, sep=' ', skipinitialspace=1)
    #读入原始数据文件
    #filepath = str(filename)
    #with open(filepath, 'r') as f:
    #    file = f.read()
    #data = file.split()
    #data = np.array(data, dtype=float)
    #data = data.reshape(-1, 2)
    data = np.loadtxt(filename)
    return data

def data2rsm(filename):
    #data = pd.read_csv(filename, sep=' ', skipinitialspace=1)
    #读入原始数据文件RSM01
    data = np.loadtxt(filename)

    x = data[:, 0]*np.pi/180
    y = data[:, 1]*np.pi/180
    z = data[:, 2]

    #print(data[:, 0])
    #print(data[:, 1])
    #print(data[:, 2])


    #处理数据
    Xraylambda = 1.540598
    R = 2*np.pi/Xraylambda
    Qx = R*(np.cos(x) - np.cos(y - x))
    Qy = R*(np.sin(x) + np.sin(y - x))
    #print(Qx)
    #print(Qy)
    #print(data_rsm[:, 0])
    #print(data_rsm)
    #save the result
    #filename_rsm_out = str(filename)+"RSM_out.csv"
    #data_rsm.to_csv(filename_rsm_out)     #将处理后的数据写入到文件RSM_out.csv
    return Qx, Qy, z


print("01. 摇摆曲线作图")
print("02. XRD RSM作图")
function_select = int(input("请输入功能对应的序号："))

if function_select == 1:
    filename = input("请输入文件名（本文件夹下）或文件完整目录：")
    data = dataxy(filename)
    print(date)
    figname = input("请输入图片的保存名称：")
    x = data[:, 0]
    y = data[:, 1]
    plotxy(figname, x, y)
elif function_select == 2:
    filename = input("请输入文件名（本文件夹下）或文件完整目录：")
    x, y, z = data2rsm(filename)
    #figname = input("请输入图片的保存名称：")
    #plotrsm(figname, x, y, z)
    data_name_rsm = str(input("请输入RSM数据的保存名称："))
    x = pd.DataFrame(x)
    x.to_csv('{}-x.csv'.format(data_name_rsm))
    y = pd.DataFrame(y)
    y.to_csv('{}-y.csv'.format(data_name_rsm))
    z = pd.DataFrame(z)
    z.to_csv('{}-z.csv'.format(data_name_rsm))
    print("RSM数据已输出完成,导入后请删除首行数据。")
