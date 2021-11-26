## Qualysis

It is about how to use the Qualysis motion capture system in the navlab. It includes: 
* how to locate the camera system; 

  If the IP of your camera system has been changed, you will have the below problem:
  ```
  The interface where a camera system has been located is no long available before.
  Make sure a network cable is connected to the cameras and that they are turned on.
  ```
  Please locate the camera system again. Click Tool->Project Options->Camera System->Locate System.
  
  ![Locate](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/locate.jpeg)
  
* how to calibrate the camera system; 
   
  If the camera locations are changed, you need to calibrate the system. 
  
  Please prepare the calibrate tools and then click the calibrate button:
  
  ![tools](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/tools.png)
  
  Let the left item be static, and move the right one and make it be observed by all the cameras.
  
  ![button](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/calibrate_capture.png)
  
  In the middle of the above pic, the red button is to capture, and the button beside it is to calibrate.
  
* how to define a body frame; 
  
  Stick the reflcetion balls to your sensor or robot. 
  
  Click the capture button, and capture a 1-minite video. 
  
  Select the balls you want to define a body in QTM window, and right click to define.
  
  ![define](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/definebody.jpeg)
  
* how to show the body info; 
  
  Select Vie->Data info 1. You will automatically see the ball locations.
  
  Right click and select 6-Dof, then you will see the body info.
  
  ![Bofy info](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/showdatainfo.png)
* how to save the body trajectory.

  We can use the [motion_capture_driver]((https://github.com/KumarRobotics/motion_capture_system)) provided by Kumar Robotics.
  
  Please modify the line 6 in [qualysis.launch](https://github.com/KumarRobotics/motion_capture_system/blob/master/mocap_qualisys/launch/qualisys.launch).
 
  You can get the server address by ipconfig. `10.11.229.233` is the what you want.
  
  ![IP](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/ip.png)
  
  In general, two computers are needed. The first (Windows) connects to Qualysis, and the second(ROS + Ubuntu) receive te trajectory. They must use the same WIFI.
  
  Though the driver will publish the transformation between the world frame and the body frame, you may save it into a text file.
  
  For example, add two lines in  QualisysDriver.cpp:
   ```
   line 27: std::ofstream f("/home/**/trajectory.txt");
   line 225: f << setprecision(6) << stamped_transform.stamp_.toSec() << setprecision(7) << " " << pos(0) << " " << pos(1) << " " << pos(2)
          << " " << att.x() << " " << att.y() << " " << att.z() << " " << att.w() << endl;
   ```
  
  
