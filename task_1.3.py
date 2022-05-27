# находим корень слова
root='процент'
# создаем цикл
for i in range(1, 101):
    if (i % 10 == 0 or
            i == 11 or
            i == 12 or
            i == 13 or
            i == 14 or
            5<=i%10<=9):
        print(i,root+'ов')
    elif 2<=i%10<5:
        print(i, root + 'a')
    elif i%10 ==1:
        print(i, root)