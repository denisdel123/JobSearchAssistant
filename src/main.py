import os

from classes import PlatformHH
from dotenv import load_dotenv

load_dotenv()
api_hh = os.getenv("HH_URL")
api_superJob = os.getenv("SUPER_URL")

if __name__ == '__main__':
    ex = PlatformHH(api_hh)
    ex.get_vacancies("python")
