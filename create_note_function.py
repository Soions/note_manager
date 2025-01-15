import datetime


def create_note():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status_option = ['Новая', 'В процессе', 'Выполнена']

    # Запрос статуса
    while True:
        print('Выберите статус:')
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

    # Проверка формата даты
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


def print_note():
    print("Список заметок:")
    for i, note in enumerate(notes_list, 1):
        print(f"{i}. Имя: {note['Имя']}")
        print(f"  Заголовок: {note['Заголовок']}")
        print(f"  Описание: {note['Описание']}")
        print(f"  Статус: {note['Статус']}")
        print(f"  Дата создания: {note['Дата создания']}")
        print(f"  Дедлайн: {note['Дедлайн']}")


notes_list = []

while True:
    print("Введите данные заметок: ")
    new_notes = create_note()
    notes_list.append(new_notes)

    print("Хотите добавить ещё одну заметку? (да/нет): ", end="")
    response = input().lower()

    if response == "нет":
        break

print_note()