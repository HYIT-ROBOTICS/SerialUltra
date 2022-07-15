#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
from ultrasonic_topic.msg import Sensor
import serial
import serial.tools.list_ports as port_list
from connectultra import *
from getSensorConfig import *


def velocity_publisher():
    # ROS节点初始化
    rospy.init_node('sensor_publisher', anonymous=True)

    # 创建一个Publisher，发布名为/person_info的topic，消息类型为learning_topic::Person，队列长度10
    sensor_info_pub = rospy.Publisher('/sensor_info', Sensor, queue_size=10)

    # 设置循环的频率
    rate = rospy.Rate(2000)
    count = getWorkingSensorCount()  # working sensor count
    wsList = getWorkingSensorIdList()  # working sensor id list
    n = 1
    serialPortOpen()
    testSensorState()
    while not rospy.is_shutdown():
        # 初始化learning_topic::Person类型的消息
        list=[]
        for i in range(count):
            sensor_msg = Sensor()
            distance = readtest(wsList[n-1])
            sensor_msg.id = wsList[n-1];
            sensor_msg.distance = distance;
            list.append(sensor_msg)
            if n >= count:
                n = 1
            else:
                n = n + 1

        # 发布消息
        sensor_info_pub.publish(list[0], list[1])
        rospy.loginfo("Publish sensor message[%d, %d][%d, %d][%d, %d][%d, %d][%d, %d][%d, %d][%d, %d][%d, %d][%d, %d]",
                      list[0].id, list[0].distance,
                      list[1].id, list[1].distance,
                      list[2].id, list[2].distance,
                      list[3].id, list[3].distance,
                      list[4].id, list[4].distance,
                      list[5].id, list[5].distance,
                      list[6].id, list[6].distance,
                      list[7].id, list[7].distance,
                      list[8].id, list[8].distance
                      )

        # if n >= count:
        #     n = 1
        # else:
        #     n = n + 1

        # 按照循环频率延时
        rate.sleep()


if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass
    serialPortClose()
