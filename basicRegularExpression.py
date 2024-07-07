#1.Demonstrate usage ot basic regular expression
import re
text=input("Enter the Text=")
pattern=input("enter the pattern to be search=")
match = re.search(pattern, text)
if match:
    print('Match found!')
else:
    print('No match found')