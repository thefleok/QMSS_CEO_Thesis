import pandas as pd

df = pd.read_csv("csv_data/raw_compustat_sic_pull.csv")

df = df.dropna(subset=["ceq", "dltt"])

df["mkt_cap"] = df["prcc_f"] * df["csho"]

df_1 = df[df["mkt_cap"] > 1000].copy()

large_cap = df_1[df_1["revt"] > 1000].copy()

sic_to_industry = {
    3674: "Semiconductors/Hardware", 3672: "Semiconductors/Hardware", 3679: "Semiconductors/Hardware",
    2836: "Biotech", 2834: "Biotech", 8731: "Biotech",
    3571: "Semiconductors/Hardware", 3572: "Semiconductors/Hardware",
    7372: "Software", 7371: "Software",
}
large_cap["industry"] = large_cap["sic"].map(sic_to_industry)

# Drop cannabis and non-relevant biotech tickers
exclude_tickers = ['CURLF', 'GTBIF', 'TCNNF', 'HLF', 'USNA']
large_cap = large_cap[~large_cap["tic"].isin(exclude_tickers)]

large_cap.to_csv("csv_data/compustat_large_cap.csv", index=False)
