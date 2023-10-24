# Standard Library
import os
from dataclasses import dataclass


@dataclass
class VoxelConfig:
    bin_size: float = 0.5
    threshold: int = 10  # Adjust this value based on your requirement
    path: str = os.getcwd() + "/data/raw/_point_cloud.ply"


@dataclass
class ExperimentConfig:
    train: VoxelConfig = VoxelConfig()
    logdir: str = "outputs"
