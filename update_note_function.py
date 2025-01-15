import datetime

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

    note_data = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": datetime.date.today().strftime("%d-%m-%Y"),
        "Дедлайн": issue_date
    }

    return note_data

def update_note(note):
    while True:
        field = input('Какие данные вы хотите обновить? (Имя, заголовок, описание, статус, деделайн): ')
        if field in note.keys():
            break
        else:
            print("Некорректное имя поля. Пожалуйста, попробуйте снова.")

    new_value = input(f"Введите новое значение для {field}: ")

    if field == "Дедлайн":
        try:
            datetime.datetime.strptime(new_value, "%d-%m-%Y")
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, попробуйте снова.")

    note[field] = new_value

    print(f"Заметка обновлена:\n{note}")

    return note

new_notes = create_note()

updates_notes = update_note(new_notes)

print(f"  Имя: {new_notes['Имя']}")
print(f"  Заголовок: {new_notes['Заголовок']}")
print(f"  Описание: {new_notes['Описание']}")
print(f"  Статус: {new_notes['Статус']}")
print(f"  Дата создания: {new_notes['Дата создания']}")
print(f"  Дедлайн: {new_notes['Дедлайн']}")




