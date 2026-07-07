import pandas as pd
import file_io
import logic

df = file_io.load_csv("data/bestsellers.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(logic.books_per_year(df))