import datetime
from colorama import Back, Style


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

    issue_date = input("Введите дату дедлайна (день-месяц-год): ")

    try:
        datetime.datetime.strptime(issue_date, "%d-%m-%Y")
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате 'день-месяц-год'.")
        issue_date = input("Введите дату дедлайна (день-месяц-год): ")

    note = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": datetime.date.today().strftime("%d-%m-%Y"),
        "Дедлайн": issue_date
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

notes_list = []

while True:
    print('\nДобро пожаловать в "Менеджер заметок"'
    '\n1: Отображение списка заметок.'
    '\n2: Создание новой заметки.'
    '\n3: Завершение программы.'
          )
    choices = int(input('Ваш выбор: '))
    if choices == 2:
        notes_list.append(create_note())
    elif choices == 1:
        display_notes(notes_list)
    elif choices == 3:
        print('\nДо свидания.')
        break
    else:
        print('\nВведите верное значение.')
        continue
