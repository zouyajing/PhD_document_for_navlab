## RW_SLAM
RW_SLAM is a tightly coupled system fusing an RGB-D camera and a wheel odometer. 
### 1. Dependences and install
RW_SLAM is tested under Ubuntu 16.04 + ROS Kinetic and Ubuntu 18.04 + ROS Melodic. 

The latest version of RW_SLAM is stored in the robot computer `~/rw_slam/src/rw_slam/`. Paste RW_SLAM to your computer under `~/rw_slam/src/`. Then cd `~/rw_slam/src/rw_slam/` and start to install the dependences:
* Eigen for matrix computation. `sudo apt-get install libeigen3-dev`
* Sophus for Lie group processing. `cd 3rdparty/Sophus/; mkdir build && cd build; cmake ..; make -j; sudo make install `
* OpenCV for image processing. `sudo apt-get install libopencv-dev python-opencv`
* CSparse is a dependece of g2o, which is used for solving HΔx=g. `sudo apt install libsuitesparse-dev`
* g2o for optimization. `cd 3rdparty/g2o/; mkdir build && cd build; cmake ..; make -j; sudo make install`
* PCL for point cloud processing. `sudo apt install libpcl-dev`
* octomap for 3D and 2D mapping. `sudo apt-get install ros-melodic-octomap*`
Go back to the working space and cmake:
```
cd ~/rw_slam/
catkin_make
```
### 2. Run the examples

Two examples are provided: 1. run RW_SLAM with a rosbag; 2. run RW_SLAM on Turtlebot2 + Kinect_DK.

Let's start with the first example:
```
roslaunch rw_slam rviz.launch
roslaunch rw_slam rw_slam_test.launch
```
The second example is about how to employ it on a Turtlebot2.
```
roslaunch rw_slam robot_and_dk.launch      (open the robot and camera driver)
roslaunch rw_slam scan_DK.launch           (convert depth image to 2D laserscan)
roslaunch rw_slam rw_slam_front_DK.launch  (run RW_SLAM)
```

### 3. Details of RW_SLAM
The design of RW_SLAM packages is shown below.

![RW_SLAM](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/RW_SLAM_code.png)

* 3rdparty. It contains some dependeces of RW_SLAM, including:
  * DBoW2.
  * g2o.
  * Sophus.
* config. It contains the config files for RW_SLAM. `rw_slam_dk.yaml` is used for an example:
  * line 2- 7 is the parameters of your RGB-D camera, which includes resolution, instrinsic calibration matrix, distortion parameters, depth scale and frequency.
  * line 28-32 is the 4x4 extrinsic calibration matrix between RGB-D camera and wheel odometer. You can transfer to the rotation matrix from Quaternion or Angle axis or Eular Angle using [rotation converter](https://www.andre-gaschler.com/rotationconverter/).
  * line 39 is the feature number. In general, the increase of the feature number indicates better tracking performance, while the decrease means faster tracking speed.
  * line 74 is the vocabulary file. ![#Must be modified.](https://via.placeholder.com/15/f03c15/000000?text=+) `Must be modified.`
  * line 75 is the result folder. Must be modified.![#Must be modified.](https://via.placeholder.com/15/f03c15/000000?text=+) `Must be modified.`
* launch. It contains the launch files for running RW_SLAM:
  * turtlebot2_demo. It contains the launch files for running RW_SLAM on a Turtlebot2. + Kinect DK or Kinect v2.
  * rviz.launch. The launch file of Rviz.
  * rw_slam_test.launch. The launch file for running RW_SLAM with a rosbag.
    * line 3 is the rosbag play node. ![0](https://via.placeholder.com/15/f03c15/000000?text=+)`Please modify the path based on your bag file.`
    * line 8 is the config file. ![0](https://via.placeholder.com/15/f03c15/000000?text=+)`Please modify the path based on your config file.`
    * line 9-11 are the image and odom topics.![0](https://via.placeholder.com/15/f03c15/000000?text=+)`Please modify the topic names based on your bag info.`
  * result. You may save the keyframe poses, camera poses or robot poses here.
  * rviz. The Rviz config.
  * src. The source code of RW_SLAM. It includes:
    * peac. RGB-D plane detection functions.
    * camera. Camera projection functions.
    * common. Help functions.
    * config. Read the config file.
    * feature_detector. Detector ORB features.
    * frame. It contains the essential parameters and functions on one frame.
    * keyframe. It contains the essential parameters and functions on one keyframe.
    * line_detector. Delect 3D line features.
    * line_g2o_edge. The edge between one line and one camera pose.
    * line_matcher. Match line features by LBD.
    * local mapping. The interface of the local mapping thread.
    * loop closing. The interface of the loop closing thread.
    * lsd_detector. Detect LSD feature.
    * map. The map contains the keyframes, the map points and their relationship, and also relative functions.
    * map_line. It contains the essential parameters and functions of a 3D line.
    * map_plane. It contains the essential parameters and functions of a plane.
    * map_point. It contains the essential parameters and functions of a 3D point.
    * odo_edge. The edge between two camera poses.
    * optimizer. The functions of optimization. (Core)
    * ORBextractor. Copied from ORB_SLAM2.
    * plane_extractor. The interface of plae detection library.
    * plane_g2o_edge. The edge between a camera pose and a plane.
    * plane_g2o_para_edge. The edge between a camera pose, a base plane and its parallel plane.
    * plane_g2o_ver_edge. The edge between a camera pose, a base plane and its vertical plane.
    * plane_matcher. The functions to match a plane.
    * prior_edge. The prior edge for planar motion assumption.
    * ros_puber. The interface for publishing ROS topics.
    * run_time. The functions to count the computation time.
    * rw_slam. The main interface of RW_SLAM, which will start three threads for tracking, local mapping and loop closing.
    * tracking. The interface for the tracking thread.
    * vocabulary. Transfer the descriptors to a word vector.
  * voc. It stores the ORB vocabulary.
  * CMakeLists. The CMake file for RW_SLAM.
    






