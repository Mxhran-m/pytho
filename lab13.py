#2.Demonstrate use of advanced regular expressions for data validation
import re
pattern = r'^[A-Za-z]{2}$'
data = '%@#'
if re.match(pattern, data):
    print('Valid data.')
else:
    print('Invalid data!')
