import pandas as pd

df = pd.read_excel(r"Customer Call List.xlsx")

#remove duplicates
dd = df.drop_duplicates()

#remove columns
dd.drop(columns="Not_Useful_Column")


print(dd)
