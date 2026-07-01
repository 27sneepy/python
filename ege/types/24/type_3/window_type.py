################### 2422
# from string import digits,ascii_uppercase
# data="XX01345A1XX"
# alpha=digits+ascii_uppercase
#
# good=alpha[:12]
# bad=alpha[12:]
# even=good[::2]
# left=0
# max_len=0
#
# for right in range(len(data)):
#     if data[right] in bad:
#         left = right + 1
#     else:
#         if data[left]=='0':
#             left+=1
#         if data[right] in even:
#             max_len=max(right - left + 1,max_len)
# print(max_len)

################### 22359
# from string import digits,ascii_uppercase
# data="LOCIZQT00795CCAELL"
# alpha=digits+ascii_uppercase
# good=alpha[:15]
# bad=alpha[15:]
# even=good[::5]
# left=0
# substrings=[]
#
# for right in range(len(data)):
#     if data[right] in bad:
#         left=right+1
#         continue
#     while data[left]=="0":
#         left+=1
#     if data[right] in even:
#         substring=data[left:right+1]
#         if substring:
#             substrings.append((substring,right))
#
# ans=max(substrings,key = lambda x: int(x[0],15))
# print(ans)

################### 2424
# from string import digits,ascii_uppercase
# data = "LOCIZQT00795CCAELL"
# alpha=digits+ascii_uppercase
# good=alpha[:14]
# bad=alpha[14:]
# even=good[::2]
# left=0
# substrings=[]
#
# for right in range(len(data)):
#     if data[right] in bad:
#         left=right+1
#         continue
#     while data[left]=="0":
#         left+=1
#     if data[right] in even:
#         substring=data[left:right+1]
#         if substring:
#             substrings.append((substring,right))
#
# ans=max(substrings,key = lambda x: int(x[0],14))
# print(len(str(ans[0])))


################### 22356
# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Onределите в этом файле последовательность идущих подряд символов, представляющих
# собой запись максимального нечётного 12-ричного числа. В ответе запишите индекс
# (номер) первого символа (первой значащей цифры), с которого начинается запись
# этого числа в прилагаемом файле. Нумерация символов в текстовом файле начинается с нуля.

# from string import digits,ascii_uppercase
# data = "LOCIZQT00795CCAELL"
# alpha=digits+ascii_uppercase
# good=alpha[:12]
# bad=alpha[12:]
# noteven=good[1::2]
# left=0
# substrings=[]
#
# for right in range(len(data)):
#     if data[right] in bad:
#         left=right+1
#         continue
#     while data[left]=="0":
#         left+=1
#     if data[right] in noteven:
#         substring=data[left:right+1]
#         if substring:
#             substrings.append((substring,left))
#
# ans=max(substrings,key = lambda x: int(x[0],12))
# print(ans[1])

