#пользователь вводит числа через пробел
spisok = []
chislo = input("Введите числа через пробел: ")
for a in chislo:
    if a != " ":
        spisok.append(a)
def sort(spisok):
    spisok.sort()
    print ("Отсортировано методом Питон:", spisok)
def puzir(spisok):
    sorti_on = True
    while sorti_on:
        sorti_on = False
        for a in range(len(spisok)-1):
            if int(spisok[a]) > int(spisok[a+1]):
                spisok[a],spisok[a+1] = spisok[a+1],spisok[a]
                sorti_on = True
    print("Отсортировано методом пузырька:", spisok)
puzir(spisok)
sort(spisok)









