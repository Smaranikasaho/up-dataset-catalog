import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/up_dataset_catalog.csv")

print(df.head())

title_count = df["title"].value_counts().head(10)

plt.figure(figsize=(10,5))

title_count.plot(kind="bar")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/top_titles.png")

print("Chart saved")