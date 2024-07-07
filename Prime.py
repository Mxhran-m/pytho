#Lab 5: Check if a given number is a Prime Number or not
# num=int(input("Enter the number:="))
# if num > 1:
#     for i in range(2,(num//2)+1):
#         if (num % i)==0:
#             print(num,"is not a prime number")
#             break
#         else:
#             print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")

def isPrime(n):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter the number that you want to check:"))
if isPrime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")