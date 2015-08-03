import csv
import json

csvfile = open('import.csv', 'r')
jsonfile = open('import.json', 'w')
model = "DjanogApp.DjangoModel"
pkstart = 0

jsonfile.write("[")
reader = csv.DictReader( csvfile)
i = 0
for row in reader:
  if i != 0:
    jsonfile.write(',\n')
  d = {}
  d["fields"] = row
  d["model"] = model
  d["pk"] = i + pkstart
  i += 1
  json.dump(d, jsonfile)

jsonfile.write("]")
