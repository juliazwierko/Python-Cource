#1
# округление до двух знаков после запятой
print(round(2.545, 2))   # 2.54
print(round(2.555, 2))   # 2.56 - округление до четного
print(round(2.565, 2))   # 2.56
print(round(2.575, 2))   # 2.58
 
print(round(2.655, 2))   # 2.65 - округление не до четного
print(round(2.665, 2))   # 2.67
print(round(2.675, 2))   # 2.67

#2
x = 45       # Значение, которое надо зашифровать - в двоичной форме 101101
key = 102    # Пусть это будет ключ - в двоичной форме 1100110
 
encrypt = x ^ key    # Результатом будет число 1001011 или 75
print(f"Зашифрованное число: {encrypt}")
 
decrypt = encrypt ^ key    # Результатом будет исходное число 45
print(f"Расшифрованное число: {decrypt}")

#3
a = 22 # в двоичной форме 10110
b = 2
c = a << b  # Сдвиг числа 10110 влево на 2 разряда, равно 1011000 или 88 в десятичной системе
print(c)   # 88
 
d = a >> b  # Сдвиг числа 10110 вправо на 2 разряда, равно 101 или 5 в десятичной системе
print(d)   # 5

#4
language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")
        
#5
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
