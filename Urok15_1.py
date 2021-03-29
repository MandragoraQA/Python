#Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
#Функция принимает в качестве параметра: длину линии,направление, символ.
import math
dlina = int(input("Введите длину: "))
simvol= input("Введите символ: ")
direction = input("Введите направление, 1- если вертикальное, 2 - если горизонтальное: ")
def linia (dlina,simvol,direction):
    while dlina != 0:
        if direction == "1":
            print(simvol)
            dlina -= 1
        elif direction == "2":
            print(simvol, end="")
            dlina -= 1
linia(dlina,simvol,direction))












