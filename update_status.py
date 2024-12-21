status = ["Выполнено", "В процессе", "Отложено"]
print('Статусы заметки: \nВыполнено: 1 \nВ процессе: 2 \nОтложено: 3')
note = input('\nВведите статус заметки: ')
if note == '1':
    print(status[0])
elif note == '2':
    print(status[1])
elif note == '3':
    print(status[2])


