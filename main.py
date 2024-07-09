import pandas as pd 
pd.set_option("display.max_columns", 500)

raw_df = pd.read_csv("all_delays.csv")

station_analysis = raw_df.groupby(["Station"])['Day'].count().reset_index()
print(station_analysis)