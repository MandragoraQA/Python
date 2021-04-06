#Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число
import random
chislo = []
spisok = []
biki = 0
korovi = 0
for a in range(4):
    b = random.randint(0,9)
    chislo.append(b)
#print(chislo)
#сколько цифр числа угадано (быки) и сколько цифр угадано и стоит на нужном месте (коровы)
while korovi != 4:
    #пользователь вводит число
    spisok = []
    ugadai = list(input("Угадайте четырёхзначное число: "))
    for a in ugadai:
        spisok.append(int(a))
    biki = 0
    korovi = 0
    #проверка чисел
    for a in chislo:
        if a in spisok:
            biki+= 1
    for a in range (0,4):
        if chislo[a] == spisok[a]:
            korovi+=1
    if korovi < 4:
        print("Быков:", biki, "Коров:", korovi)
#выход из цикла, правильное число
print("Вы угадали число")








