
def is_prime(num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
        
def gcd(num1,num2):
    if is_prime(num1) or is_prime(num2):
        return 1
    else:
        cd_list=[]
        max_num=max(num1,num2)
        for i in range(1,max_num+1):
            if num1%i==0 and num2%i==0:
                cd_list.append(i)
    if cd_list==[]:
        return 1
    else:
        cd_list.reverse()
        return cd_list[0]
        
print("GCD is: ",gcd(12,18))
                