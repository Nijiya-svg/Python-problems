

def find_non_repeating(arr):
    frequency = {}
    

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    
  
    result = [num for num in arr if frequency[num] == 1]
    return result


arr = [1, 2, 2, 3, 4, 4, 5]
result = find_non_repeating(arr)
print(f"Array: {arr}")
print(f"Non-repeating elements: {result}")