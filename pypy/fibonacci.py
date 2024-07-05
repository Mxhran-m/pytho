def isFibonacci(n):
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
        if a == n:
            return True
    return False
n = int(input("Enter any number:"))
if isFibonacci(n):
    print(n, "is a Fibonacci number.")
else:
    print (n,"is not a Fibonacci number.")