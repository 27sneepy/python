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