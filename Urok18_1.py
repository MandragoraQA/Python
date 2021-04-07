#Пользователь вводит количество секунд, минут, часов. Программа выводит количество секунд за это время.
chasi =int(input("Введите количество часов:"))
minuti =int(input("Введите количество минут:"))
sekundi = int(input("Введите количество секунд:"))
def vremja(chasi,minuti,sekundi):
    a = chasi * 3600
    b = minuti * 60
    print("Количество секунд равно: ", a+b+sekundi)
vremja(chasi,minuti,sekundi)









