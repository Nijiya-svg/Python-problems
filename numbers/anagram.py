def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()  
    return sorted(str1) == sorted(str2)


pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("triangle", "integral"),
]

for s1, s2 in pairs:
    if is_anagram(s1, s2):
        print(f'"{s1}" and "{s2}" ARE anagrams ')
    else:
        print(f'"{s1}" and "{s2}" are NOT anagrams ')