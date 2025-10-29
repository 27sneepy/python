# #15
# a=int(input())
# b=False
# for i in range(2,10):
#     if a% i==0:
#         b=True
#         print(i)
#         break
#
#
# #18
# a=int(input())
# for i in range(i):
#     if

# #20
# #in- в условии проверяет принадлежность
# a=input()
# b="aeiouAEIUO"
# for i in a:
#     if i not in b:
#         print(i,end='')

#24
for i in range(3,-1,-1):
    print('*' *(4-i) + ''*i)
for i in range (3,0,-1):
    print('*'*i+''*(4-i))

for i in range(1,8):
    if i>4:
        print("*"*(8-i))
        continue
    print('*'*i)
