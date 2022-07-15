import time

import serial

import serial

if __name__ == '__main__':
    com = serial.Serial("/dev/ttyUSB0", 9600, bytesize=8, parity='N', stopbits=1, timeout=1)
    print(com)
    d = bytes.fromhex('7F 02 12 00 00 00 00 00 03 17')
    # print(success_bytes)


    for i in range(5):
        success_bytes = com.write(d)
        data = com.read(10)
        print(data[1], "号雷达距离为：", data[4] * 0x100 + data[5])  # 距离数据
        time.sleep((0.5))
    com.close()


def analyzeData():
    print(1)