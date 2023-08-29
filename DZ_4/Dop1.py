# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

#4 - 3x^4 + //0x^3// - 1x^2 +//0x^1 //+ 3x^0
#3*x^4 - x^2 + 3 = 0

import random

k = int(input("Введите коэффициент X: "))
str_out = ""
kk = []
while k > 0:
    k_ran = random.randint(-10, 10)
    kk.append(k_ran)
    if k_ran == 0:
        str_out += ''
    elif k_ran == 1:
        str_out += '+' + 'x^' + str(k)
    elif k_ran == -1:
        str_out += '-' + 'x^' + str(k)
    elif k_ran < 0:
        str_out += str(k_ran) + '*' + 'x^' + str(k)
    elif k_ran > 0:
        str_out += '+' + str(k_ran) + '*' + 'x^' + str(k)
    
    k -= 1

k_ran = random.randint(-10, 10)
kk.append(k_ran)
if k_ran < 0:
    str_out += str(k_ran) + '= 0'
elif k_ran > 0:
    str_out += '+' + str(k_ran) + '= 0'

if str_out[0] == '+':
    str_out = str_out[1: ]

str_out = str_out.replace('-', ' - ')
str_out = str_out.replace('+', ' + ')

if str_out[0] == ' ':
    str_out = str_out[3: ]
    str_out = '-' + str_out

print(str_out)
print(f"Кофициенты: {kk}")
