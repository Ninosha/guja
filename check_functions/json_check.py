import os
from pathlib import Path


# to get the parent working directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = Path(ROOT_DIR)
parent_path = path.parent


def json_check():
    """
    :return: file path
    """
    for file in os.listdir(parent_path):
        if file.endswith(".json"):
            return os.path.join(parent_path, file)
        else:
            continue


