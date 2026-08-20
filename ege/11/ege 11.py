# from math import *
# i=ceil(log2(1710))
# idn=ceil(i*252/8)
# a=ceil(4096*idn/1024)
# print(a)

# from math import *
# a=10+999
# i=ceil(log2(a))
# idn = ceil(i * 745 / 8)
# b=312*idn
# perone=(311*1024)/312
# extra=(perone-idn)*312
# print(extra)

# from math import *
# alphabet = 520
# bits = ceil(log2(alphabet))
# id_bytes = ceil(99 * bits / 8)
# total_bytes = 543 * 1024
# users = 4322
# per_user = total_bytes // users +1
# extra_all = (per_user - id_bytes)
# print(extra_all)


# from math import *
# for i in range(1,1000):
#     bit=ceil(log2(i))
#     idn=ceil(261*bit/8)
#     if 252500 * idn >31*1024*1024:
#         print(i)
#         break


# #мощность алфавита
# from math import *
# for x in range(1,10000):
#     i=ceil(log2(x))
#     idn=ceil(80*i/8)
#     if 1200*idn<=150*1024:
#         print(x)

# from math import *
# a=25+487
# i=ceil(log2(a))
# for ln in range(1,9999):
#     idn=ceil(ln*i/8)
#     if 345*idn>70*2**10:
#         print(ln)
#         break

# from math import *
# ln=15
# a=10+11*2
# i=ceil(log2(a))
# idn=ceil(ln*i/8)
# print(idn*30)

# from math import *
# ln=115
# a=1030
# i=ceil(log2(a))
# idn=ceil(ln*i/8)
# print(idn*16384/1024)

# from math import *
# ln=196
# a=10+1550
# i=ceil(log2(a))
# idn=ceil(i*ln/8)
# print(idn*65536/1024)


# from math import *
# ln=23
# for a in range(1,100000):
#     i=ceil(log2(a))
#     idn=ceil(i*ln/8)
#     if (3222444*idn)>=(45*1024*1024):
#         print(a)
#         break

# from math import *
# ln=16
# a=62
# i=ceil(log2(a))
# dop=20
# idn=ceil(i*ln/8)+dop
# print(10240/idn)

from math import *
ln=163
for a in range(1,99999):
    i=ceil(log2(a))
    idn=ceil(i*ln/8)
    if 32768*idn==3264*2**10:
        print(a)
        break