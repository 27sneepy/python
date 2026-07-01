# height = [166,187,198,178,181,188,197,182,172,201]
#
# height.sort()
#
# left = 0
# right = len(height) - 1
#
# target = 370
#
# while left < right:
#     current_sum = height[left] + height[right]
#     print(f"левый {height[left] } правый {height[right]}")
#     if target == current_sum:
#         print("Найдены значения:",height[left] , height[right])
#         break
#     if current_sum < target:
#         left += 1
#         print("Сумма меньше\t смещение левого\n")
#     else:
#         right -= 1
#         print("Сумма больше\t смещение правого\n")


# data="abbacadbada"
# left=0
# used=set()
# max_len=0
#
# for right in range(len(data)):
#     while data[right] in used:
#         used.remove(data[left])
#         left+=1
#     used.add(data[right])
#     current_len= right - left + 1
#     if current_len > max_len:
#         max_len=current_len
# print(max_len)


# data="abbacadbada"
# left=0
# last={}
# max_len=0
#
# for right in range(len(data)):
#     if data[right] in last and last[data[right]] >= left:
#         left = last[data[right]] + 1
#
#     last[data[right]] = right
#     max_len = max(max_len, right - left + 1)
#
# print(max_len)



###################### 2404

# data="TTTTUUUTUTTUTTT"
#
# left=0
# cnt=0
# max_len=0
# k=5
#
# for right in range(len(data)):
#     if data[right]=="T":
#         cnt+=1
#     while cnt>k:
#         if data[left]=="T":
#             cnt-=1
#         left+=1
#     if cnt==k:
#         max_len=max(max_len,right-left+1)
# print(max_len)

###################### 2425

# with open("../files/2425.txt") as f:
#     data=f.readline()
# left=0
# cnt=0
# max_len=0
# k=3
#
# for right in range(len(data)):
#     if data[right]=="A":
#         cnt+=1
#     while cnt>k:
#         if data[left]=="A":
#             cnt-=1
#         left+=1
#     if cnt<=k:
#         max_len=max(max_len,right-left+1)
# print(max_len)
