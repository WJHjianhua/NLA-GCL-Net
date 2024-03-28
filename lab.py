import numpy as np
import laspy
import os
import open3d as o3d

ascii_files = {
    'birmingham_block_2.ply': 'birmingham_block_2',
    'birmingham_block_8.ply': 'birmingham_block_8',
    'cambridge_block_15.ply': 'cambridge_block_15',
    'cambridge_block_16.ply': 'cambridge_block_16',
    'cambridge_block_22.ply': 'cambridge_block_22',
    'cambridge_block_27.ply': 'cambridge_block_27'
}
# 原始点云文件
test_file_dir = "/media/wjh/SATA1/Desktop/SensatUrban-master/data/Dataset/SensatUrban/original_block_ply"
# 测试结果labels文件
test_label_dir = "/media/wjh/SATA1/Desktop/lianggemokuai"
# 结果存放位置
stack_file_dir = "/media/wjh/SATA1/Desktop/lianggemokuai/jieguo"

for txt_file_name in ascii_files:
    txt_file = os.path.join(test_file_dir, txt_file_name)
    # test_label = os.path.join(test_label_dir, ascii_files[txt_file_name] + ".label")
    # stack_file = os.path.join(stack_file_dir, ascii_files[txt_file_name] + ".las")
    pcd = o3d.io.read_point_cloud(txt_file)
    # point_cloud = np.loadtxt(txt_file)
    point_cloud = np.asarray(np.hstack((pcd.points, pcd.colors)))
    # print(point_cloud.shape)
    # label = np.loadtxt(test_label)
    # label = np.fromfile(test_label, dtype=np.uint8)
    # print(label.shape)

    data_all = np.hstack([point_cloud])

    las = laspy.create(file_version="1.2", point_format=3)
    las.x = data_all[:, 0]
    las.y = data_all[:, 1]
    las.z = data_all[:, 2]
    las.red = data_all[:, 4]
    las.green = data_all[:, 5]
    las.blue = data_all[:, 6]
    las.clas = data_all[:, 7]

    print(las.clas)

    # las.raw_classification = data_all[:, -1]
    # las.write(stack_file)

