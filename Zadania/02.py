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
