# NLA-GCL-Net: Semantic Segmentation of Large-Scale Surveying Point Clouds Based on Neighborhood Label Aggregation and Global Context Learning
## 1 Dataset
### 1.1 SensatUrban
URL:https://forms.gle/m4HJiqZxnq8rmjc8A

Unzip the downloaded data_release.zip file to ensure that the directory structure is as follows: /....../SensatUrban-master/data/Dataset/SensatUrban/data_release/. Please ensure that the "train" and "test" folders under data_release/ remain unchanged. When obtaining the project, if the data/Dataset/SensatUrban/ directory does not exist, it will need to be created manually or using a command.

### 1.2 S3DIS
URL:http://buildingparser.stanford.edu/dataset.html

Download the files named "Stanford3dDataset_v1.2_Aligned_Version.zip". Uncompress the folder and move it to /data/S3DIS.

## 2 Data preprocessing
### 2.1 SensatUrban
```
python input_preparation.py --dataset_path $YOURPATH
cd $YOURPATH; 
cd ../; mkdir original_block_ply; mv data_release/train/* original_block_ply; mv data_release/test/* original_block_ply;
mv data_release/grid* ./
```

### 2.2 S3DIS
```
python utils/data_prepare_s3dis.py
```

## 3 Train
### 3.1 SensatUrban
```
python main_SensatUrban.py --mode train --gpu 0
```
### 3.2 S3DIS
```
python main_S3DIS.py --gpu 0 --mode train --test_area 5
```
## 4 Test
### 4.1 SensatUrban
```
python main_SensatUrban.py --mode test --gpu 0
```
### 4.2 S3DIS
```
python main_S3DIS.py --gpu 0 --mode test --test_area 5
```
## 5 Qualitative results of our NLA-GCL-Net:

![Fig 7](https://github.com/WJHjianhua/NLA-GCL-Net/assets/162021896/17cbb30b-5570-4dee-8b69-39503207ce6a)

![FIGs3dis](https://github.com/WJHjianhua/NLA-GCL-Net/assets/162021896/30eec87d-c66f-4588-9342-cf5877b65255)

