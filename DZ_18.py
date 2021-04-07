#Пользователь вводит с клавиатуры строку и ещё один символ.
stroka = input("Введите строку: ")
simvol = input("Введите символ: ")
count=0
#Программа должна вывести: сколько раз символ встречается в строке, на какой позиции встречается первый раз.
for a in stroka:
    if a == simvol:
        count+=1
next = stroka.index(simvol)
print("Символ встречается: ", count, "раза")
print("Первый раз встречается на позиции: ",next+1)

#Пользователь вводит с клавиатуры строку
stroka = input("Введите строку: ")
resultat = []
#Программа должна после каждого символа добавить точку и вывести результат
for a in stroka:
    if a != " ":
        resultat.append(a)
        resultat.append(".")
    else:resultat.append(" ")
print("Строка теперь выглядит вот так:\n"," ".join(resultat))








