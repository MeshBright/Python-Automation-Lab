import pandas as pd

# 1. Create a simple dataset (Dictionary)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

# 2. Convert it into a DataFrame (The core pandas object)
df = pd.DataFrame(data)

# 3. Print it out
print("Setup Successful! Here is your DataFrame:")
print("-" * 30)
print(df)
print("-" * 30)