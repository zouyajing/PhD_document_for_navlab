## FLVIS

FLVIS is a stereo-inertial pose estimation system. It supports four modes: 1. stereo camera; 2. RGB-D camera; 3. IMU + stereo camera; 4. IMU + RGB-D camera. For RGB-D cameras, the latest version only supports depth image encoded by unsigned int. For example, if you are using a intel realsense camera or a Kinect-v2, you can directly use it. If you are using Kinect DK or other openni-related sensor, please transfer your images from float to unsigned int first.

### 1. Build and run

The content about building and running FLVIS can be referred to [FLVIS](https://github.com/HKPolyU-UAV/FLVIS).

### 2. Details and comments 

The design of FLVIS packages is shown [](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/FLVIS_code.png)
