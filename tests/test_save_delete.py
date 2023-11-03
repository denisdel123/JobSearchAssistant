from pathlib import Path

import pytest
from src.data_storage import WorkWithJson

way_json = Path(__file__).parent.parent.joinpath("data").joinpath("save_vacancy.json")


@pytest.fixture()
def class_del_and_save():
    return WorkWithJson(way_json)


def test_save(class_del_and_save):
    file = {"salaryFrom": '23000',
            "salaryTo": '48000',
            "currency": 'RUB',
            "salaryBool": True,
            "snippet": "python",
            "alternate_url": 'https',
            "name": 'python developer'}

    assert class_del_and_save.save_in_list(file, "superJob") == None


def test_delete(class_del_and_save):
    assert class_del_and_save.delete_from_list_all() == None


def test_delete_from_list_item(class_del_and_save):
    assert class_del_and_save.delete_from_list_item(1, 'superJob')
