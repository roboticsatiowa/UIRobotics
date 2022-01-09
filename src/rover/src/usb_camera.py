#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

def publish_message():
    pub_video = rospy.Publisher('usb_video_frame', CompressedImage, queue_size=10)
    rospy.init_node('usb_camera', anonymous=True)
    rate = rospy.Rate(30) # 30 FPS

    cap = cv2.VideoCapture(0) # 0 -> webcam number
    br = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        
        if ret == True:
            pub_video.publish(br.cv2_to_compressed_imgmsg(frame))
        
        rate.sleep()

if __name__ == "__main__":
    try:
        publish_message()
    except rospy.ROSInterruptException:
        pass

