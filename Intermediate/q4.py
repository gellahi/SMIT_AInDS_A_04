def even_sum(list_int):
    even_list=[i for i in list_int if i%2==0]
    return sum(even_list)
    
my_list=[0,1,2,3,4,5,6,7,8,9,10]
print("Sum of Even Numbers in List are: ",even_sum(my_list))