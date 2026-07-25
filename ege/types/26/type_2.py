# 2603

# data=[]
# with open("../files/2603.txt") as f:
#     N,S=map(int, f.readline().split())
#     for line in f:
#         parts=list(map(int,line.split()))
#         candidate={
#             "id":parts[0],
#             "result":parts[1]+parts[2]+parts[3],
#             "interview":parts[4]
#         }
#         data.append(candidate)
#
# data.sort(key=lambda x: (x["result"],x["interview"],x["id"]),reverse=True)
#
# half_pass_mark=data[S]["result"]
#
# answer1=0
# answer2=0
#
# for candidate in data:
#     if candidate["result"] > half_pass_mark:
#         answer1=candidate["id"]
#     if candidate["result"]==half_pass_mark:
#         answer2+=1
# print(answer1,answer2)

# 2604

# data=[]
# with open("files/2604.txt") as f:
#     N=int(f.readline())
#     for line in f:
#         parts=list(map(int,line.split()))
#         candidate={
#             "id": parts[0],
#             "m_1": parts[1],
#             "m_2": parts[2],
#             "m_3": parts[3],
#             "m_4": parts[4],
#         }
#         candidate["mean"]=sum(parts[1:]) / 4
#         candidate["twos"]=parts[1:].count(2)
#         data.append(candidate)
#
# data = sorted(data,key=lambda x: (-x["mean"],x["twos"],x["id"]))
#
# quart = N//4
#
#
# answer_1 = data[quart-1]["id"]
# answer_2=0
# for candidate in data:
#     if candidate["twos"]>2:
#         answer_2 = candidate["id"]
#         break
#
# print(answer_1,answer_2)
