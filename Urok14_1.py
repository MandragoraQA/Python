#Создать список из 30 целых, заполненном случайными числами в диапазоне от -100 до 100
import random
diapason = [] #задаем список
spisok1 = []
spisok2 = []
spisok3 = []
spisok4 = []
for a in range(20):
    a = random.randint(-100,100)
    diapason.append(a)
#print(diapason)
for b in diapason:
    if b%2 == 0:
        spisok1.append(b)
    elif b%2 == 1:
        spisok2.append(b)
for b in diapason:
    if b<0:
        spisok3.append(b)
    elif b>0:
        spisok4.append(b)
print("Чётные числа: ",spisok1)
print("Нечётные числа: ",spisok2)
print("Отрицательные числа: ",spisok3)
print("Положительные числа: ",spisok4)











