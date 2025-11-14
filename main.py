import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "data/movies_metadata.csv"
# df = DataFrame
df = pd.read_csv(url)
# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())
# print(df[["belongs_to_collection", "homepage", "tagline"]])

# print(df.tagline)
# Старий варіант
# df["tagline"].fillna("without tagline", inplace=True)
# Нові альтернативи старому варіанту
# df.fillna({"tagline": "without tagline"}, inplace=True)
df["tagline"] = df["tagline"].fillna("without tagline")
# print(df.tagline)
# print(df.homepage)
df.homepage = df.homepage.fillna("no homepage")
# print(df.homepage)
# print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection": "{}"}, inplace=True)
# print(df["belongs_to_collection"])
# df.info()
df.dropna(inplace=True)
# print(df.isnull().sum())
# df.info()
#------------------------------------------------------
# print(df.head())
# print(df.genres)
genres_counts = df['genres'].value_counts()
# print(genres_counts)
# print(genres_counts.index)
# print(genres_counts.values)
plt.figure(figsize=(10,6))

sns.barplot(x=genres_counts.index, y=genres_counts.values)

plt.title("Count filn for genres")
plt.xlabel("genres")
plt.ylabel("counts")

plt.xticks(rotation=0)

plt.show()