# var 6
# 1)31
# 2) z x y w
# 3)6146
# 4)9
# 7)32
# 8)152724
# 9)1727
# 11)350
# 14)1944
# 15)78122
# 18)2466 310
# 22)8

# 2
# from itertools import *
# def fun(w, x, y, z):
#      return ((w <= z)==(x<=(not y)))and(x or z)
# for a, b in product((0,1),repeat=2):
#     table = ((1, 0, 0, 1, 1),
#               (1, 1, 1, 0, 0),
#               (0, a, 0, b, 1))
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if all(fun(**dict(zip(p, line[:4]))) == line [4] for line in table):
#                 print(''.join(p))

# 15
# def f(x,y):
#     return (78125 != y + 4*x) or (a>x) or (a>y)
# for a in range(100000):
#     if all(f(x,y) for x in range(1,100000) for y in range(1,10000)):
#         print(a)
#         break

# 8
# from itertools import *
#
# k = 0
# s = 0
# for x in product('АВИКЛОРТ', repeat=6):
#     x = ''.join(x)
#     k += 1
#     if x == 'ВИКТОР' or x == 'КИРИЛЛ':
#         s += k
# print(s)

# 9
# k=0
# with open("9.txt") as f:
#     for i in f:
#         a=list(map(int,i.split()))
#         q=[x for x in a if x%5==0]
#         w=[x for x in a if len(str(x))==2]
#         if (len(q)==0) + (len(w)==6) == 1:
#             k+=1
# print(k)



# var 7
# 1 10
# 2 x w z y
# 3 1440
# 4 8
# 7 1998000
# 8 5193
# 9 1920
# 11 67
# 14 341
# 15 16
# 18 566 2197
# 22 13

# 2
# from itertools import *
# def f(w,x,y,z):
#     return (x and (not y))or(y==z)or w
# for a1,a2,a3,a4 in product([0,1],repeat=4):
#     t=[(a1,a2,1,a3),
#        (0,0,0,1),
#        (1,0,a4,1)]
#     if len(t)==len(set(t)):
#         for p in permutations("wxyz"):
#             if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
#                 print(*p)

# 8
# from itertools import *
# k=0
# for i in product(sorted("ЧМЕСИАК"),repeat = 5):
#     s="".join(i)
#     k+=1
#     if s=="МАСИК" or s=="ЧЕЧИК":
#         print(k)
# # когда спрашивается сколько слов между словами то нужно отнимать большее от меньшего и еще 1
# print(15061-9867-1)

# 9
# k=0
# with open("9.txt") as f:
#     for i in f:
#         a=sorted(list(map(int,i.split())))
#         if len(a)==len(set(a)):
#             if a[0]*a[1]<=a[2]+a[3]+a[4]+a[5]+a[6]:
#                 k+=1
# print(k)

# 11
# from math import *
# a=4090
# i=ceil(log2(a))
# for ln in range(1,10000):
#     idn=ceil(i*ln/8)
#     if 1876*idn>184*1024:
#         print(ln)
#         break

# 14
# a=3*625**173+4*125**180+3*25**157+2*5**155+156
# b=[]
# while a>0:
#     b.append(a%25)
#     a=a//25
# print(b.count(0))

# 15
# def f(x):
#     return ((x&52!=0)and(x&36==0))<=(not(x&a==0))
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

# var 8
# 1 25
# 2 z w y x
# 3 497
# 4 24
# 7 519450
# 8 38306
# 9 2462
# 11 1024
# 14 3030
# 15 3
# 18 4948 1520
# 22 21

# №2
# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f=(not(((not y)<= x)<=w))or(z<=x)
#                 if f==0:
#                     print(x,y,z,w)
# №7
# for z in range(1,1000000):
#     song=2*(27*60+27)*56000*15
#     name=z*2**13*28
#     album=name+song
#     if album/367217732>332:
#         print(z)
#         break
# №8
# k=0
# for a in ('АБДЕОП'):
#     for b in ('АБДЕОП'):
#         for c in ('АБДЕОП'):
#             for d in ('АБДЕОП'):
#                 for e in ('АБДЕОП'):
#                     for f in ('АБДЕОП'):
#                         s=a+b+c+d+e+f
#                         k+=1
#                         if k%2==0 and s.count('А')==1 and s.count('Б')==1 and s.count('Д')==1 and s.count('Е')==1 and s.count('О')==1 and s.count('П')==1 and s[0]=='О':
#                             print(k,s)
# №14
# s=4*3125**2019+3*625**2020-2*125**2021+25**2022-4*5**2023-2024
# k=0
# while s>0:
#     if s%25>10:
#         k+=1
#     s=s//25
# print(k)

# var 9
# 1)47
# 2) w y x z
# 3) 6727500
# 4) 28
# 7) 123937
# 8) 8626
# 9) 17
# 11) 5
# 14) 7567913105
# 15) 29
# 18) 2198 805
# 22) 15

# 9
# k=0
# with open("9.txt") as f:
#     for i in f:
#         a=sorted(list(map(int,i.split())))
#         povt=[i for i in set(a) if a.count(i)==2]
#         nepovt=[i for i in set(a) if a.count(i)==1]
#         k+=1
#         if len(povt)==2 and len(nepovt)==3:
#             if (povt[0]*2+nepovt[1]*2)/4 < max(nepovt):
#                 print(k)
#                 break

# 11
# from math import *
# a=37
# i=ceil(log2(a))
# for ln in range(1,1000):
#     idn=ceil(i*ln/8)
#     if 3548*idn>12*1024:
#         print(ln)
#         break


# 15
# p=list(range(17,59))
# q=list(range(29,81))
# a=[]
# for x in range(200):
#     if not ((x in p)<=(((x in q)and(not(x in a)))<=(not(x in p)))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# 8
# from itertools import *
# k = 0
# for x in product(sorted('АЛГОРИТМ'), repeat=5):
#     s =''.join(x)
#     k += 1
# if k%2==0 and s[0] not in 'AГ' and s.count('P')>=2:
#     print(k, s)
#     break

# 2
# from itertools import *
# def fun(w, x, y, z):
#     return ((x or y) <= z) or (y == w) or z
# for a, b, c, d in product((0,1),repeat=4):
#     table = ((0, 1, a, b, 0),
#              (1, c, 1, 0, 0),
#              (d, 1, 1, 0, 0))
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if all(fun(**dict(zip(p, line[:4]))) == line [4] for line in table):
#                 print(''.join(p))

# 14
# for x in range(29):
#     s1=4*29**7+6*29**6+3*29**5+x*29**4+7*29**3+9*29**2+2*29**1+1*29**0
#     s2=8*29**7+2*29**6+4*29**5+1*29**4+x*29**3+1*29**2+5*29**1+3*29**0
#     s=s1+s2
#     if s%28==0:
#         print(x,s/28)
