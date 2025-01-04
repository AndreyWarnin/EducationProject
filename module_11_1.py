import numpy as np
import pandas as pd

numbers = [1, 5, 14]
dividers = [2, 5, 7]

result1 = np.divide(numbers, dividers)
result2 = np.append(numbers, dividers)
result3 = np.abs((-3, -5.5, -1.2))
result4 = np.floor(1.3)
result5 = np.floor(1.8)
result6 = np.round(np.deg2rad(180), 2)
result7 = np.linspace(0, 7321, 100)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

data = pd.read_csv('pandas_data.csv')
df = pd.DataFrame(data)
print(df)
print(df.iloc[[1,2], 3])
print(df.iat[1, 3])