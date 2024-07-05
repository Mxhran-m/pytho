found = 0
List = [1,2,10,4,50,6]
n=int(input("Enter the key to be search:"))
for i in range(len(List)):
    if List[i] == n:
        found = 1
        
if found == 1:
    print("The given number is Found")
else:
    print("The given number is Not Found")