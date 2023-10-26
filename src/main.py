# Standard Library
import logging
import os
import time

# Third Party Library
import yaml

# First Party Library
from config import config
from futures import histogram_point_generator


def run(configs: config.Config = None, save_dir: str = "") -> None:
    histogram_point_generator.process_point_cloud(
        configs.path,
        configs.threshold,
        configs.bin_size,
        configs.voxel_size,
        save_dir,
    )
    return


def main() -> None:
    path = os.getcwd()
    config_path = path + "/src/config/config.yml"

    with open(config_path, "r") as yf:
        yaml_data = yaml.safe_load(yf)
    try:
        configs_value = config.get_config(config_path)
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
    except ValueError as e:
        print(f"Invalid configuration: {e}")

    time_str = time.strftime("%Y-%m-%dT%H-%M-%S")

    logdir = f"{path}/data/result/{time_str}"
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    config_save_path = f"{logdir}/config.yaml"
    with open(config_save_path, "w") as yf:
        yaml.dump(
            yaml_data,
            yf,
            default_flow_style=False,
        )
    run(configs_value, logdir)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
