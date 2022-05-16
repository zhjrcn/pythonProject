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
    x, y = np.meshgrid(x, y)
    z =
    plt.contourf(x, y, z)
    #plt.contour(x, y, z)
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

    print(type(x))
    #print(data[:, 1])
    #print(data[:, 2])


    #处理数据
    Xraylambda = 1.540598
    R = 2*np.pi*Xraylambda
    Qx = R*(np.cos(y) - np.cos(x - y))
    Qy = R*(np.sin(y) + np.sin(x - y))
    data_rsm = np.vstack((Qx, Qy, z))
    print(data_rsm)
    #save the result
    #filename_rsm_out = str(filename)+"RSM_out.csv"
    #data_rsm.to_csv(filename_rsm_out)     #将处理后的数据写入到文件RSM_out.csv
    return data_rsm



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
    data = data2rsm(filename)
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    figname = input("请输入图片的保存名称：")
    plotrsm(figname, x, y, z)
