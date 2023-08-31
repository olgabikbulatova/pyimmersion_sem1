# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
min_n = 2
max_n = 10
for i in range(min_n, max_n+1):
    for j in range(min_n, max_n // 2 + 1):
        print(f'{j} * {i: >2} = {(j * i): >2}', end=' '*5)
    print()
print()
for i in range(min_n, max_n+1):
    for j in range(max_n // 2 + 1, max_n):
        print(f'{j} * {i: >2} = {(j * i): >2}', end=' '*5)
    print()