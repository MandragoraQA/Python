#первое задание
#ввести два числа
chislo1 = int(input("Введите первое число: "))
chislo2 =int(input("Введите второе число: "))
count = 0 #количество нужных чисел в диапазоне
summa = 0 #сумма чисел
#вывод cуммы и среднего арифмитического чётных чисел
for a in range(chislo1,chislo2 + 1):
    if a%2 == 0:
        count=count+1
        summa=summa+a
print("Сумма чётных чисел: ",summa,"\nСреднее арифмитическое чётных чисел: ", summa/count)
count = 0
summa = 0
#вывод cуммы и среднего арифмитического нечётных чисел
for a in range(chislo1, chislo2 + 1):
    if a%2 == 1:
        count=count+1
        summa=summa+a
print("Сумма нечётных чисел: ",summa,"\nСреднее арифмитическое нечётных чисел: ",summa/count)
count = 0
summa = 0
#вывод cуммы и среднего арифмитического кратных 9
for a in range(chislo1, chislo2 + 1):
    if a%9 == 0:
        count=count+1
        summa=summa+a
print("Сумма чисел кратных 9: ",summa,"\nСреднее арифмитическое чисел кратных 9: ",summa/count)

#второе задание
#пользователь вводит число
chislo = int(input("Введите число: ")
    #начало цикла
while chislo != 7:
    if chislo < 0:
        print("Number is negative")
    elif chislo > 0:
        print("Number is positive")
    elif chislo == 0:
        print("Number is equal to zero")
    chislo = int(input("Введите число: "))
    #конец цикла
print("Good bye!")