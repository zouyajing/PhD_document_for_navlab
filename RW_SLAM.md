## RW_SLAM
RW_SLAM is a tightly coupled system fusing an RGB-D camera and a wheel odometer. The latest version of RW_SLAM is stored in the robot computer `/rw_slam/src/rw_slam`.

### 1. Dependences and install
RW_SLAM is tested under Ubuntu 16.04 + ROS Kinetic and Ubuntu 18.04 + ROS Melodic. 

You can skip this part if you already install the below libraries in your computer:
* Eigen for matrix computation. `sudo apt-get install libeigen3-dev`
* Sophus for Lie group processing. `cd 3rdpart/Sophus; mkdir build && cd build; cmake ..; make -j; sudo make install `
* OpenCV for image processing. `sudo apt-get install libopencv-dev python-opencv`
* CSparse is a dependece of g2o, which is used for solving HΔx=g. `sudo apt install libsuitesparse-dev`
* g2o for optimization. `cd 3rdpart/g2o; mkdir build && cd build; cmake ..; make -j; sudo make install`
* * PCL for point cloud processing. `sudo apt install libpcl-dev`
* octomap for 3D and 2D mapping. `sudo apt-get install ros-melodic-octomap*`



