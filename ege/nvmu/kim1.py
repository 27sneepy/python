# kim 1
# 1 76
# 2 x y w z
# 3 458
# 4 41
# 7 4
# 8 612
# 9 4387928
# 10 5
# 11 8193
# 14 1989
# 15 92
# 18 1235 3664
# 22 10

# 2
# from itertools import *
# def f(w,x,z,y):
#     return y and (((not w)or z)==x)
# for a1,a2,a3,a4,a5 in product([0,1],repeat=5):
#     t=[(a1,a2,0,0),
#        (a3,1,1,1),
#        (0,a4,a5,0)]
#     if len(t)==len(set(t)):
#         for p in permutations("wxzy"):
#             if [f(**dict(zip(p,r))) for r in t]==[1,0,1]:
#                 print(*p)

# 8
# from itertools import *
# k=0
# even="02468A"
# for i in product("0123456789AB",repeat=5):
#     s="".join(i)
#     s=s.replace("0","Ч").replace("2","Ч").replace("4","Ч").replace("6","Ч").replace("8","Ч").replace("A","Ч")
#     evens=[c for c in "".join(i) if c in even]
#     if len(set(evens))==1 and "0" not in "".join(i)[0]:
#         if s.count("Ч")==3 and "ЧЧЧ" in s:
#             k+=1
# print(k)

# 9
# from math import *
# k=0
# c=0
# with open("9.txt") as f:
#     for i in f:
#         a=list(map(int, i.split()))
#         k+=1
#         sr=sum(a)/len(a)
#         s=[x for x in a if x==(int(sr))]
#         q=[x for x in a if sqrt(x)==int(sqrt(x))]
#         if k%2==0:
#             if len(s)>0:
#                 if len(q)>0:
#                     c+=k
# print(c)

# 11
# from math import *
# ln=27
# for a in range(1,10000):
#     i=ceil(log2(a))
#     idn=ceil(ln*i/8)
#     if 3000000*idn>=126*1024*1024:
#         print(a)
#         break

# 14
# for x in range(2001):
#     a=12*13**12+11*13**7-x
#     b=[]
#     while a>0:
#         b.append(a%13)
#         a=a//13
#     if b.count(0)%2!=0:
#         print(x)

# 15
# def f(x):
#     return (x%a==0) or ((x in b)<=((x%36!=0)or(x+a<=272)))
# b=list(range(120,211))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break




# kim 2
# 1 47
# 2 z w x y
# 3 693
# 4 44
# 7 8
# 8 576
# 9 1412219
# 10 13
# 11 32769
# 14 1995
# 15 101
# 18 1139 3664
# 22 8























