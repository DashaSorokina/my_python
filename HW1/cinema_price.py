film=input("Введите название фильма: ")
data=input("сегодня,завтра?: ")
time=int(input("Укажите время: "))
ticket=int(input("Число билетов: "))
def sale(data):
    if data=='завтра':
        return 0.95
    else:
        return 1

def salet(ticket):
    if ticket>=20:
        return 0.80
    else:
        return 1

if film=='Пятница':
 def select(time,ticket):
    if time==12:
        return 250*ticket
    if time==16:
        return 350*ticket
    if time==20:
        return 450*ticket

    

if film=='Чемпионы':
 def select(time,ticket):
    if time==10:
        return 250*ticket
    if time==13:
        return 350*ticket
    if time==16:
        return 350*ticket

if film=='Пернатая банда':
 def select(time,ticket):
    if time==10:
        return 350*ticket
    if time==14:
        return 450*ticket
    if time==18:
        return 450*ticket

print("Выбрали Фильм: ",film, "День: ",data,"Время: ",time,"Количество билетов:",ticket)
print("Результат:",select(time,ticket)*salet(ticket)*sale(data))
