###################2405
# with open("../files/2405.txt") as f:
#     data=f.readline()
# next_ch={
#     "K":"L",
#     "L":"M",
#     "M":"N",
#     "N":"K"
# }
# breaks=[0]
# max_len=0
# for i in range(len(data)-1):
#     if next_ch[data[i]] != data[i+1]:
#         breaks.append(i)
# for i in range(1,len(breaks)):
#     distance = breaks[i]-breaks[i-1]
#     max_len = max(max_len,distance)
# print(max_len)

######################################2429
# data="2AAAAAAA416BB87"
#
# evens="02468"
# breaks=[0]
# i=0
#
# while i<len(data)-1:
#     if data[i] in evens and data[i+1].isalpha():
#         j=i+1
#         breaks.append(i)
#
#         while j< len(data) and data[j]==data[i+1]:
#             j+=1
#         if data[j] in evens:
#             breaks.append(j)
#         i=j
#     else:
#         i+=1
#
# breaks.append(len(data)-1)
#
# for i in range(1,len(breaks)):
#     print(f"Блок 1 - {data[breaks[i-1]:breaks[i+1]]} начало: {breaks[i-1]} конец: {breaks[i]}")

################### 7272

# data="CBAAAABABCBAAABCBBA"
# pairs=["AB","CB"]
#
# breaks=[0]
#
# i=0
# while i<len(data)-1:
#     pair=data[i]+data[i+1]
#     if pair in pairs:
#         i+=2
#     else:
#         i+=1
#         breaks.append(i)
# breaks.append(len(data)-1)
#
# max_len=0
# print(breaks)
# for i in range(1,len(breaks)):
#     distance=breaks[i]-breaks[i-1]-1
#     max_len=max(max_len,distance)
# print(max_len//2)