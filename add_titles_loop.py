titles = []
while True:
    title = input(f'Введите название заголовка: ')
    if title == '':
        break
    else:
        titles.append(title)
contents = []
while True:
    content = input('Введите описание заголовка: ')
    if content == '':
        break
    else:
        contents.append(content)

print('\nНазвание заголовков: ','; '.join(titles))
print('Описание заголовков: ','; '.join(contents))