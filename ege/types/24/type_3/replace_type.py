# from string import printable
#
# data="XZ1234AZZ"
# alph=printable[:16].upper()
#
# for i in alph:
#     data=data.replace(i, "*")
#
# for i in printable[16:37].upper():
#     data=data.replace(i, " ")
# data=data.split()
# max_len=len(max(data,key=len))
# print(max_len)


################### 2422
# Текстовый файл состоит из символов, обозначающих десятичные цифры и заглавные
# буквы латинского алфавита. Определите в прилагаемом файле максимальное количество
# идущих подряд символов, которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.
# from string import digits,ascii_uppercase
# data="XX01345A1XX"
# alpha=digits+ascii_uppercase
#
# good=alpha[:12]
# bad=alpha[12:]
# even=good[::2]
# max_len=0
# for i in bad:
#     data=data.replace(i," ")
# data=data.split()
# for i in data:
#     part=i
#     while part and part[0]=='0':
#         part=part[1:]
#     while part and part[-1] not in even:
#         part=part[:-1]
#     max_len=max(max_len,len(part))
# print(max_len)


