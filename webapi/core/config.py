from dynaconf import Dynaconf
import os

base_dir_path = "/".join(os.path.abspath(__file__).split("/")[0:-3])

settings = Dynaconf(
    settings_files=[f"{base_dir_path}/configs/config.yaml"],
)
