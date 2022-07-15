'''
Written by Amir A Mokhtarzadeh
Date: Feb 2022
HuaiYin Institute of Technology - China
All right reserved for the Author
No part of this script can be copied,
changed without the Authors permission.
If any part of this script used in any documents,
or production, this disclaimer must be displayed with it.
'''

import serial
import serial.tools.list_ports as port_list
from SerialUltra import *
from src.getSensorConfig import getWorkingSensorCount, getWorkingSensorIdList

ports = list(port_list.comports())
# port = ports[0].device
baudrate = 9600
serialPort = ""
port = "/dev/ttyUSB0"


# port = 'COM5'


def connection(po):
    global serialPort
    try:
        serialPort = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=1)
        print("Serial Port is opened as:", po)
        return 1
    except:
        print("Failed to open serial port:", po)
        return 0


def connection485(po):
    global serialPort
    try:
        send = serial.Serial(
            # port='/dev/ttyUSB0',
            port='COM5',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        # print("Serial Port is oppened as:", po)
        return 1
    except:
        return 0


def readtest(num):
    sens1 = SerialUltra(serialPort, 5, num)
    return sens1.read()


def serialPortOpen():
    connection(port)


def serialPortClose():
    serialPort = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=1)
    serialPort.close()


def testSensorState():
    count = getWorkingSensorCount()  # working sensor count
    wsList = getWorkingSensorIdList()  # working sensor id list
    list = []
    for i in range(count):
        distance = readtest(wsList[n - 1])
        sid = wsList[n - 1];
        sdistance = distance;
        if sdistance >= 0:
            print("Num ", sid + 1, " sensor is working properly")
        else:
            print("Num ", sid + 1, " sensor is not connected")
        if n >= count:
            n = 1
        else:
            n = n + 1


if __name__ == '__main__':
    connection(port)
    sens1 = SerialUltra(serialPort, 5, 1)
    print(sens1.read())
    for i in range(5):
        print(sens1.read())
        time.sleep(0.5)
    serialPortClose()
