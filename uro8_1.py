#введите два числа
chislo1 = int(input("Введите первое число: "))
chislo2 =int(input("Введите второе число: "))
summa=0 #вспомогательная переменная для суммы чисел
count=0 #вспомогательная переменная для количества
#подсчёт суммы чисел суммы чисел в диапазоне и их количества
for a in range (chislo1, chislo2 +1):
    summa=summa+a
    count=count+1
print("Сумма всех чисел: ",summa, "\nСреднее арифмитическое чисел: ",summa/count)


