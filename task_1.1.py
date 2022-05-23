#создаем переменные
minute=60
hour=minute*60
day=hour*24


#запрашиваем ввод у пользователя и создаем цикл для многократного ввода
duration = int(input('Введите время в секундах: '))

#выводим информацию до минуты
if duration<minute:
    print('{} сек' .format (duration))

#выводим информацию до часа
elif duration>=minute and duration<hour:
    user_minute=duration//minute
    user_second=duration%minute
    print('{} мин {} сек'.format (user_minute, user_second))

#выводим информацию до дня
elif duration>=hour and duration<day:
    user_hour=duration//hour
    duration=duration%hour
    user_minute=duration//minute
    user_second=duration%minute
    print('{} час {} мин {} сек'.format(user_hour, user_minute, user_second))

#выводим информацию до недели
elif duration>=day:
    user_day=duration//day
    duration=duration%day
    user_hour = duration // hour
    duration = duration % hour
    user_minute = duration // minute
    user_second = duration % minute
    print('{} дн {} час {} мин {} сек'.format(user_day, user_hour, user_minute, user_second))