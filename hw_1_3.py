# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 100
num = randint(LOWER_LIMIT, UPPER_LIMIT)
attemps = 5
# print(num)
for i in range(attemps):
    print('попытка №', i + 1, end=' ')
    n = int(input('введите число: '))
    if n == num:
        print(n, 'вы угадали, поздравляем!')
        break
    elif n > num:
        print(n, 'больше')
        continue
    else:
        print(n, 'меньше')
        continue
else:
    print('попытки закончились, попробуй еще раз')