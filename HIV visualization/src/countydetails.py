import pandas as pd

# demonstrate data source for HIV prevelance and county census details.

data_prev = "AIDSVu_County_prev_2020.csv"
data_SDOH = "AIDSVu_County_SDOH_2020.csv"

prev = pd.read_csv(data_prev, encoding="cp1252").dropna()
county_data = pd.read_csv(data_SDOH,encoding="cp1252").dropna()

merge = pd.merge(prev,county_data)

