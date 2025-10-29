# a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
# for i in a:
#     print(ord(i), i)
# print("q"<"w")
#
# a="10"
# print(int(str(a),16))


# print("\n\t")
# print('\'')
# print("\U0001F600")
# g=r"https:\\google.com"
# print("\U0001F600")
# print(g)

# name= "Миша"
# #s[n:m:k]
# #n-начало среза
# #m-конец среза(не включительно)
# #k-шаг среза
# print(name[0:4:2])
# #Мщ
# print(name[-1])
# print(name[::-1])

# string="hello world"
# print(string.find("w"))# поиск первого вхождения подстроки
# print(string.index("d"))# возвращает индекс подстроки если такого нет выдаст ошибку
# # print(string.rfind("w"))
# print(string.split(" "))#делит строку по разделителю " "
# print(string.count(" "))#считает эл-ты количетсво подстрок
# print(string.lower())# делает текст в нижнем регистре
# print(string.upper())# поднимает текст с колен(верхний регистр)
# print(string.isdigit())# все символы строки это числа
# string="hello"
# print(string.isalpha())#true если нет пробелов в троке и цифр
# print(string.isalnum())#2 верхних метода в 1
# string="***hello world***"
# print(string.strip("*"))#удаляет выбранный символ в начале и конце строки(по умолч пробел)
# #replace(символ на что меняем, сколько раз)
# print(string.replace("*","\U0001F600",2))
# l=["h","e","e","l","l"]
# print("-".join(l))#соединяет эл-ты с разделителем

#1
# a=input()
# print(a[-4:])
#2
a=input()
print(a[0::2])