# from string import digits, ascii_uppercase
#
# data="XZ1234AZZ"
# alph=digits+ascii_uppercase
#
# good=alph[:16]
# cnt=max_len=0
# for i in range(len(data)):
#     if data[i] in good:
#         cnt+=1
#     else:
#         cnt=0
#     max_len=max(max_len,cnt)
# print(max_len)

################### 22359
# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.
# from string import digits,ascii_uppercase
# with open("../files/22359.txt") as f:
#     data=f.readline()
# alpha=digits+ascii_uppercase
# good=alpha[:15]
# bad=alpha[15:]
# even=good[::5]
# string=""
# max_len=index=0
#
# for i in range(len(data)):
#     if string=="" and data[i]=="0":
#         continue
#     if data[i] in good:
#         string+=data[i]
#     else:
#         string=""
#     if data[i] in even and max_len<int(string,15):
#         max_len=int(string,15)
#         index=i
# print(index)