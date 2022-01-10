## Evaluation_tools

It includes the tools I used to evaluate the localization and mapping accuracy.

### 1. Localization

As to evalute the localization accuracy, we must prepare two trjectory files first. I usually adopt TUM format `t x y z qx qy qz qw`.

Then you can use [evo](https://github.com/MichaelGrupp/evo) or [TUM tools](https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation) for comparasion.
```
evo_ape tum ground_truth.txt trajectory.txt  -va --plot --plot_mode xy --save_results results/slam
python evaluate_ate.py --save_associations ground_truth.txt trajectory.txt 
```
If you want to compare the accuracies of mutiple SLAM systems, you can use the association files saved by `evaluate_ate.py`.

### 2. Mapping

[groundtruth.ply](https://drive.google.com/file/d/15dDPVI8OuOI7BbBYdWX8hMvWcr0gX1Ls/view?usp=sharing) is the groundtruth model of a corridor built by a high-quality mobile mapping system. 

[tunnel.ply](https://drive.google.com/file/d/14PyJte9iM7PzARfpxeJgWwwecyZUaFOB/view?usp=sharing) is the 3D model built by your SLAM system:
```
python generate_registered_pointcloud.py rgb.txt depth.txt trajectory.txt tunnel.ply --nth 5 --downsample 5
```
where `rgb.txt` `depth.txt` and `trajectory.txt` stores the rgb file paths, the depth file paths and the camera poses, respectively, and tunnel.ply is your reconstruction result. You may download the scripts [here](https://github.com/zouyajing/PhD_document_for_navlab/tree/main/scripts).Please modify `fx, fy, cx, fy and scale` in `generate_registered_pointcloud.py`.

The steps of computing mapping accuracy is then listed below:
* Open groundtruth.ply and tunnel.ply using CloudCompare

  ![open](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/open.png)

* Select groundtruth.ply and tunnel.ply and selct tools->registration->fine registration(ICP). 
  
  ![selct](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/ICP.png)

  Please use groundtruth.ply as the reference, then tunnel.ply will be aligned to it by ICP.

* Compute the point-to-point distance by selecting tools->distances->Cloud/Cloud Dist.

  ![compare](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/compare.png)
  
* Select groundtruth.ply and tunnel.ply, and select file->save. `exa_000001.txt` is the comparasion result you want.
  ![01](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/ex_0001.png)
  ![001](https://github.com/zouyajing/PhD_document_for_navlab/blob/main/imgs/ex_00001.png)
  
  The column 7 in `exa_000001.txt` stores the point-point distance. You may read and show it by MATLAB:
  ```
  ply_slam = txtread('exa_000001.txt');
  xyz_slam = ply_slam(1:end,1:3);
  distance_slam = ply_slam(1:end,7);
  rmse = sqrt((distance_slam).^2);
  pointcloud_show = pointCloud(xyz_slam,'Intensity',distance_slam);
  figure;
  pc_show(pointcloud_show);
  grid_offl
  color_bar;
  caxis([0 0.5]);
  ```


