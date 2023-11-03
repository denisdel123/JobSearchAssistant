import os
from pathlib import Path

from src import utils
from dotenv import load_dotenv
import utils

load_dotenv()

api_hh = os.getenv("HH_URL")
url_superJob = os.getenv("SUPER_URL")
header = os.getenv("KEY_SUPER")

way_json = Path(__file__).parent.parent.joinpath("data").joinpath("save_vacancy.json")

if __name__ == '__main__':
    print(f"Привет! Я помогу найти работу.\n")

    while True:

        print("0 выйти из программы\n1 показать сохраненные вакансии\n2 найти вакансии\n3 сортировать вакансии\n4 \
удалить вакансии по ID\n5 очистить список")
        try:
            user_opt = int(input(": "))

            if user_opt == 0:
                break

            elif user_opt == 1:

                vacancy = utils.look_list_vacancy(way_json)

            elif user_opt == 2:

                b = 0
                while b == 0:

                    print("На каком сайте будем искать работу?\n0 выйти в главное меню\n\
1 hh.ru\n2 superJob\n3 оба сайта\nвведите число.")
                    try:
                        number = int(input(': '))

                        if number != 0:

                            print('в каком городе искать?')
                            city = input(": ")

                            print('напишите ключевое слово для поиска:')
                            word = input(': ')

                            if number == 1:

                                hh_obj = utils.interaction_with_hh(word, city, api_hh, way_json)
                                b += 1

                            elif number == 2:

                                super_obj = utils.interaction_with_super(word, city, way_json, url_superJob, header)
                                b += 1

                            elif number == 3:

                                print('работаем с вакансиями hh.ru')
                                hh_obj = utils.interaction_with_hh(word, city, api_hh, way_json)

                                print('Работаем с вакансиями superJob')
                                super_obj = utils.interaction_with_super(word, city, way_json, url_superJob, header)
                                b += 1

                            else:
                                print('нет такого варианта')

                        else:
                            break

                    except ValueError:
                        print(f'не корректный ввод {ValueError} попробуйте снова\n')

            elif user_opt == 3:

                c = 0
                while c == 0:
                    try:

                        print("сортировать\n0 выйти в главное меню\n1 по зарплате\n2 по дате ")
                        option_sort = int(input(': '))

                        if option_sort == 0:
                            break

                        elif option_sort == 1:

                            utils.sort_vacancy_salary(way_json)
                            c += 1

                        elif option_sort == 2:

                            utils.sort_vacancy_date(way_json)
                            c += 1
                    except ValueError:
                        print(f'не корректный ввод {ValueError} попробуйте снова\n')

            elif user_opt == 4:
                d = 0
                while d == 0:

                    try:
                        print('на какой платформе удалить?\n0 выйти в главное меню\n1 hh.ru\n2 superJob')
                        plat = int(input(': '))
                        if plat != 0:

                            print('введите id')
                            id_item = int(input(': '))

                            if plat == 1:
                                utils.delete_id(way_json, id_item, 'hh')

                            elif plat == 2:
                                utils.delete_id(way_json, id_item, 'superJob')
                        else:
                            break

                    except ValueError:
                        print(f'не корректный ввод {ValueError} попробуйте снова\n')

            elif user_opt == 5:
                i = 0
                while i == 0:

                    print("вы уверены?\n0 выйти в главное меню\n1 yes")
                    try:

                        option_user = int(input(': '))

                        if option_user != 0:
                            utils.delete_all(way_json)

                        elif option_user == 0:
                            break

                        else:
                            print('не корректный ввод')

                    except ValueError:
                        print(f'не корректный ввод {ValueError} попробуйте снова\n')

        except ValueError:
            print(f'не корректный ввод {ValueError} попробуйте снова\n')
