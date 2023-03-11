if 5 == 5:
    print("5 = 5")
    print("!!!", end="\n\n")

if 5 > 5:
    print("5 > 5")

user_data = int(input("Wpisz liczbe: "))
print("Podana liczba", user_data, end="\n\n")

if user_data != 5:
    print("liczba weksza od 5")
    # < > =< +> == !=   
    if user_data == 6:
        print("Liczba jest rowna 6", end="\n\n")
    
isHappy = True
if isHappy == True:
    print("user is happy 1x")
#to samo co i:
if isHappy:
    print("user is happy 2x")

isUnhappy = False
if isUnhappy == True:
    print("user is unhappy 1x")
    
if isUnhappy:
    print("user is unhappy 2x")
elif isUnhappy == False:
    print("Yooooo")
else:
    print("user is unhapy")


