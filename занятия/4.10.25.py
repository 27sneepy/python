#1
student = {"Имя": "Иван","Фамилия": "Иванов", "Возраст": 17,"Класс": "11A"}
print(student)
#2
a=45
a=str(a)
print('Число в строке:',a)
#3
a="sdfsdfs"
b="sdfsdf"
c="sfsdfdsf"
print(a,b,c,sep=",")
#6
#a=(input())
#b=(input())
#a=float(a)
#b=float(b)
#a=int(a)
#b=int(b)
#print(a+b)
#7
#a,b,c=input(),input(),input()
#print(a,b,c,sep=':')

split-разделитель
a=input().split(" ")
#print(a[0],a[1],a[2],sep=':')

#8
#text="Python"
#text=list(text)
#print(text)
#9
#my_tuple=(1,2,3,4)
#my_list=list(my_tuple)
#print(id(my_tuple),id(my_list),sep=';')

a=(1,2,3,4)
b=[1,2,3,4]
b[0]=5
print(a)
print(b)
