
def reverse_number(n):

    reversed_n = int(str(n)[::-1])
    return reversed_n

num = 123456789
result = reverse_number(num)
print(f"Original number: {num}")
print(f"Reversed number: {result}")