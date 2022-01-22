import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = Path(ROOT_DIR)
parent_path = path.parent
#

def json_check():
    """
    :return: file path
    """

    final_path = None

    for file in os.listdir(parent_path):
        if file == "tasks.json":
            final_path = os.path.join(parent_path, file)

    if final_path:
        return True
    else:
        return False
