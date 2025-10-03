#Переменная - именновая ячейка в памяти
test = 10
user_name="Alice"#строковый тип - string (str)
max_value=100#численный тип - intereg (int)
our_float= 1.6#число с плавающей точкой (float)
logical=True# True/False (1 или 0) - boolean (bool)

# id - возвращает адрес в памяти
print(id(user_name), max_value, our_float, logical)
a=2
b=2345634
a=b
print(id(a) ,id(b) )

#определяет тип переменной (объекта)
a=123
print(type(a))

a="1"
a=int(a)
print(type(a))
a=int(1)#переводит в int
print(type(a), a)
a=float(a)#переводит в float
print(type(a), a)
a=str(a)#переводит в str
print(type(a), a)
a=bool(a)#переводит в bool (логический тип)
print(type(a), a)


#задача 2
#age=16
#print('Мне',age,'лет')
#индекс начинается с 0
#index всегда целое числоо
a="Текст"
#a- имя, a[index: int]
#print(a[1]) #синтаксис получения элемента по индексу

my_list=[1,2,3,4,5,"Привет"] #тип данных (list)
print(my_list[3].__sizeof__()) #показывает размер в битах

my_list=[1,2,3,4,5,6,7,8,9,10] #always list (нет массивов)
# * / + - (базовые операторы)

print(my_list[1]/3-2)

#{}- dict (словарь) в качестве аргументов ключ: значение
dictonary={"a": 1000}
print(dictonary["a"])

#input - команда ввода данных
a=input('Введите текст: ')
print("Вы ввели:", a)

a=int(input())
b=int(input())
print(a+b)

