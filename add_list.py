username = input('Введите имя пользователя: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки в формате день-месяц-год: ')
issue_date = input('Введите дату истечения заметки в формате день-месяц-год:  ')

titles = []
for i in range(3):
    title = input(f"Введите название заголовка {i + 1}: ")
    titles.append(title)

print('\nВы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Название заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дату создания заметки: ', created_date[:5])
print('Дату истечения заметки: ', issue_date[:5])