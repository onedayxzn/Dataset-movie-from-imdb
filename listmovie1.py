import pandas as pd
import json
import csv
with open("JSON File/listmovie1.json") as file:
    data = json.load(file)

fname = "CSV file/listmovie1.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["movie_id", "movie_title", "genre_ids", "overview"])
    for item in data["items"]:
        csv_file.writerow(
            [item["id"], item["original_title"], item["genre_ids"], item["overview"]])

data = pd.read_csv("CSV file/listmovie1.csv")
print(data.shape)

# total 58 baris
