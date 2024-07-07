#4Display Multiplication Tables
# i=1
# n=int(input("Enter which No multiplication Table to display="))
# print(n, "Multiplication Table is")
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1

#another approach
n = int(input("Enter any number:"))
for i in range(1 , 11):
    print(f"{n} X {i} = {n * i}")