import pandas as pd

df = pd.read_csv("csv_data/CEOS.csv")

unique_directorids = df["directorid"].dropna().unique()

with open("txt_data/unique_directorids.txt", "w") as f:
    for directorid in sorted(unique_directorids):
        f.write(str(int(directorid)) + "\n")
