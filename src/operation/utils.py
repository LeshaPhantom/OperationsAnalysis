import os
from src.operation.schemas import key

def format_lst_contents(content: list):
    """ Получаем content с типом list. После перебираем каждую строчку.
    """
    #   Проверка на List
    if not isinstance(content, list):  # Проверка на тип
        raise TypeError("Неверный type у content переданный в  format_lst_contents()")

    lst = list()
    for i in content:
        lst.append(format_lst_len(i))
    return lst


def format_lst_len(content: str):
    """ Получаем content с типом str. После перебираем каждый символ в строчке.
    """
    #   Проверка на str
    if not isinstance(content, str):
        raise TypeError("Неверный type у content переданный в format_lst_len() ")
    active = False
    line = str()
    lst = list()
    for i in content:
        if i == '"':
            active = not active
            continue
        if i != ';':
            line = line + i
        else:
            lst.append(line)
            line = str()
    lst.append(line[:-1])
    return format_dict(lst)


def format_dict(lst: list):
    """ Получаем lst с типом list. Для создания словаря из списка
    """
    result = dict(zip(key, lst))

    # редактирование даты в формат 06-09-2023 11:20:02
    result['data_time_operation'] = refactoring_data(result['data_time_operation'])
    result['data_payment'] = refactoring_data(result['data_payment'])

    # Редактирование статус операции. Приходит 'OK' или 'FAILED'
    if result['status_operation'] == 'FAILED':
        result['status_operation'] = False
    else:
        result['status_operation'] = True

    # Редактирование переменных имеющие числовое значение.
    result['sum_operation'] = result['sum_operation'].replace(",", ".")
    result['sum_payment'] = result['sum_payment'].replace(",", ".")
    result['bonus_cashback'] = result['bonus_cashback'].replace(",", ".")
    result['rounding_invest'] = result['rounding_invest'].replace(",", ".")
    result['rounding_operation'] = result['rounding_operation'].replace(",", ".")
    return result

def refactoring_data(data_time):
    """ Преобразуем '03.09.2023 07:35:19' в '2023-09-03 07:35:19' для модуля datetime
    """
    data_time = data_time.replace(".", "-")
    data_time = data_time.split(' ')
    data_time[0] = data_time[0].split('-')
    data_time[0].reverse()
    data_time[0] = '-'.join(data_time[0])

    return ' '.join(data_time)
def main(url='operationsFiles/operations.csv'):
    size = os.path.getsize(url)
    if size == 0:
        raise FileExistsError("Файл пустой")
    try:
        with open(url, 'r') as file:
            contents = file.readlines()
            contents.pop(0)
            result = format_lst_contents(contents)
            return result
    except FileNotFoundError:
        print('Нет файла по указанному пути', url)


if __name__ == '__main__':
    print(main())


