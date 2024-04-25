import pytest
import func
import json


@pytest.fixture
def operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]


def test_latests_operations():
    data = func.latests_operations("../operation.json", "date", 1)
    assert data == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                     'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                     'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]


def test_nide_characters(operations):
    number_1 = operations[1]["from"]
    number_2 = operations[1]["to"]
    assert func.nide_characters(number_1, "from") == "MasterCard 7158 30** **** 6758"
    assert func.nide_characters(number_2, "to") == "Счет ** 5560"

