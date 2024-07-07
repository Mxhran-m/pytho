#3 Find the sum of n natural nun)bets
i=1
sum=0
n=int(input("Enter the number of natural no's to be sum="))
print(n, "Natural nurnbers are \n")
while i<=n:
    print(i)
    sum+=i
    i += 1
print(n, "Natural no's Sum=", sum)