## IMU_GNSS_ESKF

It is a loose-coupled system fusing IMU and GNSS data. We can extend it to support cameras easily. 

The building and running of IMU_GNSS_ESKF is referred to [imu_gnss_eskf](https://github.com/zouyajing/imu_gnss_eskf).

The detail of IMU_GNSS_ESKF is shown below:

![ESKF](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/ESKF_.png)

* include.
  * utils.h. It includes the data structure of IMU data, GNSS data and the state, and also the functions to convert between LLA and ENU, and so3 to SO3.
  * eskf.h. It contains the state and noises of the IMU, and also the essential functions: 1. initialize; 2. predict; 3. update.
* src.
  * eskf.cpp. It contains the imprlmentation of the essential functions in eskf.h.
  * imu_gnss_eskf_node.cpp. The interface to fuse IMU and GNSS data.
* launch. The launch file of running IMU_GNSS_ESKF.
* rviz. The config file for Rviz.
* CMakeLists. The CMake File for IMU_GNSS_ESKF.
  
  

