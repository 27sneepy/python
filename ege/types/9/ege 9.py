# with open("9.txt","r") as f:
#     k=0
#     for line in f:
#         a=sorted([int(x) for x in line.split()])
#         if (a[0]+a[2])/2<=a[1]:
#             k=k+1
#             print(k)
# with open("9.txt") as f:
#     k = 0
#     for line in f:
#         a = sorted(map(int, line.split()))
#         cond2 = False
#         for x in a:
#             if a.count(x) == 3 and len(set(a)) == 4:
#                 cond2 = True
#         cond1 = (a[0] + a[5]) ** 2 > sum(x * x for x in a[1:5])
#         if cond1 or cond2:
#             k += 1
# print(k)
from xml.dom.minidom import ProcessingInstruction

# with open("9.txt","r") as f:
#     k=0
#     for line in f:
#         a=sorted(map(int,line.split()))
#         summ = 0
#         isFirst = False
#         pov = 0
#         for x in a:
#             if a.count(x) == 3 and len(set(a)) == 5:
#                 pov = x
#                 isFirst = True
#             if a.count(x) < 3:
#                 summ += x
#         isSecond = (summ / 4) <= pov
#         if isFirst and isSecond:
#             k += 1
# print(k)

# with open("9.txt", "r") as f:
#     k=0
#     for line in f:
#         a=sorted(map(int, line.split()))
#         if len(set(a))==5 and 2*(a[0]+a[4])<=3*(a[1]+a[2]+a[3]):
#             k+=1
#         print(k)


# В каждой строке электронной таблицы записаны шесть целых чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# в строке есть как повторяющиеся, так и неповторяющиеся числа;
#
# среднее арифметическое всех неповторяющихся чисел строки меньше, чем среднее арифметическое всех повторяющихся чисел этой строки.
#
# При вычислении средних значений каждое число учитывается столько раз, сколько оно встречается в строке.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
#
# with open("9.txt") as f:
#     k = 0
#     for line in f:
#         a = list(map(int, line.split()))
#         rep = []  # повторяющиеся числа
#         uniq = []  # неповторяющиеся числа
#         for x in a:
#             if a.count(x) > 1:
#                 rep.append(x)
#             else:
#                 uniq.append(x)
#         # в строке должны быть И повторяющиеся, И неповторяющиеся
#         if len(rep) > 0 and len(uniq) > 0:
#             if sum(uniq) / len(uniq) < sum(rep) / len(rep):
#                 k += 1
# print(k)



# with open("92.txt") as f:
#     k = 0
#     for line in f:
#         a = list(map(int, line.split()))
#         k += 1
#         povt = [x for x in a if a.count(x) == 3]
#         nepovt = [x for x in a if a.count(x) == 1]
#
#         if len(set(povt)) == 1 and len(nepovt) == 4:
#             if sum(nepovt) > sum(povt):
#                 print(k)
#
# k=0
# with open("9_9832") as f:
#     for i in f:
#         k=k+1
#         a=sorted(map(int,i.split()))
#         p=[i for i in set(a) if a.count(i)==2]
#         if a.count(max(a))==1 and len(p)==2 and len(set(a))==5:
#             print(sum(a))
#             break
#

# k=0
# with open("9123") as f:
#     for line in f:
#         a=list(map(int,line.split()))
#         if len(set(a))==4:
#             k+=1
# print(k)

# k=0
# with open("912") as f:
#     for i in f:
#         a=sorted(list(map(int, i.split())))
#         if 2*(a[-1]+a[-2])>3*(a[0]+a[1]+a[2]):
#             q=[x for x in a if x%10==5]
#             if len(q)>=2:
#                 k+=1
# print(k)

# k=0
# with open("098") as f:
#     for i in f:
#         k+=1
#         a=list(map(int,i.split()))
#         povt=[i for i in set(a) if a.count(i)==2]
#         nepovt=[i for i in set(a) if a.count(i)==1]
#         nechet=[i for i in a if i%2!=0]
#         if len(povt)==2 and len(nepovt)==3:
#             if sum(povt)*2<=sum(nechet):
#                 print(sum(a))
#                 break

# k=0
# with open("890") as f:
#     for i in f:
#         s=list(map(int,i.split()))
#         if (s[0]*s[1]>0 and s[2]*s[3]<=0) or (s[0]*s[1]<=0 and s[2]*s[3]>0):
#             k+=1
# print(k)

# k=0
# with open("442") as f:
#     for i in f:
#         k+=1
#         a=list(map(int,i.split()))
#         povt = [i for i in set(a) if a.count(i) == 2]
#         nepovt=[i for i in set(a) if a.count(i)==1]
#         if len(povt)==2 and len(nepovt)==2:
#             if sum(nepovt)<=sum(povt):
#                 print(sum(a))

# k=0
# with open("9123") as f:
#     for i in f:
#         a=sorted(list(map(int,i.split())))
#         if len(set(a))==5:
#             if 2*(a[0]+a[4])<=3*(a[1]+a[2]+a[3]):
#                 k+=1
# print(k)


# k=0
# with open("9123") as f:
#     for i in f:
#         a=sorted(list(map(int,i.split())))
#         povt=[i for i in set(a) if a.count(i)>1]
#         povt1 = [i for i in a if a.count(i) > 1]
#         nepovt=[i for i in set(a) if a.count(i)==1]
#         if len(nepovt)!=0 and len(povt)!=0:
#             if max(a) not in povt:
#                 if (sum(nepovt)/sum(povt1))>=3:
#                     k+=1
# print(k)
