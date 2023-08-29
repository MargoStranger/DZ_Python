#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

import random
eagle_count = 0
tails_count = 0
money = []
side_money = ("eagle", "tails")
for i in range(random.randint(2, 20)):
    money.append(random.choice(side_money))
    if money[i] == "tails":
        tails_count += 1
    else: 
        eagle_count += 1

print(money)

if tails_count > eagle_count:
    print(f"Нужно перевернуть {eagle_count} орлов")
else:
    print(f"Нужно перевернуть {tails_count} решек")



