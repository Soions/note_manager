def create_note():
    notes = []
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    created_date = input("Введите дату создания (день-месяц-год): ")
    issue_date = input("Введите дедлайн (день-месяц-год): ")

    new_note = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дедлайн": issue_date
    }

    notes.append(new_note)

    return notes

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
    notes_list.extend(new_notes)

    print("Хотите добавить ещё одну заметку? (да/нет): ", end="")
    response = input().lower()

    if response == "нет":
        break
print_note()

while True:
    print("Хотите изменить статус заметки (да/нет): ", end="")
    response = input().lower()

    if response == "нет":
        break

    print("Введите имя заголовка: ", end="")
    criterion = input()

    title_notes = [note for note in notes_list if note['Заголовок'] == criterion]
    if title_notes:
        print('Введите новый статус заметки: ', end='')
        new_status = input()
        notes_list[notes_list.index(title_notes[0])]["Статус"] = new_status
        print(f"Статус заметки с заголовком {criterion} успешно изменен на {new_status}.")

    else:
        print("Заметок, соответствующих критерию, не найдено.")
print_note()
