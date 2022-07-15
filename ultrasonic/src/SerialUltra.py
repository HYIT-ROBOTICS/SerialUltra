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
import time


class SerialUltra:
    last = 0
    serialPort = ""
    tr = 0
    id = 0

    def __init__(self, con, t, i):
        self.serialPort = con
        self.tr = t
        self.id = i
        return

    def read1(self, sendstr):
        line = {}
        i = 1
        l = 0
        d = bytes.fromhex(sendstr)
        while True:
            try:
                self.serialPort.write(d)
                data = self.serialPort.read(10)
                time.sleep(0.1)
                line1 = data[4] * 0x100 + data[5]
                if line1 == 8015:
                    line1 = 0

                    #return line1
                # self.tr = int(self.tr * line1 / 100)
                # while i > 0 and i < 3:
                #     self.serialPort.write(d)
                #     data = self.serialPort.read(10)
                #     time.sleep(0.1)
                #     line[i] = data[4] * 0x100 + data[5]
                #     if (abs(line[1] - line[i]) < self.tr):
                #         # print (i," : ", line[i])
                #         l = l + line[i]
                #         i += 1
                return line1 #int((l + line1) / 3)
            except serial.serialutil.SerialException:
                print(self.serialPort, "   Connection is not available")
        return 0

    def read_sensor_1(self):
        return self.read1('7F 01 12 00 00 00 00 00 03 16')

    def read_sensor_2(self):
        return self.read1('7F 02 12 00 00 00 00 00 03 17')

    def read_sensor_3(self):
        return self.read1('7F 03 12 00 00 00 00 00 03 18')

    def read_sensor_4(self):
        return self.read1('7F 04 12 00 00 00 00 00 03 19')

    def read_sensor_5(self):
        return self.read1('7F 05 12 00 00 00 00 00 03 1A')

    def read_sensor_6(self):
        return self.read1('7F 06 12 00 00 00 00 00 03 1B')

    def read_sensor_7(self):
        return self.read1('7F 07 12 00 00 00 00 00 03 1C')

    def read_sensor_8(self):
        return self.read1('7F 08 12 00 00 00 00 00 03 1D')

    def read(self):
        num = self.id
        if num == 1:
            return self.read_sensor_1()
        if num == 2:
            return self.read_sensor_2()
        if num == 3:
            return self.read_sensor_3()
        if num == 4:
            return self.read_sensor_4()
        if num == 5:
            return self.read_sensor_5()
        if num == 6:
            return self.read_sensor_6()
        if num == 7:
            return self.read_sensor_7()
        if num == 8:
            return self.read_sensor_8()


