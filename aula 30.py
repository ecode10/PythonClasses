#aula 30
#loop using if 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#newList = [fruit for fruit in fruits if fruit != "apple"]

newList = []

for fruit in fruits:
    if fruit != "apple":
        newList.append(fruit)

print(newList)