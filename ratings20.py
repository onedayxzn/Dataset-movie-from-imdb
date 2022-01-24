import pandas as pd
import json
import csv
with open("JSON File/listmovie20.json") as file:
    data = json.load(file)

fname = "CSV file/ratings20.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["", ""])
    for item in data["items"]:
        csv_file.writerow(
            [item["id"], item["vote_average"]])
data = pd.read_csv("CSV file/ratings20.csv")
print(data.shape)
