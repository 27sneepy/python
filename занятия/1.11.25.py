#28
# a=input()
# if a.isupper()==True:
#     print("соситоит из заглавных")
# if a.islower()==True:
#     print("состоит из прописных")
# if a.istitle()==True:
#     print('заголовок')
#30
# a=input()
# if a.isalpha()==False:
#     print(a.upper())
# if a.isalnum()==False:
#     print(a.replace(" ","*"))
# else:
#     print(a)
#32
# j=input()
# a="aoiuyeAOIUYE"
# maxim=0
# alpha=""
# for x in a:
#     nex_maxim =j.rfind(x)
#     if maxim<nex_maxim:
#         maxim=nex_maxim
#         alpha=x
# print(maxim,alpha)
#31
# s="abcd defg ghij"
# s=s.replace(" ","")
# for i in s:
#     if s.count(i) > 1 :
#         s=s.replace(i,"")
# print(s)
#20
# from random import choice
# #choice - случайный эл-т последовательности
# s="hello world!"
# k=[" ", ",", ".","!","?"]
# while s:
#     a=choice(s)
#     if a in k:
#         continue
#     s=s.replace(a, "")
#     print("удалили букву", a,":",s)
#19
a=input() #M000MM
k="ABEKMHOPCTYX"
if len(a)==6:
    numbers=a[1:4]
    alpha=a[0]+a[4:]
    print(numbers.isdigit() and alpha[0] in k and alpha[1] in k and alpha[2] in k)
else:
    print(False)

