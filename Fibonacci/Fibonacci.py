import time
sum = 0
next = 1
temp = 0
i = 0

while(True):
    temp = sum 
    sum = next + sum 
    next = temp
    print("Nummer " + str(i) + ": " + str(sum))
    time.sleep(0.1)
    i+=1
