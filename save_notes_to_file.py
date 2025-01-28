import json
import yaml
import datetime
from datetime import timedelta
from colorama import  Back, Style

def create_note():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status_option = ['Новая', 'В процессе', 'Выполнена']

    while True:
        print(f'Выберите статус:')
        for i, stat in enumerate(status_option, start=1):
            print(f'{i}) {stat}')
        status_input = input('Ваш выбор: ')

        try:
            status_choice = int(status_input)
            if 1 <= status_choice <= len(status_option):
                status = status_option[status_choice - 1]
                print(f'Вы выбрали: {status}')
                break
            else:
                print("Пожалуйста, выберите допустимый статус.")
        except ValueError:
            print("Пожалуйста, введите допустимое значение.")
    note = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": datetime.date.today().strftime("%d-%m-%Y"),
        "Дедлайн": (datetime.date.today() + timedelta(days=7)).strftime("%d-%m-%Y")
    }

    return note

def display_notes(notes):
    if len(notes) == 0:
        print('\n', Back.RED, 'У вас нет заметок', Style.RESET_ALL)

    elif len(notes) == 1:
        print('\n',Back.BLUE, 'Ваша заметка', Style.RESET_ALL)
        for note in notes:
            print(f'Имя: {note['Имя']}')
            print(f'Заголовок: {note['Заголовок']}')
            print(f'Описание: {note['Описание']}')
            print(f'Статус: {note['Статус']}')
            print(f'Дата создания: {note['Дата создания']}')
            print(f'Дедлайн: {note['Дедлайн']}')

    else:
        print('\n', Back.GREEN, 'Ваши заметки:', Style.RESET_ALL)
        for i, note in enumerate(notes, start=1):
            print(f'\nЗаметка №{i}')
            print(f'Имя: {note['Имя']}')
            print(f'Заголовок: {note['Заголовок']}')
            print(f'Описание: {note['Описание']}')
            print(f'Статус: {note['Статус']}')
            print(f'Дата создания: {note['Дата создания']}')
            print(f'Дедлайн: {note['Дедлайн']}')

def load_notes_from_file(filename):
    try:
        with open(filename , encoding='utf-8') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа')

    display_notes(data)

def save_notes_to_file(note, filename):
    try:
        with open(filename, "w", encoding='utf-8') as file:
            yaml.dump(note, file)
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as ex:
        print(f'Ошибка {ex}')

def addend_notes_to_file(note, filename):
    try:
        with open(filename, "a", encoding='utf-8') as file:
            yaml.dump(note, file)
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as ex:
        print(f'Ошибка {ex}')

def save_notes_to_file_json(note, filename):
    try:
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(note, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as ex:
        print(f'Ошибка {ex}')

new_notes = []

while True:
    print('\n1: Новая заметка')
    print('2: Показать заметки')
    print('3: Перезаписать заметки в файле(.yaml or .json)')
    print('4: Загрузить заметки')
    print('5: Добавить заметки в файл')
    print('Для завершение введите любой символ вне списка')
    choices = int(input('Ваш выбор: '))
    if choices == 1:
        new_notes.append(create_note())
        continue
    elif choices == 2:
        display_notes(new_notes)
        continue
    elif choices == 3:
        filename = input('Введите название файла(example.yaml): ')
        if '.yaml' in filename:
            save_notes_to_file(new_notes, filename)
        elif '.json' in filename:
            save_notes_to_file_json(new_notes, filename)
        else:
            print('Введите верный формат файла.')
            continue

        continue
    elif choices == 4:
        try:
            filename = input('Введите название файла(example.yaml): ')
            load_notes_from_file(filename)
        except Exception as ex:
            print(f'Ошибка {ex}')
        continue
    elif choices == 5:
        filename = input('Введите название файла(example.yaml): ')
        addend_notes_to_file(new_notes, filename)
    else:
        break
