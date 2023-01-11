import os
from pathlib import Path


REPO_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = os.path.join(REPO_PATH, 'data')
# print("REPO_PATH=", REPO_PATH)
# print("DATA_PATH=", DATA_PATH)
