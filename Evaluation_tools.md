## Evaluation_tools

It includes the tools I used to evaluate the localization and mapping accuracy.

### 1. Localization

As to evalute the localization accuracy, we must prepare two trjectory files first. I usually adopt TUM format `t x y z qx qy qz qw`.

Then you can use [evo](https://github.com/MichaelGrupp/evo) or [TUM tools](https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation) for comparasion.
```
evo_ape tum ground_truth.txt trajectory.txt  -va --plot --plot_mode xy --save_results results/slam
python evaluate_ate.py --save_associations ground_truth.txt trajectory.txt 
```
If you want to compare the accuracies of mutiple SLAM systems, you can use the association files saved by evaluate_ate.py.

### 2. Mapping

The groundtruth of the 3D model of a corridor is built by a high-quality mobile mapping system. 

The 3D model of your SLAM system can be built by 
```
python generate_registered_pointcloud.py rgb.txt depth.txt trajectory.txt tunnel.ply --nth --downsample 5
```
where rgb.txt depth.txt and trajectory.txt stores the rgb file paths, the depth file paths and the camera poses, respectively, and tunnel.ply is your reconstruction result.

The steps to use CloudCompare is listed below:
* Open groundtruth.ply and tunnel.ply using Clou

* Select groundtruth.ply and tunnel.ply and selct tools->registration->fine registration(ICP). 

  Use groundtruth.ply as the reference, then tunnel.ply will be aligned to it by ICP.

* Compute the point-to-point distance by selecting tools->distances->Cloud/Cloud Dist.
* Select groundtruth.ply and tunnel.ply, and select file->save. `exa_000001.txt` is the comparasion result you want.


