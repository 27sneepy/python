######################################2405
# with open("../files/2405.txt") as f:
#     data=f.readline()
# # неправильно
# # data=data.replace("KLMN","*")
# # data=data.translate(str.maketrans('KLMN','    '))
# # data=data.split()
# # print(len(max(data,key=len)))
#
# # K -> L -> M -> N -> K
# next_ch={
#     "K":"L",
#     "L":"M",
#     "M":"N",
#     "N":"K"
# }
#
# cnt=1
# max_len=0
# for i in range(len(data)-1):
#     if next_ch[data[i]]==data[i+1]:
#         cnt+=1
#         max_len=max(max_len,cnt)
#     else:
#         cnt=1
# print(max_len)


######################################2429
# data="2AAAAAAA416BB87"
#
# max_len=0
# current=0
# evens="02468"
#
# for i in range(len(data)):
#     if data[i] in evens and data[i+1].isalpha():
#         j=i+1
#
#         while j< len(data) and data[j]==data[i+1]:
#             j+=1
#         if data[j] in evens:
#             lenght=j-i+1
#             max_len=max(lenght,max_len)
#         i=j
# print(max_len)

################### 7272

# data="CBAAAABABCBAAABCBBA"
# pairs=["AB","CB"]
# i=0
# counter=0
# max_len=0
# while i<len(data)-1:
#     pair=data[i]+data[i+1]
#     if pair in pairs:
#         counter+=1
#         i+=2
#     else:
#         counter=0
#         i+=1
#     max_len=max(counter,max_len)
# print(max_len)
