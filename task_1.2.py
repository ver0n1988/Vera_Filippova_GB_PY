# создаем список кубов нечетных чисел от 1 до 1000:
cubes = []
for i in range(1001):
    if i % 2 != 0:
        cubes.append(i ** 3)


# функция для вычленения цифр из чисел и нахождения суммы цифр
def sum_digits(n):
    sum = 0

    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


# находим cумму чисел, в которых сумма цифр делится на 7 без остатка:
result = 0
for num in cubes:
    if sum_digits(num) % 7 == 0:
        result += num
print(result)

# добавляем 17 к каждому элементу списка и снова находим сумму чисел, в которых сумма цифр делится на 7 без остатка:
new_list = []
for num in cubes:
    num += 17
    new_list.append(num)

new_result = 0
for num in new_list:
    if sum_digits(num) % 7 == 0:
        new_result += num
print(new_result)
