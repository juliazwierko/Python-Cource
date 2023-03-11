number = 5 # integer/int 
digit = 4.54321 # float
digit_2 = "4.54321" # string!!!
word = "Siemaaa:" # string
#bool - True/False # bool
boolean = False

print("\n")
#print(word + boolean) - ERROR string+bool BLAD, rozne typy danych 
print(boolean)
print(word, digit)
print("Wynik:",number)

#usuwanie zmniennej
del number 

number = 5**2
print("Wynik:",number)
print("\n")

#Funkcja str(float/int) - float/int-->string
#Funkcja int(string) - string-->int

#unput() - praca z uzytkownikiem 
num_1 = int(input("Wpisz 1 liczbe "))
num_2 = int(input("Wpisz 2 liczbe "))

print("Dzialania matematyczny na wpisanych liczbach:")
print("num_1 + num_2 = ", num_1+num_2)
print("num_1 - num_2 = ", num_1-num_2)
print("num_1 * num_2 = ", num_1*num_2)
print("num_1^num_2 = ", num_1**num_2)
print("num_1 / num_2 = ", num_1/num_2)
print("num_1 // num_2 = ", num_1//num_2, end="\n\n")

num_1 += 5 #num_1 = num_1+5
print("num_1 + 5 = ",num_1, end="\n\n")

word = "Paweeeł <3" #string
print(word * 2) #wypisuje 2 razy
word = "Cynamonka ^_^" #string
print(word)
word = True #bool
print(word)
