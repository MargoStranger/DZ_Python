# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

k = int(input("Введите количество чисел Фибоначчи: "))
array = [fib(i) for i in range(k)]
array_negafib = [array[i]*-1 if i % 2 == 0 else array[i] for i in range(1, k)]

array_negafib.reverse()
array_negafib.extend(array)

print(array_negafib)