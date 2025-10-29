import pandas as pd

data ={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "steps": [10000, 15000, 12000],
    "heart_rate": [120, 130, 125]
}

df = pd.DataFrame(data)
print("original data",df)
pivot_table=df.pivot_table(index='calories', values=['duration','steps'], aggfunc='mean')
print("pivot table",pivot_table)
crosstable=pd.crosstab(df['calories'], df['duration'])
print("cross table",crosstable)