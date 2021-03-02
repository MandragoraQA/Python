#первое задание
#ввести два числа
chislo1 = int(input("Введите первое число: "))
chislo2 =int(input("Введите второе число: "))
#вывод каждого кратного семи
for resultat in range(chislo1,chislo2 + 1):
    if resultat%7 == 0:
        print(resultat)

#второе задание
#ввести два числа
chislo1 = int(input("Введите первое число: "))
chislo2 =int(input("Введите второе число: "))
kratnoe = 0 #вспомогательная переменная
#вывод всех чисел
for resultat in range(chislo1,chislo2 + 1):
    print(resultat)
#вывод всех чисел от большего к меньшему
for resultat in range(chislo2,chislo1 -1, -1):
    print(resultat)
#вывод всех чисел в диапазоне кратных 7
for resultat in range(chislo1,chislo2 +1):
    if resultat%7 == 0:
        print(resultat)
#вывод количества чисел кратных 5
for resultat in range(chislo1,chislo2 +1):
    if resultat%5 == 0:
        kratnoe=kratnoe+1
print(kratnoe)

#третье задание
#ввести два числа
chislo1 = int(input("Введите первое число: "))
chislo2 =int(input("Введите второе число: "))
#вывод чисел в диапазоне
for resultat in range(chislo1,chislo2 + 1):
    if resultat % 3 == 0 and resultat % 5 == 0: print("Fizz Buzz") #если кратно 3 и 5
    elif resultat % 3 == 0:print("Fizz") #если кратно 3
    elif resultat % 5 == 0:print("Buzz") #если кратно 5
    else:print(resultat) #вывести остальные числа