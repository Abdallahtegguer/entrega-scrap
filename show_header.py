import pandas as pd

df = pd.read_csv("dataset/99_to_2001_dataset_fr.csv", encoding="latin1", sep=None, engine="python")
print(df.head())
print(df.columns)
