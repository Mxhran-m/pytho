#1ab 1 Check given no is fibonacci no
# def is_fibonacci(n):
#     a, b = 0, 1  
#     while b <= n:  
#         if b == n:  
#             return True
#         a, b = b, a + b  
#     return False  

# n = int(input("Enter a number: "))  
# if is_fibonacci(n):
#     print(n, "is a Fibonacci number.")  
# else:
#     print(n, "is not a Fibonacci number.")  



#another approach
def isfib(n):
    a = 0
    b = 1
    while b <= n:
        if b == n:
            return True
        a, b= b, a + b
         
    return False
n = int(input("Enter a number:"))
if isfib(n):
    print(f"{n} is a Fibonacci num")
else:
    print(f"{n} is not a fib seq")