#math - библиотека для мат вычислений
#random- библиотека для генерации псевдослучайных чисел
#import math #импортируем модуль (как коробку)
#from math import sqrt  #импортируем инструмент from math
#import math as mth #меняем название модуля и импортируем
from future.backports import count

# import math
# print(math.sqrt(25))
#
# from math import pow,sqrt
# from math import * #* - все инструменты из модуля
# print(pow(3,2))
#
#
# import math as mth
# print(mth.pow(3,3))
#
# from random import randint,choice
# print(randint(1,100)) #от какого до какого числа (диапазон)
# l=["a","b","c","d","e"]
# print(choice(l))

# #задача 9
# a=input()
# i=len(a)//2
# print(a[i:],a[:i])
#
# #14
# a=input()
# j=a[::2]
# #[от какого индекса:до какого индекса: с каким шагом]
# k=a[1::2]
# k=[::-1]
# print(j+k)
#
# #15
# a=input()
# for i in range(0, len(a)):
#     print(a[i:i+3])
#12
# a="шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс"
# a=a.split(", ")
# for i in a:
#     if i==i[::-1]:
#         print(i)
#16
a=input()
alpha=""
amount=0
#уникализирует список [1,2,3,4]
setter=set(a)
print(setter)
for i in setter:
    count=a.count(i)
    if count>amount:
        alpha=i
        amount=count
print(alpha, amount)
print(a[::3])
maxim=0
indexes=[0,0]
print(a.rfind("o"))
for i in setter:
    if a.count(i)==1:
        continue
    backward=a.rfind(i)
    forward=a.find(i)
    if (backward - forward) > maxim:
        maxim=backward-forward
        # indexes[0]=backward
        # indexes[1]=forward   <--- можно и так
        indexes=a[forward:backward]
print(indexes)