#Lab IO progratn to implement stack operation
print("-----stack operation-----")
repeat = 1
arr = []
while repeat == 1:
    print("1. push  2. pop  3. display")
    n = int(input("Enter choice="))
    if n == 1:
        num = int(input("Enter number to push="))
        arr.append(num)
    elif n == 2:
        if arr:
            print("Popped element is=", arr.pop())
        else:
            print("Stack is empty")
    elif n == 3:
        print("Stack:", arr)
    else:
        print("Invalid choice")
    
    repeat = int(input("Press 1 to repeat or any other key to exit="))
