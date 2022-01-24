import json
import csv

with open("JSON File/genres.json") as file:
    data = json.load(file)

fname = "CSV file/genre.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["genre_id", "genre"])
    for item in data["genres"]:
        csv_file.writerow(
            [item["id"], item["name"]])
