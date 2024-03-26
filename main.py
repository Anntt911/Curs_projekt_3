from func import latests_operations, print_operations

file_json = 'operation.json'


def main(data, num):
    last_opers = latests_operations(data, soft_param= 'date', num_op=num)
    for data in last_opers:
        print(print_operations(data))


if __name__ == '__main__':
    main(file_json, num=5)