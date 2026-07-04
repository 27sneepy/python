###################### 2404

# data="TTTTUUUTUTTUTTT"
#
# parts=data.split("T")
# print(parts)

###################### 2403
# data = "CDCDDCCDDCCDCDCDCD"
# cnt = max_len = 0
# k = 3
#
# data=data.replace("CD","C D").split()
# for i in range(len(data)-k):
#     substring = len("".join(data[i:i+k+1]))
#     max_len = max(max_len, substring)
# print(max_len)

###################### 2407
with open("../files/2407.txt") as f:
    data=f.readline()
cnt = max_len = 0
k = 80

data=data.replace("FSRQ","FSR Q").split()
for i in range(len(data)-k):
    substring = len("".join(data[i:i+k+1]))
    max_len = max(max_len, substring)
print(max_len)