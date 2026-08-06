# count = 0
# with open("9.txt") as f:
#     for line in f:
#         x1, y1, x2, y2, x3, y3 = map(int, line.split())
#         if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
#             count += 1
# print(count)

# from math import *
# l=10
# a=62
# i=ceil(log2(a))
# idn=ceil(10*i/8)
# q=870/30
# print(int(q-idn))


# a=2**379+2**378+2**377
# print((hex(a))[2])


# with open("9.txt") as f:
#     k = 0
#     for line in f:
#         a = list(map(int, line.split()))
#         d = [x for x in a if a.count(x) == 2]   # повторяющиеся
#         q = [x for x in a if a.count(x) == 1]   # неповторяющиеся
#         if len(d) == 2 and len(q) == 4:
#             if min(q) + max(q) <= sum(d):
#                 k += 1
#     print(k)

# from math import *
# a=10+26
# i=ceil(log2(a))
# idn=ceil(30*i/8)
# for x in range(1,1000):
#     if (idn+110)*x<=(45*1024):
#         print(x)
# from math import *
# party_bits = 30 * ceil(log2(36))
# for n in range(1, 1000):
#     bits = party_bits + ceil(log2(n))
#     bytes_code = ceil(bits / 8)
#     if n * (bytes_code + 110) <= 45 * 1024:
#         ans = n
# print(ans)

# for x in range(0,2030):
#     n=7**91+7**160-x
#     d=[]
#     while n>0:
#         d.append(n%7)
#         n=n//7
#     if d.count(0)==70:
#         print(x)


# Вариант № 5083.
# k=0
# with open ("9.txt", "r") as f:
#     for line in f:
#         a,b,c=sorted(map(int, line.split()))
#         if a + b > c and c ** 2 > a ** 2 + b ** 2:
#             k += 1
# print(k)

# from math import *
# a=26
# i=ceil(log2(a))
# idn=ceil(9*i/8)
# b=10
# q=ceil(log2(b))
# r=ceil(6*q/8)
# w=1980/30
# print(int(w-r-idn))

# for x in range(1,1000):
#     a=64**11-4**10+96-x
#     d=[]
#     while a>0:
#         d.append(a%4)
#         a=a//4
#     if sum(d)==71:
#         print(x)
#         break



