def highest_val_key(myDict):
    if myDict==None:
        return None
    return max(myDict,key=myDict.get)

myDict={'a': 10, 'b': 25, 'c': 7}
print("Highest Key: ",highest_val_key(myDict))