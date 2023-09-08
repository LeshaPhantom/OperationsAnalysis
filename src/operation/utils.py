from src.operation.schemas import key
import os

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
    return dict(zip(key, lst))

def main(URL='operationsFiles/operations.csv'):
    size = os.path.getsize(URL)
    if size == 0:
        raise FileExistsError("Файл пустой")
    try:
        with open(URL, 'r') as file:
            contents = file.readlines()
            contents.pop(0)
            result = format_lst_contents(contents)
            return result
    except FileNotFoundError:
        print('Нет файла по указанному пути', URL)


if __name__ == '__main__':
    print(main())
