#aula 32
#join two lists

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

#1
#list3 = list1 + list2

#2 - append
#for x in list2:
#    list1.append(x)

list1.extend(list2)
print(list1)