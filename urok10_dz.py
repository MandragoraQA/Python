#задание 1
#пользователь вводит диапазон для таблицы умножения
chislo1 = int(input("Введите первое число: "))
chislo2 = int(input("Введите второе число: "))
#таблица умножения
for a in range(chislo1, chislo2 +1):
    for b in range(1,10 +1):
        print(a,"*",b,"=",a*b)

#задание 2
#показать на экран все простые числа в диапазоне, указанном пользователем
#пользователь задаёт диапазон
chislo1 = int(input("Введите первое число: "))
chislo2 = int(input("Введите второе число: "))
#все простые числа
simple = True
for a in range(chislo1, chislo2 +1):
    for b in range (2,a):
        if a%b == 0:
            simple = False
            break;
        else:
            simple = True

    if simple is True:print(a)