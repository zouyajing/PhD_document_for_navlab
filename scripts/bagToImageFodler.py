# coding:utf-8
#!/usr/bin/python

# Extract images from a bag file.

#PKG = 'beginner_tutorials'
import roslib;   #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
cvb=CvBridge()
i=0
depth_mem=None
first_flag=True

# Reading bag filename from command line or roslaunch parameter.
#import os
#import sys

rgb_path = 'rgb/'
depth_path= 'depth/'
rgb_txt = open('rgb.txt','w')
depth_txt = open('depth.txt','w')
odom_txt = open('odom.txt','w')

def imnormalize(xmax,image):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : image:image data.
    : return: Numpy array of normalize data
    """
    xmin = 0
    a = 0
    b = 255
    
    return (np.array(image,dtype=np.float32)*1000)
class ImageCreator():


    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('2021-01-13-01-32-40.bag', 'r') as bag:  #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == "/kinect2/qhd/image_color": #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        print timestr
                        image_name = timestr+ ".png" #图像命名：时间戳.png
                        cv2.imwrite(rgb_path + image_name, cv_image)  #保存；
                        rgb_txt.write(timestr+" "+rgb_path+image_name)
                        rgb_txt.write('\n')
                elif topic == "/kinect2/qhd/image_depth_rect": #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"16UC1")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        print timestr
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".png" #图像命名：时间戳.png
                        cv2.imwrite(depth_path + image_name, cv_image)  #保存；
                        depth_txt.write(timestr+" "+depth_path+image_name)
                        depth_txt.write('\n')
                elif topic == "/odom": #ground truth的topic；
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        print timestr
                        x = "%.6f" % msg.pose.pose.position.x
                        y = "%.6f" % msg.pose.pose.position.y
                        z = "%.6f" % msg.pose.pose.position.z
                        qx = "%.6f" % msg.pose.pose.orientation.x
                        qy = "%.6f" % msg.pose.pose.orientation.y
                        qz = "%.6f" % msg.pose.pose.orientation.z
                        qw = "%.6f" % msg.pose.pose.orientation.w
                        odom_txt.write(timestr+" "+x+" "+y+" "+z+" "+qx+" "+qy+" "+qz+" "+qw)
                        odom_txt.write('\n')
        rgb_txt.close()
        depth_txt.close()
        odom_txt.close()

if __name__ == '__main__':

    #rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
