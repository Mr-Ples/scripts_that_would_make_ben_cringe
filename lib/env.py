import os
from pathlib import Path
from dotenv import load_dotenv


REPO_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = os.path.join(REPO_PATH, 'data')
ENV_PATH = os.path.join(REPO_PATH, '.env')
load_dotenv(ENV_PATH)

# print("REPO_PATH=", REPO_PATH)
# print("DATA_PATH=", DATA_PATH)
