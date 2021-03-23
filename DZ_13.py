#Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в строке замену одного слова на другое.
stroka = input("Введите строку: ")
slovo = input("Введите слово для поиска: ")
zamena = input("Введите слово для замены: ")
#ищем слово и заменяем его сразу в цикле
for a in range (len(stroka) - len(slovo)+1):
    if slovo == stroka[a:a + len(slovo)]:
        stroka = stroka.replace(slovo,zamena)
print(stroka)


#Пользователь вводит с клавиатуры арифметическое выражение. Необходимо вывести на экран результат выражения.
stroka = input("Введите арифмитическое выражение, состоящее из число,оператор,число: ")
#если сложение
if "+" in stroka:
    chislo1=int(stroka[:stroka.index("+")])
    chislo2=int(stroka[stroka.index("+")+1:])
    print("Значение выражения: ",chislo1+chislo2)
#если вычитание
elif "-" in stroka:
    chislo1=int(stroka[:stroka.index("-")])
    chislo2=int(stroka[stroka.index("-")+1:])
    print("Значение выражения: ",chislo1-chislo2)
#если умножение
elif "*" in stroka:
    chislo1=int(stroka[:stroka.index("*")])
    chislo2=int(stroka[stroka.index("*")+1:])
    print("Значение выражения: ",chislo1*chislo2)
#если деление
elif "/" in stroka:
    chislo1=int(stroka[:stroka.index("/")])
    chislo2=int(stroka[stroka.index("/")+1:])
    print("Значение выражения: ",int(chislo1/chislo2))



