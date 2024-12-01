def is_anagram(str1,str2):
    if len(str1)==len(str2):
        count=0
        for i in str1:
            if i in str2:
                count+=1
        if count==len(str2):
            return True
        else:
            return False
    return False
    
print(is_anagram("bored","robed"))