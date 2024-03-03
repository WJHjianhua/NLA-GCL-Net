import pyvista as pv

# 加载点云数据
cloud = pv.PolyData("F:\RandLA-Net-master\data\S3DIS\original_ply\Area_1_conferenceRoom_1.ply")  # 假设点云数据保存在point_cloud.ply文件中

# 显示点云
cloud.plot()