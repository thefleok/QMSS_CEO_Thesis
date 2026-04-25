import pandas as pd

df = pd.read_csv("csv_data/MERGE2.csv")

unique_tickers = df["tic"].dropna().unique()

with open("txt_data/unique_tickers.txt", "w") as f:
    for ticker in sorted(unique_tickers):
        f.write(ticker + "\n")
