import time


def rec_fib(i:int, end:int, sum:int , next:int , temp:int): 
    if i == end: 
        return 

    temp = sum 
    sum = next + sum 
    next = temp 
    print(f"Die nummer {i+1} : {sum}")
    i += 1
    rec_fib(i, end, sum, next, temp)



if __name__ == "__main__":
    sum = 0
    next = 1
    temp = 0
    choosen = input("Geben Sie die gewünschte Fibonaccizahl ein: ")
    rec_fib(1, int(choosen), sum, next, temp)
   
