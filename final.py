note = {"Имя пользоватля: ": input('Введите имя пользователя: '),
        "Названия заметок: ": [],
        "Описание заметки: ": input('Введите описание заметки: '),
        "Статус заметки: ": input('Введите статус заметки: '),
        "Дата создания: ": input('Введите дату создания заметки в формате день-месяц-год: '),
        "Дата окончания: ": input('Введите дату истечения заметки в формате день-месяц-год:  '),}
for i in range(3):
    titles = input(f'Введите название заметки: {i + 1}: ')
    note["Названия заметок: "].append(titles)
print('\nСобранная информация о заметке')
for key, value in note.items():
    print(f'{key.capitalize()}: {value }')
