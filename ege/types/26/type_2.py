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


# 2619
# times = []
#
# with open("files/2619.txt") as f:
#     n = int(f.readline())
#     for i in range(1, n + 1):
#         sh, o = map(int, f.readline().split())
#         times.append((sh, i, "SH"))
#         times.append((o, i, "O"))
#
# times=sorted(times)
#
# belt=[0]*n
# left=0
# right=n-1
#
# last_detail = 0
# count_before = 0
#
# used=set()
# for time, num, sho in times:
#     if num in used:
#         continue
#     used.add(num)
#     if sho == "SH":
#         belt[left] = num
#         left += 1
#     else:
#         belt[right]=num
#         right-=1
#     last_detail=num
#     count_before=left
# print(last_detail,count_before)

# 2608
# data=[]
# with open("files/2608.txt") as f:
#     num=int(f.readline())
#     for line in f:
#         string=list(map(int,line.split()))
#         product={
#             "item_num":string[0],
#             "price":string[1],
#             "status":string[2]
#         }
#         data.append(product)
#
# avg_price=sum(item["price"] for item in data)/len(data)
#
# exp_products = []
#
# for item in data:
#     if item["price"] > avg_price:
#         exp_products.append(item)
#
# products={}
#
# for item in exp_products:
#     item_num=item["item_num"]
#
#     if item_num not in products:
#         products[item_num]={
#             "price": item["price"],
#             "sold": 0,
#             "left": 0
#         }
#     if item["status"] == 0:
#         products[item_num]["sold"] += 1
#     else:
#         products[item_num]["left"] += 1
#
# leader=max(products.values(),key= lambda x: (x["sold"], x["price"], -x["left"]))
#
# revenue=leader["price"]*leader["sold"]
#
# print(revenue,leader["left"])

# 2609
# data=[]
# with open("files/2609.txt") as f:
#     num=int(f.readline())
#     for line in f:
#         data.append(list(map(int,line.split())))
#
# data = sorted(data, key=lambda x: (x[1],-x[0]))
#
# approved=[data[0]]
# for event in data[1:]:
#     if approved[-1][1]<=event[0]:
#         approved.append(event)
#
# longest_break=0
# for event in data:
#     if approved[-2][1] <= event[0]:
#         longest_break= max(longest_break,event[0]-approved[-2][1])
#
# print(len(approved),longest_break)

# 2620

# data=[]
# with open("files/2620.txt") as f:
#     windows_num=int(f.readline())
#     request_num=int(f.readline())
#     for line in f:
#         data.append(list(map(int, line.split())))
#
# data=sorted(data)
#
# ending_windows=[0]*windows_num
# clients=0
# last_window=0
#
# for start,end in data:
#     for i in range(windows_num):
#         if ending_windows[i]<start:
#             ending_windows[i]=end
#             clients += 1
#             last_window = i + 1
#             break
# print(clients,last_window)

# 2610

# data=[]
# with open("files/2610.txt") as f:
#     num=int(f.readline())
#     for line in f:
#         start,time=list(map(int,line.split()))
#         data.append([start,start+time])
#
# data = sorted(data, key=lambda x: (x[1],-x[0]))
#
# approved=[data[0]]
# for event in data[1:]:
#     if approved[-1][1]<=event[0]:
#         approved.append(event)
#
# longest_break=0
# for event in data:
#     if approved[-2][1] <= event[0]:
#         longest_break= max(longest_break,event[0]-approved[-2][1])
#
# print(len(approved),longest_break)