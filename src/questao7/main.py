import pandas as pd
import numpy as np

name = ['joaquim','aline','angela','sheldon','leonard','raje','raui','ammy']
num = [1,2,3,4,5,6,7,8]
idade=[12,33,22,4,31,12,32,55]

df = pd.DataFrame({"Name": name, "Numeros": num, "Idade": idade})

df_mask = df["Idade"] <= 25
positions = np.flatnonzero(df_mask)
filtered_df = df.iloc[positions]
print(filtered_df)