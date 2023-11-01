import os
from pathlib import Path

from src import utils
from dotenv import load_dotenv
import utils

load_dotenv()

api_hh = os.getenv("HH_URL")
url_superJob = os.getenv("SUPER_URL")
api_key_superJob = os.getenv("KEY_SUPER")

way_json = Path(__file__).parent.parent.joinpath("data").joinpath("save_vacancy.json")

if __name__ == '__main__':
    res = utils.interaction_with_user(api_hh, way_json, url_superJob, api_key_superJob)



