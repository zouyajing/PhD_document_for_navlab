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
Please modify:
* line 3 in rw_slam_test.launch based on your bag file;
* line 8 based on your config file;
* line 9-11 based on the image and odom topics.

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
  * line 74 is the vocabulary file. ![#Must be modified.](https://via.placeholder.com/15/f03c15/000000?text=+) `#Must be modified.`
  * line 75 is the result folder. Must be modified.![#Must be modified.](https://via.placeholder.com/15/f03c15/000000?text=+) `#Must be modified.`







