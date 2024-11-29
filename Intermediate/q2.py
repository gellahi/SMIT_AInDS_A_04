def nth_fibonacci(nth_term):
    fibonacci_list=[]
    def fibonacci_series(firstNum,secondNum,limit,fibonacci_list):
        if(len(fibonacci_list)==limit):
            return fibonacci_list
        else:
            fibonacci_list.append(firstNum)
            return fibonacci_series(secondNum,firstNum+secondNum,limit,fibonacci_list)
    resList=fibonacci_series(0,1,nth_term,fibonacci_list)
    return resList[nth_term-1]
    
print("Nth Fibonacci Term is: ",nth_fibonacci(10))