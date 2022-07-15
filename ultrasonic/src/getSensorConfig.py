import serial
import serial.tools.list_ports as port_list
from connectultra import *

import pandas as pd

sensor_configData = []
sensor_configData_id = []
sensor_configData_iswork = []


# sensor_configData = pd.read_csv("ultraSensor_id_config.txt",usecols=[0])

def transformToList(transList):  # 将dataframe转化为list
    newlist = []
    transList = transList.values.tolist()
    for i in range(len(transList)):
        newlist.append(transList[i][0])
    return newlist


def transformToList_str(transList):  # 将dataframe转化为list
    newlist = []
    transList = transList.values.tolist()
    for i in range(len(transList)):
        newlist.append(str(transList[i][0]))
    return newlist


def getColumnData(filename, ColumnNum):  # 获取列项数据并适配
    colummDataList = pd.read_csv(filename, usecols=[ColumnNum])
    colummDataList = transformToList(colummDataList)
    return colummDataList


def getColumnData_str(filename, ColumnNum):  # 获取列项数据并适配
    colummDataList = pd.read_csv(filename, usecols=[ColumnNum])
    colummDataList = transformToList_str(colummDataList)
    return colummDataList

def getWorkingSensorCount():
    n=len(sensor_configData_iswork)
    Count=0
    for i in range(n):
        if sensor_configData_iswork[i]==1:
            Count=Count+1
    return Count

def getWorkingSensorIdList():
    newlist=[]
    n = len(sensor_configData_iswork)
    Count = 0
    for i in range(n):
        if sensor_configData_iswork[i] == 1:
            newlist.append(sensor_configData_id[i])
    return newlist


sensor_configData_id = getColumnData("/home/zz/catkin_ws/src/ultrasonic_topic/src/ultraSensor_id_config.txt", 0)
sensor_configData_iswork = getColumnData("/home/zz/catkin_ws/src/ultrasonic_topic/src/ultraSensor_id_config.txt", 1)


if __name__ == '__main__':
    print(getWorkingSensorCount())
    print(getWorkingSensorIdList())

