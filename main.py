# 1)Создать переменную типа String
name = ("Gulzharkyn")
# 2)Создать переменную типа Integer(представляет целое число)
age = 32
# 3)Создать переменную типа Float(представляет число с плавающей точкой)
weight = 64.3
# 4)Создать переменную типа Bytes(последовательность чисел в диапазоне 0-255)
b_type = b'Gulzharkyn'
# 5)Создать переменную типа List(список)
list_type = [name, age, weight]
# 6)Создать переменную типа Tuple(кортеж)
tuple_type = (1, '2')
# 7)Создать переменную типа Set(неупорядоченная коллекция уникальных объектов)

# 8)Создать переменную типа Frozen set(то же самое, что и set, только не может изменяться (immutable))

# 9)Создать переменную типа Dict(словарь, где каждый элемент имеет ключ и значение)
dict_type = {'key1': 33,
     'name_1': 'Gulzharkyn'}
# 10)Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(type(name), name)
print(type(age), age)
print(type(weight), weight)
print(type(b_type), b_type)
print(type(list_type), list_type)
print(type(tuple_type), tuple_type)
print(type(dict_type), dict_type)
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 5
b = 8
c = str(5 + 8)
print(type(c), c)
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
d = 4
e = 2
f = 2 + 4
print(type(f), f)
# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
j = int(d / e)
print(type(j), j)
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
i = d * e
print(type(i), i)
# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
s = d // e
print(type(s), s)
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
g = d % e
print(type(g), g)
# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
r = (7 + 12)**3 + 7 * 4 - 44 / 2**4
print(r)