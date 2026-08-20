from re import *
with open("../../files/24_17563.txt") as f:
    data = f.readline()
# data="-8*7007**8**0-9**7--90*9708897-*0008-*-990"
data = data.replace("-","*")
data = data.replace("**","  ")

for i in "89":
    data=data.replace(i,"7")

data = data.replace("*0","  ")
while " 0" in data: data = data.replace(" 0","  ")

data=data.split()

# data_1=[]
# for i in data:
#     i = i.strip("*")
#     data_1.append(i)
#
# print(data_1)
# print(len(max(data_1, key = len)))

print(len(max(data, key = lambda x: len(x.strip("*"))).strip("*")))