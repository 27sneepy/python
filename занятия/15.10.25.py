#пока условие
#бесконечный цикл если True
# while True:#while условие (a>10)
#     print("hello")

#for переменная in итерируемый объект
#list
#1:1
#3:3
#2:2
#string
# a="asfasdfa"
# #print(a[0])
# #в переменную i записываются эл-ты посимвольно
# #для каждой итерации цикла
# for i in "asfda":
#     print(i)


#range (начало, конец, шаг)
#этот метод генерирует список (генератор) чисел от
#начало до конец-1

# print(list(range(0,10,3)))
# print(list(range(10,0,-3)))
# for i in range(10):
#     print(i)

#break -останавливает выполнение цикла
#continue- останавливает итерацию цикла
# counter=0
# counter_false=0
# while True:
#     counter+=1
#     if counter%3==0:
#         break
#         counter_false+=1
#         continue
#     print("наше значение:", counter)
# print("Это количество не кратных: ", counter_false)

# a=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# for i in a:
#     for j in i:
#         print(j)


# a=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# i=0
# j=0
# #len(object) - возвращает длину object
# # print(len(a))
# # print(len(a[0]))
# # print(a[len(a)-1])
# while i<=len(a):
#     while j<len(a[0]):
#         print(a[i][j])
#         j+=1
#     i+=1
#
# a=[1,2,3]
# #отрицательный индекс получает эл-т с обратной стороны
# print[a[-2]]

#2
# for i in range(11):
#     print(i)

#6
# n=int(input())
# for i in range(1,n+1):
#     print(i*i)

# 11
# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)
# print("gotovo")
