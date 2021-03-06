# функции для главного меню консольного файлового менеджера
import os
import shutil
import sys
import json

this_path = os.getcwd()
files = []  # для сохранения списка файлов в текущей директории
folders = []  # для сохранения списка папок в текущей дирректории


# функции создания папки

def create_dir(folder):
    os.mkdir(folder)
    message = f'Создана папка {folder}!'
    return message


def create_folder():
    folder = input('Введите название папки, которую нужно создать: ')
    full_path = os.path.join(this_path, folder)
    try:
        message = create_dir(folder)
    except FileExistsError:
        message = f'Папка {folder} уже существует!'
    return message


# функция удаления папки или файла

def delete_folder_file():
    folder = input('Введите название папки/файла, которую(ый) нужно удалить: ')
    full_path = os.path.join(this_path, folder)
    try:
        os.rmdir(full_path)
        print(f'Папка {folder} удалена!')
    except NotADirectoryError:
        os.remove(full_path)
        print(f'Файл {folder} удален!')
    except FileNotFoundError:
        print('Такой(го) папки/файла не существует!')


# функция копирования папки или файла

def copy_folder_file():
    folder = input('Введите название папки/файла, которую(ый) нужно скопировать: ')
    full_path = os.path.join(this_path, folder)
    if not os.path.exists(full_path):
        print('Такой(го) папки/файла не существует!')
    else:
        new_folder = input('Введите название для копии папки/файла: ')
        new_full_path = os.path.join(this_path, new_folder)
        try:
            shutil.copytree(full_path, new_full_path)
            print(f'Папка {folder} скопирована в папку {new_folder}!')
        except NotADirectoryError:
            shutil.copyfile(full_path, new_full_path)
            print(f'Файл {folder} скопирован в файл {new_folder}!')
        except FileNotFoundError:
            print('Такой(го) папки/файла не существует!')


# функция просмотра только папок

def get_only_folders():
    content_list = list(os.listdir())
    for folder in content_list:
        if os.path.isdir(folder):
            folders.append(folder)
    return folders


# функция просмотра только файлов

def get_only_files():
    content_list = list(os.listdir())
    for file in content_list:
        if os.path.isfile(file):
            files.append(file)
    return files


# функция сохранения содержимого рабочей директории в файл listdir.txt

def dir_in_files():
    with open('listdir.txt', 'w', encoding='utf-8') as f:
        f.write(f'Файлы в рабочей директории: {get_only_files()}\nПапки в рабочей директории: {get_only_folders()}')


# функция просмотра информации об операционной системе

def view_sys_info():
    return f'Операционная система: {os.name}, {sys.platform}'


# функция вывода создателя программы

def display_program_creator():
    return 'Создатель программы - Светлана Ж.'


# функция смены рабочей директории

def change_dir():
    new_path = input('Введите полный путь, куда следует перейти: ')
    try:
        os.chdir(new_path)
        print(f'Вы перешли в директорию: {new_path}')
        print(f'Файлы в рабочей директории: {get_only_files()}\nПапки в рабочей директории: {get_only_folders()}')
    except OSError:
        print(f'Директории: {new_path} не существует!')


# функция возврата в директорию проекта "Консольный файловый менеджер"

def return_project_dir():
    if os.getcwd() == os.path.join('D:' + os.sep, 'Python', 'Projects', 'Консольный файловый менеджер'):
        print('Вы уже находитесь в директории "Консольного файлового менеджера" ')
    else:
        new_path = os.path.join('D:' + os.sep, 'Python', 'Projects', 'Консольный файловый менеджер')
        os.chdir(new_path)
        print('Вы перешли в директорию проекта "Консольный менеджер" ')
        print(f'Файлы в рабочей директории: {get_only_files()}\nПапки в рабочей директории: {get_only_folders()}')


# функция чтения числа, которое сохранили

def read_number(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            number = json.load(f)
    else:
        number = 0
    return number


# функция чтения списка данных, который сохранили

def read_list(file_name):
    if os.path.exists(file_name):
        data = []
        with open(file_name, 'r') as f:
            for item in f:
                data.append(item.replace('\n', ''))
    else:
        data = []
    return list(data)


# декоратор для функции с одним входным аргументом

def add_separators_arg1(my_func):
    def wrapper(arg1):
        print('*' * 39)
        my_func(arg1)
        print('*' * 39)
    return wrapper


# декоратор для функции с тремя входными аргументами

def add_separators_arg3(my_func):
    def wrapper(arg1, arg2, arg3):
        print('*' * 39)
        my_func(arg1, arg2, arg3)
        print('*' * 39)
    return wrapper


# функция печати баланса счета

@add_separators_arg1
def print_funds(personal_account):
    print(f'Баланс счета: {personal_account} руб.')


# функция печати истории покупок

@add_separators_arg3
def print_history(sum_history, name_history, total_sum_buy):
    if len(sum_history) == 0:
        print('Покупок не было!')
    else:
        print('История покупок:')
        for i in range(len(name_history)):
            print(f" {name_history[i]} {'_' * (25 - len(name_history[i]))} {sum_history[i]} руб.")
        print(f" ИТОГО {'_' * (25 - len(str(total_sum_buy)))} {total_sum_buy} руб.")