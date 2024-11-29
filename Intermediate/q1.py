def largest_number(list_num):
    list_num.sort(reverse=True)
    return list_num[0]
list_num=[3,5,1,0,10,9,7,2]
print("Largest Number is: ",largest_number(list_num))