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
