import random

def create_password(pass_len):
    upperCase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
               'Q','R','S','T','U','V','W','X','Y','Z']
    lowerCase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    special=['@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',
                '|',';',':','<','>','/','?','.',',']
    password = ""
    for i in range(pass_len):
        if pass_len<8:
            return "Password length should be atleast 8"
        if i%4 == 0:
            password += random.choice(upperCase)
        elif i%4 == 1:
            password += random.choice(lowerCase)
        elif i%4 == 2:
            password += random.choice(numbers)
        else:
            password += random.choice(special)
    return password

print(create_password(8))