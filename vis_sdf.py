import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from mesh_to_sdf import get_surface_point_cloud,scale_to_unit_cube, scale_to_unit_sphere, BadMeshException, sample_sdf_near_surface

def vis_sdf(data):
    # 获取xyz坐标和sdf值
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    sdf_values = data[:, 3]

    threshold = 1

    x = x[sdf_values<threshold]
    y = y[sdf_values<threshold]
    z = z[sdf_values<threshold]

    sdf_values = sdf_values[sdf_values<threshold]

    # 创建一个新的3D图形
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)
    ax2.hist(sdf_values)

    # 使用SDF值作为颜色映射
    scatter = ax.scatter(x, y, z, c=sdf_values, cmap='viridis')
    plt.colorbar(scatter, ax=ax, label='SDF Value')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.title('SDF Visualization')
    plt.show()

if __name__ == "__main__":
    raw = np.load("data/SdfSamples/ShapeNetV2/04256520/1a04dcce7027357ab540cc4083acfa57.npz")
    data = raw['pos']
    vis_sdf(data)

