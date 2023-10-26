# Standard Library
import math
from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple

# Third Party Library
import open3d as o3d
from plyfile import PlyData


def read_ply_file(filepath: str) -> List[Tuple[float, float, float]]:
    vertices: List[Tuple[float, float, float]] = []
    plydata = PlyData.read(filepath)
    for vertex in plydata["vertex"]:
        x, y, z = vertex["x"], vertex["y"], vertex["z"]
        vertices.append((x, y, z))
    return vertices


def create_histogram(
    vertices: List[Tuple[float, float, float]], bin_size: float
) -> Tuple[
    DefaultDict[Tuple[int, int], int], DefaultDict[Tuple[int, int], int]
]:
    histogram_xz: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    histogram_yz: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    for x, y, z in vertices:
        binned_x = math.floor(x / bin_size)
        binned_y = math.floor(y / bin_size)
        binned_z = math.floor(z / bin_size)
        histogram_xz[(binned_x, binned_z)] += 1
        histogram_yz[(binned_y, binned_z)] += 1
    return histogram_xz, histogram_yz


def threshold_histogram(
    histogram: Dict[Tuple[int, int], int], threshold: int
) -> Dict[Tuple[int, int], int]:
    return {k: v for k, v in histogram.items() if v > threshold}


def generate_points(
    histogram_xz: Dict[Tuple[int, int], int],
    histogram_yz: Dict[Tuple[int, int], int],
) -> List[Tuple[int, int, int]]:
    new_vertices: List[Tuple[int, int, int]] = []

    for (x, z), count in histogram_xz.items():
        for _ in range(count):
            new_vertices.append((x, 0, z))  # y-coordinate is set to 0

    for (y, z), count in histogram_yz.items():
        for _ in range(count):
            new_vertices.append((0, y, z))  # x-coordinate is set to 0

    return new_vertices


def voxelize_point_cloud(
    pcd: o3d.geometry.PointCloud, voxel_size: float, save_dir: str
) -> o3d.geometry.VoxelGrid:
    # ポイントクラウドをボクセルグリッドに変換
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(
        pcd, voxel_size=voxel_size
    )
    o3d.io.write_voxel_grid(f"{save_dir}/voxel.ply", voxel_grid)
    # 新しいファイルにボクセルグリッドを保存
    return voxel_grid  # 必要に応じてボクセルグリッドを返すか、他の操作を行う


def process_point_cloud(
    ply_file_path: str,
    threshold: int,
    bin_size: float,
    voxel_size: int,
    save_dir: str,
) -> None:
    vertices = read_ply_file(ply_file_path)
    histogram_xz, histogram_yz = create_histogram(vertices, bin_size)
    thresholded_histogram_xz = threshold_histogram(histogram_xz, threshold)
    thresholded_histogram_yz = threshold_histogram(histogram_yz, threshold)
    new_vertices = generate_points(
        thresholded_histogram_xz, thresholded_histogram_yz
    )
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(new_vertices)
    o3d.io.write_point_cloud(f"{save_dir}/new_point_cloud.ply", pcd)
    voxelize_point_cloud(pcd, voxel_size, save_dir)
