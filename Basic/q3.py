def factorial(num):
    if num>0:
        return num*factorial(num-1)
    else:
        return 1
print("Factorial of Number is: ",factorial(4))