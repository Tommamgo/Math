import time
sum = 0
next = 1
temp = 0

choosen = input("Geben Sie die gewünschte Fibonaccizahl ein: ")


for i in range(int(choosen)):
    temp = sum
    sum = next + sum
    next = temp 
    print(f"Die nummer {i+1} : {sum}")





