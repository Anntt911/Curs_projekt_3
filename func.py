from datetime import datetime
import json


def latests_operations(file_json, soft_param, num_op=5) -> list:
    '''
    returna list of the specified number of dictionaries from a ist of dictionaries sorted by value
    :param file_json: json file with
    :param soft_param: str: sort by value with key
    :param num_op: int: number of returned dictionaries
    :return: list dicts sorted list by parameter < num_op:> will return the last by parameter <num_op>
    '''
    with open(file=file_json, mode="r", encoding='UTF-8') as file:
        data = json.load(file)
        data = [elem for elem in data if "state" in elem and elem["state"] == "EXECUTED"]
        return (sorted(data, key=lambda x: x[soft_param], reverse=True))[:num_op]


def    print_operations(data: list):
    '''
    prints the specified list of dictionaries sorted by value
    :param data: list: list of dictionaries
    :return: prints
    '''
    number_from = ''
    number_to = ''
    if data.get("from"):
        number_from = nide_characters(data.get('from'), tp= 'from')
    if data.get("to"):
        number_to = nide_characters(data.get('to'), tp= 'to')
    date_obj = datetime.strptime(data.get('date').split('T')[0], "%Y-%m-%d")
    date = date_obj.strftime("%d.%m.%Y")

   # def prt(key):
        # return get_val(data, key)

    return (f"{date} {data.get('description')}\n"
            f"{number_from} -> {number_to}\n"
            f"{data["operationAmount"]["amount"]} {data["operationAmount"]["currency"]["code"]}\n")


def get_al(data, keys) -> str:
    '''
    searching for a dictionary by key
    :param data: list: list of dictionaries
    :param keys: str: key to search
    :return: value:
    '''
    val = data.get(keys)
    if val is not None:
        return val
    else:
        for daa in data.values():
            if isinstance(data, dict):
                # val = get_val(data, keys)
                if val is not None:
                    return val
                else:
                    return ''


def nide_characters(data, tp):
    '''
    masking the meaning
    :param data: str: string to be mined
    :param tp: str: sort key
    :return: str: misc value
    '''
    if data == '':
        return ''
    val_num = data.rsplit(' ', 1)
    val = val_num[0: len(val_num) - 1]
    num = val_num[-1]
    if tp == 'from':
        num_hide = num[0:-12] + ' ' + num[-12:-10] + '** **** ' + num[-4:]
    elif tp == 'to':
        num_hide = num[0:-20] + '** ' + num[-4:]
    return ' '.join([*val, num_hide])
