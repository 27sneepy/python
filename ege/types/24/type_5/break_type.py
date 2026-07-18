# 2427
# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле последовательность
# из максимального количества идущих подряд символов, среди которых ровно
# 35 букв S, начинающуюся чётной цифрой, не содержащую других чётных
# цифр, кроме первой.

# data="4SS48SOS"
# even="02468"
# breaks=[i for i in range(len(data)) if data[i] in even]
# k=2
# max_len=0
# breaks.append(len(data))
# for i in range(len(breaks)-1):
#     start=breaks[i]
#     end=breaks[i+1]
#     cnt_s=0
#     for j in range(start,end):
#         if data[j] =="S":
#             cnt_s+=1
#         if cnt_s == k:
#             max_len=max(max_len,j-start+1)
# print(max_len)


# 26549
# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# оканчивающихся подстрокой 2025, среди которых буква Y встречается не менее 140 раз,
# а подстрока 2025 содержится ровно 50 раз.
# data="2025QQQQQYQQQYQQQY2025"
# breaks=[0]
# k=2
# y=2
# max_len=0
# for i in range(len(data)):
#     if data[i:i+4] == "2025":
#         breaks.append(i+3)
#
# for i in range(len(breaks)-k):
#     start=breaks[i]
#     end=breaks[i+k]+1
#     srez=breaks[i:i+k+1]
#     stroka=data[srez[0]:srez[-1]+1]
#
#     cnt_y=stroka.count("Y")
#     if cnt_y >= y:
#         max_len=max(max_len,end-start+1)
# print(max_len)

# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле минимальное
# количество идущих подряд символов, среди которых подстрока 2025
# встречается не менее 110 раз и при этом содержится ровно 90 букв W.
data="AAW2025WAAAA2025WY2025WAAAY"
breaks=[-1]
k=2
y=2
min_len = 10**9
for i in range(len(data)):
    if data[i] == "W":
        breaks.append(i)
breaks.append(len(data))
print(breaks)
for i in range(len(breaks)-k-1):
    start=breaks[i]
    end=breaks[i+k+1]
    stroka=data[start+1:end]
    print(stroka)
    cnt_2025=stroka.count("2025")
    if cnt_2025 >= y:
        min_len = min(min_len, end - start - 1)
print(min_len)