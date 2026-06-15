def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
   
    return s == s[::-1]


words = ["racecar", "hello", "madam", "python", "level"]

for word in words:
    if is_palindrome(word):
        print(f'"{word}" is a Palindrome ')
    else:
        print(f'"{word}" is NOT a Palindrome ')