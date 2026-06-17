###################2405
# with open("../files/2405.txt") as f:
#     data=f.readline()
# next_ch={
#     "K":"L",
#     "L":"M",
#     "M":"N",
#     "N":"K"
# }
# left=0
# max_len=0
# for right in range(len(data)-1):
#     if next_ch[data[right]]!=data[right+1]:
#         left=right
#     lenght = right - left +1
#     max_len=max(lenght,max_len)
# print(max_len)

################### 7272

# data="CBAAAABABCBAAABCBBA"
# pairs=["AB","CB"]
# left=right=0
# max_len=0
#
# while right<len(data)-1:
#     pair= data[right]+data[right+1]
#     if pair in pairs:
#         lenght=(right-left)//2 + 1
#         max_len=max(max_len,lenght)
#         right+=2
#     else:
#         left=right
#         right+=1
# print(max_len)
