import time


def rec_fib(i:int, end:int, sum:int , next:int , temp:int): 
    if i == end: 
        return 
    print(f"Die nummer {i} : {sum}")
    
    temp = sum 
    sum = next + sum 
    next = temp 
    i += 1
    rec_fib(i, end, sum, next, temp)



if __name__ == "__main__":
    sum = 0
    next = 1
    temp = 0
    choosen = input("Geben Sie die gewünschte Fibonaccizahl ein: ")
    rec_fib(0, int(choosen), sum, next, temp)
   
