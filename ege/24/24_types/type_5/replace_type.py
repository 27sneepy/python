# Текстовый файл состоит из десятичных цифр и заглавных букв
# латинского алфавита. Определите в прилагаемом файле
# последовательность из максимального количества идущих
# подряд символов, среди которых ровно 35 нечётных цифр
# и при этом начинающуюся с буквы S, не содержащую других
# букв S, кроме первой.

# data = "DSFS23543132S555"
# k = 5
# max_len=0
#
# data= data.translate(str.maketrans("13579","*****"))
#
# data = data.replace("S", " S")
#
# for seq in data.split():
#     print(seq)
#     # pos=[i for i,c in enumerate(seq) if c=="*"]
#     # print(pos)
#     # if len(pos)>=k:
#     #     max_len=max(max_len, pos[k] if len(pos)>k else len(seq))
#     cnt=seq.count("*")
#     while cnt-1>=k:
#         if seq[-1] == "*":
#             cnt-=1
#         seq=seq[:-1]
#     if cnt==5:
#         max_len=max(max_len,len(seq))
# print(max_len)