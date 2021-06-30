import pandas as pd

df = pd.read_parquet('data/training_data_2020_03_14.parquet')
print(df.info())

