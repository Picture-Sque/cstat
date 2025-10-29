def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter n (0 for 0, 1 for first Fibonacci): "))
print("Fibonacci number:", fib(n))
