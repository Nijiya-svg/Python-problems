def char_frequency(s):
    frequency = {}
    
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

text = "hello world"
result = char_frequency(text)

print(f"Character frequency in '{text}':")
for char, count in sorted(result.items()):
    if char != " ":
        print(f"  '{char}' : {count}")