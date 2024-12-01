def temp_converter(temp,typeTemp):
    if typeTemp == 'F' or typeTemp =='f':
        return ((32*temp)-32)*5/9
    elif typeTemp == 'C' or typeTemp =='c':
        return (temp*9/5)+32
    return None
        
        
print(temp_converter(35.6,'C'))