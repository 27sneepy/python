#+ (складывает)
#- (вычитает)
#/ (делит)
#* (умножает)
#% (остаток от деления)
#// (целочисленное деление)
#() (Объединение)
#** (возведение в степень)

#and - логическое умножение (и)
#print(True and 0)
#or- логическое или
#print(True or 0)
#not - не
#print(not(True))
#числа и объекты
#== - сравнение(эквивалентность)
#print(True==True)
#!= - сравнение(отрицание)
#print(5!=5)

#числа
#>= <= < >
#print(10>=10)

#if 1>2:
#    print(2)

# is_weather=input("Идет ли дождь? : ")
# if is_weather == "yes":
#     print("Да идет")
# elif is_weather == "no":
#     print("Нет не идет")
# #elif может быть бесконечное количество
# else:#действие срабатывает если не сработали предыдущие
#     print("МБ да МБ нет")
#
# a=input("Введите слово: ")
# match a:
#     case "no":
#         print("Почему нет")
#     case "yes":
#         print("Почему да")
#     case _:
#         print("Любые символы")

# #задача 3
# a=int(input())
# if a%2==0:
#     print("Четное")
# else:
#     print("Нечетное")
# #задача 9
# a=int(input())
# if a>0 and a%2==0:
#     print("Положительное и четное")
# elif a>0 and a%2!=0:
#     print("Положительное и нечетное")
# elif a%10==0 and a>0:
#     print("Положительное и оканчивается на 0")
# elif a<0:
#     print("Отрицательное")
#задача 7
a=int(input())
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
else:
    print(a)

