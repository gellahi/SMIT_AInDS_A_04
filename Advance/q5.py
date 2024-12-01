def remove_duplicates(myList):
    temp_list=[]
    for i in myList:
        if i in temp_list:
            continue
        temp_list.append(i)
    return temp_list

myList=[1,2,3,2,5,3,7,1,9]
print(remove_duplicates(myList))
        