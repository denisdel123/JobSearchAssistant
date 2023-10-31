import os

from getting_data import WorkWithPlatforms
from dotenv import load_dotenv
import utils

load_dotenv()
api_hh = os.getenv("HH_URL")
url_superJob = os.getenv("SUPER_URL")
api_key_superJob = os.getenv("KEY_SUPER")

if __name__ == '__main__':
    check = WorkWithPlatforms.get_vacancies_hh('python', api_hh)
    for i in check:
        print(i)
        print()
