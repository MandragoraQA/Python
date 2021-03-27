#Два списка заполняются целыми случайными числами, по 20 в каждом.
import random
#задаём списки
diapason1 = []
diapason2 = []
spisok1 = [] #содержит элементы обоих списков
spisok2 = [] #содержит элементы обоих списков без повторений;
spisok3 = [] #содержит элементы общие для двух списков;
spisok4 = [] #содержит только уникальные элементы каждого из списков;
spisok5 = [] #содержит только минимальное и максимальное значение каждого из списков
#выбираем числа
for a in range(20):
    b = random.randint(0,50)
    diapason1.append(b)
    c = random.randint(0,50)
    diapason2.append(c)
#составляем spisok1 и spisok2
spisok1 = diapason1 + diapason2
spisok2 = list(set(spisok1))
#составляем spisok3 и spisok4
for a in diapason1:
    if a in diapason2:spisok3.append(a)
    else:spisok4.append(a)
for b in diapason2:
    if b not in diapason1:spisok4.append(b)
#составляем spisok5
list.sort(diapason1)
list.sort(diapason2)
min1 =diapason1[0]
max1= diapason1[-1]
min2=diapason2[0]
max2=diapason2[-1]
spisok5=min1,max1,min2,max2
print(diapason1)
print(diapason2)
print("Список с элементами обоих списков: ", spisok1)
print("Список с элементами обоих списков без повторений: ", spisok2)
print("Список с элементами общими для двух списков: ", spisok3)
print("Список с уникальными элементами каждого из списков: ", spisok4)
print("Список с минимальными и максимальными значениями: ", spisok5)









