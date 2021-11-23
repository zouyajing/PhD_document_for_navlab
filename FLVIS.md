## FLVIS

FLVIS is a stereo-inertial pose estimation system. It supports four modes: 
1. stereo camera;
2. RGB-D camera;
3. IMU + stereo camera; 
4. IMU + RGB-D camera. 

For RGB-D cameras, the latest version only supports depth image encoded by unsigned int. For example, if you are using a intel realsense camera or a Kinect-v2, you can directly use it. If you are using Kinect DK or other openni-related sensor, please transfer your images from float to unsigned int first.

### 1. Build and run

The content about building and running FLVIS can be referred to [FLVIS](https://github.com/HKPolyU-UAV/FLVIS).

### 2. Details of FLVIS 

The design of FLVIS packages is shown below.

![FLVIS](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/FLVIS_code.png)
* 3rdPartLib. It contains the dependeces of FLVIS beyonds ROS and OpenCV, including:  
  * DBoW3 for loop closure detection.
  * Eigen for matrix computation.
  * g2o fornon-linear optimization. 
  * Sophus for SE3 and se3 transformation.
  * yaml-cpp for config file reading. 
* bag. You can put your testing bags in the bag folder.
* launch. It contains launch files and yaml files for different sensors and datasets.
  * flvis_bag. The launch file for processing a roabag recording the IMU, left IR and depth messages from a D435i camera.
  * flvis_d435i_depth. The launch file for tracking with a D435i camera, which uses IMU, left IR and depth messages.
  * flvis_d435i_stereo. The launch file for tracking with a D435i camera, which uses IMU, left and right IR messages.
  * flvis_d435_pixhawk_depth. The launch file for tracking with a D435 camera and pixhawk. It use the IMU message from pixehawk to replace that inside D435i.
  * flvis_kitti. The launch file for kitti stereo dataset.
  * flvis_euroc_mav. The launch file for euroc dataset, which contains IMU, left and right grey messages.
  * rep_rec. The launch file for publishing the groundtruth from VICON, and the trajectory from FLVIS.
  * rviz. The launch file for Rviz.
  * d435_pixhawk. It contains the launch file and config file for openning D435 camera and pixhawk.
  * d435i. It contains the launch file and config file for openning D435i camera.
  * EuRoc_MAV. The config for euroc mav dataset.
  * KITTI. The config for KITTI dataset.
  * ss_ipad. It will be introduced in other project. [Reconstruction_demo](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/Reconstruction_demo.md)
* msg. It contains two slef-defined messages:
  * CorrectionInf.msg. It is published by the local mapping node, which informs the update KF and map points.
  * KeyFrame.msg. It is published by the tracking node, which contains the images, 2D and 3D points on a keyframe.
* results. In genreal, you can output the camera pose or 3D models here.
* rviz. The config file for Rviz.
* src. The implementation of FLVIS is here.
  * backend.
    * vo_localmap.cpp. The interface for local mapping node.
    * vo_loopclosing.cpp. The interface for loop closing node.
  * frontend.
    * vo_tracking.cpp. The interface for tracking node.
  * independ_moduls.
    * vo_repub_rec.cpp. The node to publish and save the camera poses.
    * kitti_publisher.cpp. The node to publish image messages from KITTI.
* voc. The ORB vocabulary for DBoW3.
* CMakeLists. The CMake File for the FLVIS package.

### 3. An example launch file

Use flvis_d435i_depth.launch as an example to explain the usage of FLVIS.

* <include file="$(find flvis)/launch/d435i/d435i_depth.launch"/> include the launch file for D435i driver.
* /yamlconfigfile is the config file for FLVIS. Please modify line 8-19 according to your sensor.
* /voc is the vocabulary file.
* TrackingNodeletClass_loader is to open the tracking node.
  * /vo/input_image_0. Please remap to your IR or RGB image topic.
  * /vo/input_image_1. Please remap to your depth image topic.
  * /imu. Please remap to your IMU image topic.
* LocalMapNodeletClass_loader is to open the local mapping node.
* LoopClosingNodeletClass_loader is to open the loop closing node.


