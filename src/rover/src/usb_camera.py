#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publish_message():
    print("hello world")


if __name__ == "__main__":
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass

