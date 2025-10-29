# a=[[1,2],
#    [3,4]
# ]
# # [3,1],
# # [4,2]
# #
# print(a[0])
# print(a[1])
# print('-'*10)
# for index in range(0,len(a)):
#     print(a[index][1])
#range - генерирует список элементов в промежутке от и до
#len - длина object
# a=[[1,2],[3,4]]
# b=[[0,0],[0,0]]
# for i in range (len(a)):
#     for j in range (len(a[0])):
#         b[i][j] = a[i][j]
# for i in b:
#     print(i)
#2
# b="1234567890"
# counter=0
# while True:
#     a=input("введите пароль: ")
#     if counter==2:
#         print("попробуй в другой раз")
#         break
#     counter+=1
#     if len(a)<8:
#         print("Пароль неверный, нужно больше 8 символов")
#     else:
#         k=False#есть ли в пароле числа?
#         for i in b:
#             print(i)
#             if i in a:
#                 k=True
#                 break
#             if k:
#                 print("Пароль верный")
#             else:
#                 print("Пароль неверный")



a = [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
]#куб
a = [1,2,3,4]
a = [#[[1,2],[1,2]]
    [1,2],
    [3,4],
    [5,6],
]#таблица#a[0][1]
b = [[0,0],[0,0],[0,0]]
#len range
a = [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        for z in range(len(a[i][j])):
            print(a[i][j][z])