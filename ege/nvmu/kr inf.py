#kr inf
# #10
# count = 0
# with open("9.txt") as f:
#     for line in f:
#         a = list(map(int, line.split()))
#         for x in a:
#             if a.count(x) == 3:  # число повторяется ровно 3 раза
#                 y = sum(a) - 3 * x  # неповторяющееся число
#                 if x % 2 == 1 and y % 2 == 0:  # x — нечетное, y — четное
#                     count += 1
#                 break
# print(count)

#11
# with open("9.txt", "r") as f:
#     k=0
#     for line in f:
#         a=list(map(int,line.split()))
#         if len(set(a))<6:
#             m=max(a)
#             if a.count(m)==1:
#                 s=0
#                 for x in a:
#                     if a.count(x)>1:
#                         s+=x
#                 if s<m:
#                     k+=1
#                     print(k)


#12
# with open("9.txt", "r") as f:
#     for line in f:
#         a=list(map(int,line.split()))
#         two=0
#         one=0
#         for x in set(a):
#             if a.count(x)==2:
#                 two+=1
#             if a.count(x)==1:
#                 one+=1
#         if two==2 and one==3 and a.count(max(a))==1:
#             print(sum(a))
#             break

#13
# from math import *
# a=128*2+10
# i=ceil(log2(a))
# idn=ceil(73*i/8)
# print(int((idn*29_696)/1024))
# #2407

#14
# from math import *
# a=10+52+963
# i=ceil(log2(a))
# for x in range(1,10000):
#     idn=ceil(i*x/8)
#     if 2000*idn<=693*1024:
#         print(x)
# #257

#15
# from math import *
# for a in range(1,10000):
#     i=ceil(log2(a))
#     idn=ceil(261*i/8)
#     if 252_500*idn>31*2**20:
#         print(a)
#         break

#16
# for x in range(21):
#     s1=8*21**6+2*21**5+9*21**4+3*21**3+4*21**2+x*21**1+2
#     s2=2 * 21 ** 6 + 9 * 21 ** 5 + 2 * 21 ** 4 + 4 * 21 ** 3 + x * 21 ** 2 + x * 21 ** 1 + 7
#     s3=6*21**6+7*21**5+5*21**4+6*21**3+4*21**2+x*21**1+8*21**0
#     s=s1+s2+s3
#     if s%20==0:
#         print(x,s//20)

#17
# a=361*2349**84-89**192+1953**481*4843**151
# b=[]
# while a>0:
#     b.append(a%9)
#     a=a//9
# print(b.count(5))
#235

#18
# from sys import *
# for i in range(10,36):
#     for x in range(i):
#         for y in range(i):
#             for z in range(i):
#                 for w in range(i):
#                     s1=y*i**3+7*i**1+x
#                     s2=w*i**3+y*i**2+9*i**1+z
#                     s3=z*i**4+x*i**3+y*i**2+x*i**1+y
#                     if s1+s2==s3:
#                         print(x,y,z,w,"",i)
#                         exit()

