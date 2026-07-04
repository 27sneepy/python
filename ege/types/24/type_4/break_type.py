###################### 2404

# data="TTTTUUUTUTTUTTT"
#
# breaks=[-1]
# k=5
# max_len=0
#
# for i in range(len(data)):
#     if data[i]=="T":
#         breaks.append(i)
#
# breaks.append(len(data))
# for i in range(1,len(breaks)-k):
#     right = breaks[i+k]
#     left = breaks[i-1]
#     max_len = max(max_len, right-left-1)
# print(max_len)


###################### 2425

# with open("../files/2425.txt") as f:
#     data=f.readline()
#
# breaks=[-1]
# k=3
# max_len=0
#
# for i in range(len(data)):
#     if data[i]=="A":
#         breaks.append(i)
#
# breaks.append(len(data))
# for i in range(1,len(breaks)-k):
#     right = breaks[i+k]
#     left = breaks[i-1]
#     max_len = max(max_len, right-left-1)
# print(max_len)


###################### 2403
data = "CDCDDCCDDCCDCDCDCD"

breaks=[-1]
k=3
max_len=0

for i in range(len(data)-1):
    if data[i]+data[i+1]=="CD":
        breaks.append(i)

breaks.append(len(data)-1)
for i in range(len(breaks)-k-1):
    right = breaks[i+k+1]
    left = breaks[i]
    max_len = max(max_len, right-left)
print(max_len)
