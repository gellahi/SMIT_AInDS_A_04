def vowels_count(my_str):
    count=0
    vowels = ['a','e','i','o','u']
    for i in my_str:
        if i in vowels:
            count+=1
    return count
print("No. of Vowels in String: ",vowels_count("GoharEllahi"))