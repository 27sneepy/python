#задача 5
#a=int(input())
#if (a%4==0 and a%100!=0) or a%400==0:
#    print("YES")
#else:
#    print("NO")
# #13
# a=int(input())
# if a==1:
#     print(2*3.14*a)
# elif a==2:
#     c=int(input())
#     b=int(input())
#     print(3.14*c*b)
# elif a!=1 and a!=2:
#     print("error")
# #15 первое решение
# a=int(input())
# a1=a//10
# a2=a%10
# a31=a//100
# a32=a31//10
# if ((a1%2==0 and a2%2==0) or (a2%2==0 and a32%2==0) or (a1%2==0 and a32%2==0)) or ((a1%5==0 and a2%5==0) or (a2%5==0 and a32%5==0) or (a1%5==0 and a32%5==0)):
#     print(a)
# else:
#     print(a+1)
#15 второе решение
# a=int(input())
# a1=a%10
# a2=a//100
# a3=a//10%10
# count=0
# if a1%2==0 or a1%5==0:
#     count+=1
# if a2%2==0 or a2%5==0:
#     count+=1
# if a3%2==0 or a3%5==0:
#     count+=1
# if count>=2:
#     print(a)
# else:
#     print(a+1)
#17
# a=int(input())
# b=int(input())
# c=int(input())
# if a==b and b==c and (a+b>=c and b+c>=a and a+c>=b):
#     print("равносторонний")
# if a!=b and b!=c and a!=c and (a+b>=c and b+c>=a and a+c>=b):
#     print("разносторонний")
# if (a==b or a==c or b==c) and (a+b>=c and b+c>=a and a+c>=b):
#     print("равнобедренный")

# #задача 20
#
# # | - or
# # & - and
# a=int(input())
# match a:
#     case 1|3|5|7|8|10|12:
#         print('31')
# match a:
#     case 4|6|9|11:
#         print('30')
# match a:
#     case 2:
#         print('28')
#задача 22
a=input()
b=int(input())
match (a,b):
    #t- переменная, в которую попадает b
    #после идет условие
    case ("Рабочий", t) if 9<=t<=18:
        print('рабочее время')
    case("Выходной", t) if 10<=t<=16:
        print('рабочее время')
    case ("Праздничный", t):
        print("Не работает")
    case _:
        print("error")