# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле
# последовательность из максимального количества идущих
# подряд символов, среди которых ровно 35 нечётных цифр
# и при этом начинающуюся с буквы S, не содержащую других
# букв S, кроме первой.

# data = "DSFS23543132S555"
# k = 5
# odds = "13579"
# max_len = left = cnt_s = cnt_odds = 0
# for right in range(len(data)):
#     if data[right] == "S":
#         cnt_s+=1
#     if data[right] in odds:
#         cnt_odds+=1
#
#     while cnt_s>1 or cnt_odds>k:
#         if data[left] == "S":
#             cnt_s-=1
#         if data[left] in odds:
#             cnt_odds-=1
#         left+=1
#     while left<=right and data[left] != "S":
#         if data[left] in odds:
#             cnt_odds-=1
#         left+=1
#     if cnt_s==1 and cnt_odds==k and data[left] == "S":
#         print(data[left:right],right-left+1)
#         max_len = max(max_len,right-left+1)

# 2427
# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле последовательность
# из максимального количества идущих подряд символов, среди которых ровно
# 35 букв S, начинающуюся чётной цифрой, не содержащую других
# чётных цифр, кроме первой.

# data = "QQQQQ4SSSS3333S"
# k = 5
# even = "02468"
# max_len = left = cnt_s = cnt_even = 0
# for right in range(len(data)):
#     if data[right] in even:
#         cnt_even+=1
#     if data[right] == "S":
#         cnt_s+=1
#
#     while cnt_even>1 or cnt_s>k:
#         if data[left] in even:
#             cnt_even-=1
#         if data[left] == "S":
#             cnt_s-=1
#         left+=1
#     while left<=right and data[left] not in even:
#         if data[left] == "S":
#             cnt_s-=1
#         left+=1
#     if cnt_even==1 and cnt_s==k and data[left] in even:
#         print(data[left:right+1],right-left+1)
#         max_len = max(max_len,right-left+1)


# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле минимальное
# количество идущих подряд символов, среди которых подстрока 2025
# встречается не менее 110 раз и при этом содержится ровно 90 букв W.

# data="AA2025WWAAAWWA2025AWAWWWAW"
# with open("../files/2433.txt") as f:
#     data=f.readline()
# left=cnt_w=cnt_2025=0
# min_len=10**9
#
# for right in range(len(data)):
#     if data[right]=="W":
#         cnt_w+=1
#     if right>=3 and data[right-3:right+1]=="2025":
#         cnt_2025+=1
#     while cnt_w > 90:
#         if data[left]=="W":
#             cnt_w-=1
#         if left<=right-3 and data[left:left+4]=="2025":
#             cnt_2025-=1
#         left+=1
#     if cnt_w==90 and cnt_2025>=110:
#         while cnt_w==90 and cnt_2025>=110:
#             min_len=min(min_len,right-left+1)
#             if data[left]=="W":
#                 break
#             if data[left:left+4]=="2025"and left<=right-3:
#                 cnt_2025-=1
#             left+=1
# print(min_len)

# 26549
# data="2025YY2025YY2025"
# data=open("../files/26549.txt").readline()
# y=140
# n=50
# left=cnt_y=cnt_2025=0
# max_len=0
#
# for right in range(len(data)):
#     if data[right]=="Y":
#         cnt_y+=1
#     if right >= 3 and data[right - 3:right + 1] == "2025":
#         cnt_2025+=1
#     while cnt_2025>n:
#         if left<=right-3 and data[left:left+4]=="2025":
#             cnt_2025-=1
#         if data[left]=="Y":
#             cnt_y-=1
#         left+=1
#     if cnt_y>=y and cnt_2025==n and data[right-3:right+1]=="2025":
#         max_len=max(max_len,right-left+1)
# print(max_len)