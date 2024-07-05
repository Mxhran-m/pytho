#1ab 1 Check given no is fibonacci no
def is_fibonacci(n):
    a, b = 0, 1  
    while b <= n:  
        if b == n:  
            return True
        a, b = b, a + b  
    return False  

n = int(input("Enter a number: "))  
if is_fibonacci(n):
    print(n, "is a Fibonacci number.")  
else:
    print(n, "is not a Fibonacci number.")  
