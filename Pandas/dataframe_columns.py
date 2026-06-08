import pandas as pd

data = {
    "Name": ["Khushi", "Aman"],
    "Marks": [95, 88]
}

df = pd.DataFrame(data)

print(df["Name"])
