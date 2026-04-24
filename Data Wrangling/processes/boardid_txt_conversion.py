import pandas as pd

df = pd.read_csv("csv_data/boardex_id_data.csv")

unique_boardids = df["boardid"].dropna().unique()

with open("txt_data/unique_boardids.txt", "w") as f:
    for boardid in sorted(unique_boardids):
        f.write(str(int(boardid)) + "\n")
