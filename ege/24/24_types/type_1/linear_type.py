# data="QRW1Q112424QQQ1"
# data=data.translate(str.maketrans("QRW124","***000"))
# counter=1
# max_len=0
# for i in range(len(data)-1):
#     if data[i]!=data[i+1]:
#         counter+=1
#         max_len=max(max_len,counter)
#     else:
#         counter=1
# print(max_len)

################### 13866
# data="111AAAAA3333AAAA"
# data=data.translate(str.maketrans("13579","*****"))
#
# counter=2
# max_len=0
#
# for i in range(len(data)-2):
#     counter+=1
#     if data[i]==data[i+1]==data[i+2]=="*":
#         counter=2
#     max_len=max(max_len,counter)
# print(max_len)

