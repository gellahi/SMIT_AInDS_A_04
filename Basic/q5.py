def is_Prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
        
print(is_Prime(13))
        