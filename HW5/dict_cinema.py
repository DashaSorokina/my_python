cinema = {'Пятница':{12:250,16:350,20:450},
          'Чемпионы':{10:250,13:350,16:350},
          'Пернатая банда':{10:350,14:450,18:450}}
film = input('Выберите фильм: ')
date = input('Выберите день(сегодня/завтра): ')
time = int(input('Выберите время: '))
tickets = int(input('Количество билетов: '))
price=cinema[film][time]

def count(tickets):
    if tickets >= 20:
        return 0.8
    else:
        return 1

def discount(date):
    if date == "сегодня":
        return 1
    else:
        return 0.95
print('Фильм:',film,'День: ',date,'Время: ',time,'Количество билетов: ',tickets,'Стоимость: ',count(tickets)*discount(date)*price*tickets)
