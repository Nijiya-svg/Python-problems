def is_perfect(n):
    divisors_sum = 0
    
    for i in range(1, n):
        
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n


numbers = [6, 28, 12, 496]
for num in numbers:
    if is_perfect(num):
        print(f"{num} is a Perfect Number ")
    else:
        print(f"{num} is NOT a Perfect Number ")