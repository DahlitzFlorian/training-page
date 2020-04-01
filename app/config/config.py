from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).parent / "social_media.yml"


def get_social_media_info() -> dict:
    with open(CONFIG_PATH) as config_file:
        social_media_config = yaml.safe_load(config_file)

    return social_media_config
