# kitti-bin-to-pcd-ply
Converting .bin files of KITTI Velodyne into .pcd/.ply files.

## Convert `.bin` to `.pcd`

```bash
# 1. Only one file
python kitti_bin2pcd.py <path-to-bin-file>, <path-to-pcd-file>
# 2. Folders containing multiple .bin and .pcd
python kitti_bin2pcd_folder.py <path-to-folder-containing-bin-files>, <path-to-folder-containing-pcd-files>
```

## Convert `.bin` to `.ply`

```bash
# 1. Only one file
python kitti_bin2ply.py <path-to-bin-file>, <path-to-ply-file>
# 2. TODO: Folders containing multiple .bin and .ply
```

## Dataset

KITTI, Sementic3D
