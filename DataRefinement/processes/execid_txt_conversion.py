import pandas as pd

bridge = pd.read_csv("csv_data/boardex_to_execucomp.csv")

unique_execids = bridge["execid"].dropna().unique()

with open("txt_data/unique_execids.txt", "w") as f:
    for execid in sorted(unique_execids):
        f.write(str(int(execid)) + "\n")
