def power_func(number,power):
    if power>0:
        return number*power_func(number,power-1)
    return 1
print(power_func(2,4))