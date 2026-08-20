################### type 1

# data="ABCAABACACAB"
# data=data.replace("AB","A B")
# data=data.split()
# print(len(max(data,key=len)))
#
#
# data="0123456789012301234000123420123423"
# while "00" in data:
#     data=data.replace("00","0 0")
# data=data.split()
# print(len(max(data,key=len)))

# data="QRW1QR2RQWR44RQW1"
#
# # for i in "QRW":
# #     data=data.replace(i,"*")
# # for i in "124":
# #     data=data.replace(i,"0")
#
# data=data.translate(str.maketrans("QRW124","***000"))
#
# while "**" in data or "00" in data:
#     data=data.replace("**","* *")
#     data=data.replace("00","0 0")
# data=data.split()
# print(data)

################### 13866
# data="111AAAAA3333AAAA"
# data=data.translate(str.maketrans("13579","*****"))
# while "***" in data:
#     data=data.replace("***","** **")
#
# print(data.split())



