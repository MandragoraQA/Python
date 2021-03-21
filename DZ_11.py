#задача 1, стандартная шахматная доска 8*8
indicator = 4 #число повторов 2 строк
chislo = int(input("Введите размер клетки для шахматной доски: "))
while indicator != 0: #пишем строки
    for c in range (1, 5): #первая строка
        for a in range (1,chislo+1):
            print("*", end="")
        for b in range (1,chislo+1):
            print("-", end="")
    print("")
    for c in range (1, 5): #вторая строка
        for b in range (1,chislo+1):
            print("-", end="")
        for a in range (1,chislo+1):
            print("*", end="")
    print("")
    indicator-=1
    

#задача 2, имеется букет, который собран из разных видов цветов (минимум 4)
zweti = [] #список названий цветов
skolko = [] #список количества цветов
chislo = int(input("Введите количество видов цветов в букете, минимум 4: ")) #количество видов цветов
while chislo < 4:
    chislo = int(input("Введите количество видов цветов в букете, минимум 4: "))
#заполнение списков
for a in range(1,chislo+1):
    b = input("Введите название цветов: ")
    zweti.append(b)
    c = int(input("Введите количество этих цветов в букете: "))
    skolko.append(c)
skolko1 = skolko.copy() #копия списка "skolko" для сортировки
list.sort(skolko1)
list.reverse(skolko1)
#выясняем индекс и выводим список цветов в порядке убывания
for d in skolko1:
    indicator = skolko.index(d)
    print(zweti[indicator])





