#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#Выведите все элементы, которые меньше 5.

#Варианты решения:

for elem in a:
    if elem < 5:
        print(elem)
            
print(list(filter(lambda elem: elem < 5, a)))

print([elem for elem in a if elem < 5])
