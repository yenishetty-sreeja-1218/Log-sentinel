import dask.dataframe as dd

# Load logs
df = dd.read_csv("app_logs.csv")

print("\n✔ Logs Loaded Successfully")
print(df.head())

# Basic stats
print("\n✔ Log Level Count:")
print(df["level"].value_counts().compute())

print("\n✔ Service-wise Avg Response Time:")
print(df.groupby("service")["response_time_ms"].mean().compute())
