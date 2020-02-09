import pytest
from CrudBear.BearAPI import *

api = BearApi()

@pytest.fixture(scope='function')
def delete_bears():
    api.delete_all_bears()
    yield


class TestClass:

    @pytest.mark.usefixtures("delete_bears")
    @pytest.mark.parametrize("bear_type, bear_name, bear_age", [
        ("BROWN", "BILLY", 1),
        ("GUMMY", "WILLY", 5),
        ("BLACK", "LEON", 100),
        ("POLAR", "SLAYER", 0)

    ])
    def test_create_new_bear(self, bear_type, bear_name, bear_age):
        """

        :param bear_type: Вид медведя
        :param bear_name: Имя медведя
        :param bear_age: Возраст медведя (0-100)
        :return:

        Параметризированный тест проверяющий все виды медведей и их возраст от 0 до 100
        """
        bear_id = api.create_bear(bear_type, bear_name, bear_age)
        etalon_bear = CreateJson.bear_etalon_json(bear_id, bear_type, bear_name, bear_age)
        bear_created = api.get_bear_by_id(bear_id).json()
        assert etalon_bear == bear_created


    @pytest.mark.usefixtures("delete_bears")
    @pytest.mark.parametrize("bear_type, bear_name, bear_age", [
        ("", "BILLY", 1),
        ("BRWN", "WILLY", 5),
        ("BLACK", "", 100),
        ("POLAR", "SLAYER", -1),
        ("BLACK", "SILVER", 101),
        ("BROWN", "KENNY", "")


    ])
    def test_create_bear_negative(self, bear_type, bear_name, bear_age):
        """

        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        Параметриизированные негативные тесты. Неправильный вид медведя,
        отсуствие вида медведя, отсутсвие имени, возраст меньше 0, возраст больше 100, без возраста
        """
        response = api.create_bear(bear_type, bear_name, bear_age)
        assert response.status_code == 500

    @pytest.mark.usefixtures("delete_bears")
    def test_update_bear(self):
        """
        Проверка апдейта медведя
        :return:
        """
        bear1 = api.create_bear("BLACK", "BERNY", 5)
        etalon_bear = CreateJson.bear_etalon_json(bear1, "BLACK", "BERNY", 5)
        api.update_bear_by_id(bear1, "BROWN", "HOLMS", 10)
        response = api.get_bear_by_id(bear1)
        assert response.json() == etalon_bear

    @pytest.mark.usefixtures("delete_bears")
    def test_delete_bear(self):
        """
        проверка удаления медведя
        :return:
        """
        bear1 = api.create_bear("POLAR", "TOR", 10)
        api.delete_bear_by_id(bear1)
        response = api.get_bear_by_id(bear1)
        assert response.text == "EMPTY"

    @pytest.mark.usefixtures("delete_bears")
    def test_check_all_bears(self):
        """
        Проверка всех медведей на сервере
        :return:
        """
        allBears = api.create_list_of_4_bears()
        allBearsFromServer = api.get_all_bears(allBears)
        assert allBears == allBearsFromServer









