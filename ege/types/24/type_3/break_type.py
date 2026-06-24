################### 2422
# from string import digits,ascii_uppercase
# data="XX01345A1XX"
# alpha=digits+ascii_uppercase
#
# good=alpha[:12]
# bad=alpha[12:]
# even=good[::2]
#
# breaks=[0]
# max_len=0
#
# for i in range(len(data)):
#     if data[i] in bad:
#         breaks.append(i)
#
# breaks.append(len(data))
#
# for i in range(len(breaks)-1):
#     part=data[breaks[i]+1:breaks[i+1]]
#     while part and part[0]=='0':
#         part=part[1:]
#     while part and part[-1] not in even:
#         part=part[:-1]
#     max_len=max(max_len,len(part))
# print(max_len)

################### 22359
# from string import digits, ascii_uppercase
#
#
# alpha = digits + ascii_uppercase
#
# good = alpha[:15]
# bad = alpha[15:]
# even = good[::5]
#
# data = "LOCIZQT00795CCAELL"
# # with open("22359.txt") as f:
# #     data = f.readline()
#
#
# breaks = [0]
#
# for i in range(len(data)):
#     if data[i] in bad:
#         breaks.append(i)
#
# breaks.append(len(data))
#
# candidates = []
# for i in range(1,len(breaks)):
#     left = breaks[i - 1] + 1
#     right = breaks[i]
#     part = data[left:right]
#
#     while part and part[0] == "0":
#         part = part[1:]
#
#     for j in range(len(part)-1,-1,-1):
#         if part[j] in even:
#             number = part[:j+1]
#             end_index = right - (len(part) - j)
#             candidates.append((number, end_index))
# ans = max(candidates, key = lambda x: int(x[0], 15))
# print(ans)