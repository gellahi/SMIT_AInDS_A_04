def is_palindrome(any_str):
    temp_str=any_str[::-1]
    if any_str.lower()==temp_str.lower():
        return True
    return False
    
print(is_palindrome("Maham"))