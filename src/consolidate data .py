import json
import pandas as pd

with open("data/raw/page_001.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data, columns=["title"])

print(df)

df.to_csv("data/processed/up_dataset_catalog.csv", index=False)

print("CSV file created")