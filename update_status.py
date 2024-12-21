change_status = ["Выполнено", "В процессе", "Отложено"]
print('Текущий статус заметки: В процессе')
print('Выберити новый статус заметки: \n1: Выполнено  \n2: В процессе \n3: Отложено')
note = input('\nВведите статус заметки: ')
if note == '1':
    print(change_status[0])
elif note == '2':
    print(change_status[1])
elif note == '3':
    print(change_status[2])
