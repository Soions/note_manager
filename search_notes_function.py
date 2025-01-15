import datetime
from datetime import timedelta
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

def search_notes(notes, keyword = None, status = None):
    if not keyword and not status:
        input("Вы не указали ключевое слово и статус для поиска!")
        return []

    found_notes = []

    for idx, note in enumerate(notes):
        if keyword and not status:
            if (keyword in note['Заголовок'].lower() or keyword in note['Описание'].lower() or
                    keyword in note['Имя'].lower()):
                found_notes.append(note)
        elif not keyword and status:
            if status == note['Статус']:
                found_notes.append(note)
        elif keyword and status:
            if (keyword in note['Заголовок'].lower() or keyword in note['Описание'].lower() or
                    keyword in note['Имя'].lower() or status == note['Статус']):
                found_notes.append(note)

    if not found_notes:
        print("Заметки, соответствующие запросу, не найдены.")
        input("Для продолжения нажмите Enter")
    return found_notes

notes_list = []

while True:
    print('\nДобро пожаловать в "Менеджер заметок"'
    '\n1: Отображение списка заметок.'
    '\n2: Создание новой заметки.'
    '\n3: Поиск заметки.'
    '\n4: Завершение программы.'
          )
    choices = int(input('Ваш выбор: '))
    if choices == 2:
        print('\n')
        notes_list.append(create_note())
        input("\nНажмите Enter для продолжения")
    elif choices == 1:
        display_notes(notes_list)
        input("\nНажмите Enter для продолжения")
    elif choices ==3:
        if __name__ == '__main__':
            keyword = input("Введите ключевое слово для поиска: ").strip().lower()
            while True:
                status_option = ['Новая', 'В процессе', 'Выполнена']
                status = input("Введите статус для поиска (или оставьте пустым): ").strip().lower()
                if status and not status_option:
                    input("Вы вели неправильный статус для поиска.\nВарианты статуса: новая, в процессе, выполнена.\nДля продолжения нажмите Enter")
                    continue
                break
            found_notes = search_notes(notes_list, keyword, status)
            display_notes(found_notes)
            input("\nНажмите Enter для продолжения")
    elif choices == 4:
        print('\nДо свидания.')
        break
    else:
        print('\nВведите верное значение.')
        continue
