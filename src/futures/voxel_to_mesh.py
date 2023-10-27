# Third Party Library
# import aspose.threed as a3d
# Third Party Library
import numpy as np
import open3d as o3d

def point_cloud_to_mesh_and_save_fbx(point_cloud: o3d.geometry.PointCloud) -> None:
    # 点の法線推定
    point_cloud.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(
            radius=0.1, max_nn=30
        )
    )
    print(1)
    # 点の法線の方向一貫性の考慮
    point_cloud.orient_normals_consistent_tangent_plane(
        k=10
    )  # k is the number of nearest neighbors
    print(2)

    # Marching cubesによるメッシュ再構成
    voxel_size = np.mean(point_cloud.compute_nearest_neighbor_distance()) * 0.5  # Adjust voxel size accordingly
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_marching_cubes(
        point_cloud, voxel_size=voxel_size, iso_level=0
    )
    print(3)
    o3d.visualization.draw_geometries([mesh])
    
if __name__ == "__main__":
    point_cloud = o3d.io.read_point_cloud(
        "/home/iplslam/research_point_cloud/python_research_enviroment/data/result/new_point_cloud.ply"
    )
    point_cloud_to_mesh_and_save_fbx(point_cloud)
