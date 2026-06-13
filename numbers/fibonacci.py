def fibonacci(n):
    series = []
    a, b = 0, 1
    
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series
n = 7
result = fibonacci(n)
print(f"Fibonacci series up to {n} terms:")
print(result)