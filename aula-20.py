#string format

age = 26
#description = "My name is John, I am " + age
#print(description)

description = "My name is John, I am {} "

print(description.format(age))

salario = 1000
bonus = 5000

txt = "Eu quero o valor {} de salário mas também quero o bônus de {}"

print(txt.format(salario, bonus))