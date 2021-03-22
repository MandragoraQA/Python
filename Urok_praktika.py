#Пользователь вводит размер списка, программа заполняет его целыми случайными числами от -100 до 100.
import random
diapason = [] #задаем список
chislo = int(input("Введите число: "))
for a in range(1,chislo+1):
    a = random.randint(-100,100)
    diapason.append(a)
#print(diapason)
#определить минимальное и максимальное значение
list.sort(diapason)
print("Минимальное значение в списке: ", diapason [0])
list.reverse(diapason)
print("Максимальное значение в списке: ", diapason [0])
#посчитать количество отрицательных элементов
chislo1 = len([b for b in diapason if b < 0])
print("Количество отрицательных чисел: ", chislo1)
#посчитать количество положительных элементов
chislo2 = len([b for b in diapason if b > 0])
print("Количество положительных чисел: ", chislo2)
#посчитать количество нулей
null = len([b for b in diapason if b == 0])
print("Количество нулей: ", null)






