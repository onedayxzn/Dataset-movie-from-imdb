import pandas as pd
import json
import csv
with open("JSON File/listmovie4.json") as file:
    data = json.load(file)

fname = "CSV file/listmovie4.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["", "", "", ""])
    for item in data["items"]:
        csv_file.writerow(
            [item["id"], item["original_title"], item["genre_ids"], item["overview"]])

data = pd.read_csv("CSV file/listmovie4.csv")
print(data.shape)

# total 9 baris
