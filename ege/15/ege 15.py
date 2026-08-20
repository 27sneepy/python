# 1
# def f(x,y):
#     return (x-3*y<a) or (y>400) or (x>56)
# for a in range(1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break

# 2
# def f(x):
#     return (x%a!=0) <= ((x%28==0) <= (x%49!=0))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break


# 3
# def f(x):
#     return ((x&673!=0) or (x&189!=0)) <= (x&a!=0)
# for a in range(1,1000):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break

# 4 (отрезки)
# ОТРЕЗОК ВСЕГДА МЕЖДУ ТОЧКАМИ ИЗ УСЛОВИЯ
# ЕСЛИ ПРОСЯТ МИН ОТРЕЗОК - НАЧИНАЕМ С ПУСТОГО
# ЕСЛИ ПРОСЯТ МАКС ОТРЕЗОК - НАЧИНАЕМ С ПОЛНОГО

# p=list(range(25,65))
# q=list(range(40,116))
# a=[]
# for x in range(200):
#     if not((x in p) <= (((x in q) and (x not in a)) <= (x not in p))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# 5
# p=list(range(66,68))
# o=list(range(32,126))
# t=list(range(30,492))
# a=[]
# for x in range(1000):
#     if not((x in a) or ((x in p) or (x not in o) or (x not in t))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# 6
# b=list(range(25,41))
# c=list(range(12,34))
# a=[]
# for x in range(100):
#     if not(((x in b) <= (x in a)) and ((x not in c) or (x in a))):
#         a.append(x)
# print(a)
# print(a[-1]-a[0])

# 7
# d=list(range(133,178))
# b=list(range(144,191))
# a=[]
# for x in range(300):
#     if not((x in d)<=(((x not in b) and (x not in a))<=(x not in d))):
#         a.append(x)
# print(a)
# print(a[-1]-a[0])
# 11

# 8
# c=list(range(48,95))
# j=list(range(83,101))
# a=list(range(200))    # должны совпасть с for x in....
# for x in range(200):
#     if not(     (not((x in c) or (x in j)))<=(x not in a)       ):
#         a.remove(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# 9
# p=list(range(15,34))
# q=list(range(35,49))
# a=list(range(200))
# for x in range(200):
#     if not(     ((x in a) and (x not in q))<=((x in p) or (x in q))      ):
#         a.remove(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])
# нельзя брать потому что 34 не должно входить
# либо 33-15=18 либо 48-35=13
# 18


# 10
# b=list(range(36,76))
# c=list(range(60,111))
# a=[]
# for x in range(200):
#     if not((x not in a)<=((x in b)==(x in c))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# 11
# p={3,6,9,12}
# q={1,2,3,4,5,6}
# a=set()
# for x in range(200):
#     if not((not((x not in a) and (x in p))) or (x not in q)):
#         a.add(x)
# print(a)

# конец веба






# варианты


# def f(x):
#     return (x%128==0)<=((x%a!=0) <=(x%80!=0))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break


# def f(x):
#     return ((x%34==0) and (x%51!=0))<=((x%a!=0)or (x%51==0))
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

#
# def f(x):
#     return (70%a==0) and ((x%a!=0)<=((x%18==0)<=(x%42!=0)))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break


# b=list(range(60,81))
# def f(x):
#     return (x%a==0) or ((x in b)<=(x%22!=0))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

# def f(x,y):
#     return (x*y>a) or (x>y) or (74>x)
# for a in range(6000,-1,-1):
#     if all(f(x,y) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# def f(x,y):
#     return ((x**2>16)or(a>x))and((y**2<=81)or(a<=y))
# k=0
# for a in range(-1000,1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         k+=1
# print(k)

# def f(x,y):
#     return ((x*y>a) and (x>y) and (x<8))==False
# for a in range(-10000,10000):
#     if all(f(x,y) for x in range(1,10000) for y in range(1,10000)):
#         print(a)
#         break

# def f(x):
#     return ((not ((x%263==0)<=(x%a==0)))and (x%71==0))==False
# for a in range(20000,0,-1):
#     if all(f(x) for x in range(1,20000)):
#         print(a)
#         break

# def f(x):
#     return (a%12==0)and((530%x==0)<=((a%x!=0)<=(170%x!=0)))
# k=0
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         k+=1
# print(k)

#
# def f(x):
#     return ((x&112!=0)or(x&86!=0))<=((x&65==0)<=(x&a!=0))
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

# def f(x,y):
#     return (7*y + 5*x < 1000) or (x < y) or (a < x)
# for a in range(1000,0,-1):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break


# p=list(range(5,55))
# q=list(range(50,94))
# def f(x):
#     return ((x not in p)and (x in q))<=(x>a)
# for a in range(1,100):
#     k=0
#     if all(f(x) for x in range(1,1000)):
#         if k==20:
#             print(a)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# def f(x):
#     return (a%5==0) and ((2020%a!=0) <=((x%1718==0)<=(2023%a==0)))
# for a in range(1,10000):
#     if all(f(x) for x in range(1,10000)):
#         print(a)


# def f(x):
#     return ((((a+x+37+45)==180)and (a>0) and (x+45>0)) == (((a+x+90)==180) and (a>0) and (x>0))) and (not(a+23<120))
# for a in range(1,1000,):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break
#
# b=list(range(25,41))
# c=list(range(12,34))
# a=[]
# for x in range(200):
#     if not(((x in b)<=(x in a))and((x not in c)or(x in a))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# from math import *
# p={1,3,4,9,11,13,15,17,19,21}
# q={3,6,9,12,15,18,21,24,27,30}
# a=set()
# for x in range(1,100):
#     if not (((x in p)<=(x in a))or((x not in a)<=(x not in q))):
#         a.add(x)
# print(prod(a))

# def f(x):
#     return (x%128==0)<=((x%a!=0)<=(x%80!=0))
# for a in range(1000,0,-1):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break

# p=list(range(25,65))
# q=list(range(40,116))
# a=[]
# for x in range(1,1000):
#     if not ((x in p)<=(((x in q)and(x not in a))<=(x not in p))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# def f(x):
#     return ((x&117!=0) and (x&91==0)) <= (x&a!=0)
# for a in range(0,1000):
#     if all(f(x) for x in range(0,1000)):
#         print(a)
#         break


# p=list(range(52,106))
# q=list(range(0,54))
# a=[]
# for x in range(1000):
#     if not (((x not in p)and(x not in q)and(x not in a))<=(x**2>303601)):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# def f(x):
#     return (a+2*x>400-a)and((a%100)+(120%a)>140)
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)
#         break


# !!!!!
# def f(x, y):
#     return (4*x + y > 115) or (x > 3*y) or (x + 4*y < a)
# for a in range(1000, -1, -1):
#     if any(not f(x, y) for x in range(1000) for y in range(1000)):
#         print(a)
#         break