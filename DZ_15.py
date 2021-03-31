#Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
dlina = int(input("Введите длину стороны квадрата: "))
simvol= input("Введите символ: ")
tolstiy = input("Введите заполненность, 1 - если квадрат заполненный, 2 - если пустой: ")
#переменная логического типа
if tolstiy == "1" : zapl = True
else : zapl = False
#тело функции
def kvadrat (dlina,simvol,tolstiy):
    if tolstiy:
        side = simvol*dlina
    else:
        side = simvol + " " * (dlina-2)+simvol
    print(simvol*dlina)
    for a in range(dlina-2):
        print(side)
    print(simvol*dlina)
kvadrat (dlina,simvol,zapl)

#Напишите функцию, которая считает количество цифр в числе.
chislo = input("Введите число: ")
def dlina(chislo):
    print(len(chislo))
dlina(chislo)









