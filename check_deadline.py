from datetime import datetime

current_date = datetime.today().strftime('%d-%m-%Y')
print(f'Текущая дата: {current_date}')

issue_date_str = input('Введите дату дедлайна: ').replace('.','-').replace('/','-').replace(',','-')
current_date = datetime.strptime(current_date, '%d-%m-%Y')
issue_date = datetime.strptime(issue_date_str, '%d-%m-%Y')

deadline = (issue_date - current_date).days
if deadline < 0:
    print(f'Дедлайн истек {-deadline} дней назад.')
elif deadline == 0:
    print('Дедлайн сегодня.')
else:
    print(f'Дедлайн наступит через {deadline} дней.')




