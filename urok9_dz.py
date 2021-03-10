#первая задача
#пользователь вводит границы диапазона и число
graniza1 = int(input("Введите первую границу диапазона: "))
graniza2 = int(input("Введите вторую границу диапазона: "))
chislo = int(input("Введите число: "))
#для выбранного диапазона
for a in range (graniza1, graniza2 +1):
#пока не выполнено условие будет повторяться
    while chislo > graniza2 or chislo < graniza1:
        chislo = int(input("Введите число: "))
#выделять нужное число
    if a == chislo: print("!",a,"!", end="")
    else:print(a, end="")


#вторая задача
#программа загадывает число
import random
chislo = random.randint(1,500)
#print(chislo)
count = 1 #количество угадываний
#игрок вводит числа
otvet =int(input("\nУгадайте число от 1 до 500: "))
#начало цикла угадывания
while otvet != chislo:
    count +=1
#если ответ больше
    if otvet > chislo:
        otvet = int(input("Число должно быть меньше, введите число: "))
# если ответ меньше
    elif otvet < chislo and otvet > 0:
        otvet = int(input("Число должно быть больше, введите число: "))
# для выхода из программы
    elif otvet == 0:break
# ответ совпадает с загданным
if otvet == chislo:print("Верно. Вы угадали число за",count,"попыток")