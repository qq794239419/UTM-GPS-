import pyproj
import csv
import numpy as np
def gps_to_utm(longitude,latitude) :
    p1 = pyproj.Proj(init="epsg:4326")#wgs坐标系统的EPSG Code
    p2 = pyproj.Proj(init="epsg:32647")#wgs坐标系统的EPSG Code
    x, y = pyproj.transform(p1, p2,float(longitude),-float(latitude))
    # print(x,y)
    return [x,y]

def read_csv(path):  # 读取csv文件
    with open(path, 'r') as csv_file:
        lines = csv.reader(csv_file)
        # print(csv_file) #可以先输出看一下该文件是什么样的类型
        content = []  # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行

        for line in lines:
            # print(line) #打印文件每一行的信息
            content.append(line)
    return content
def transform_all(csv_file):
    gps_0845=read_csv('kl_gps_%s.csv'%csv_file)
    utm_0845=[]
    c1=[]
    c2=[]
    for i in range(len(gps_0845)):
        # print(i)
        print('正在转换',i,'还剩余',len(gps_0845)-i,'个', '\r', end='')
        utm_0845.append(gps_to_utm(gps_0845[i][1],gps_0845[i][0]))
    # print(utm_0845[0:3:1])

    for i in utm_0845:
        c1.append(i[0])
        c2.append(i[1])

    with open('kt_utm_%s.csv'%csv_file,"w",newline="") as datacsv:

        csvwriter = csv.writer(datacsv,dialect = ("excel"))

        csvwriter.writerow(c1)
        csvwriter.writerow(c2)
# print(gps_0845[0])
# print(gps_to_utm(gps_0845[0][1],gps_0845[0][0]))
# gps_to_utm(153.00236500000000000000, -27.50407166666666500000)
all=['q','db']
for s in all:
    transform_all(s)