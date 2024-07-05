#11. Create Data Frame from Excel sheet using Pandas and Perform Operations on Data frames
import pandas as pd
data = pd.read_excel("dataf.xlsx")
print(data)
print(data['column1'].sum())
print(data['Column2'].mean())
print(data['Column3'].max())
print(data['Column4'].min())