#7. Demonstrate Exceptions in Python
try:
    numl = int(input('Enter a number'))
    num2 = int(input("Enter another number:"))
    result = numl / num2
    print("Result:",result)
except ValueError:
    print("invalid input.Please enter a valid number.")
except ZeroDivisionError:
    print("Error:Division by zero occurred.")
except Exception as e:
    print ("An error occurred:", str(e))