import pandas as pd
import IPython

df = pd.read_csv("usa-agricultural-exports-2011.csv")
columns = df.columns.tolist()
columns = [column for column in columns
           if "Unnamed" not in column]
df = df[columns]
IPython.embed()
