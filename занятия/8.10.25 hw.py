# #1
# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# #2
# num1 = int(input())
# num2 = int(input())
#
# if num1 > num2:
#     last = num1 % 10
#     if last == 0:
#         print("Первое больше и оканчивается на 0")
#     elif last % 2 == 0:
#         print("Первое больше и четное")
#     else:
#         print("Первое больше и нечетное")
# else:
#     print(num2)
# #3
# a = int(input())
# b = int(input())
#
# if a > 0 and b > 0:
#     print(a + b)
# elif a < 0 or b < 0:
#     print(a * b)
# else:
#     print("Оба ноль")
# #4
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b + c and b < a + c and c < a + b:
#     print("Да")
# else:
#     print("Нет")
# #5
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# dx = abs(x1 - x2)
# dy = abs(y1 - y2)
#
# if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
#     print("Да")
# else:
#     print("Нет")
#6
a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if d < 0:
    print("Уравнение не имеет решений")
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    print(x1, x2)