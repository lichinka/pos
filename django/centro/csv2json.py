import csv
import json

#
# Find the structure of each record
# as described in lines with PK = -1
#
model_str = dict ( )
with open ('/tmp/sample.csv', 'r') as f:
    reader = csv.DictReader (f, fieldnames = ('model', 'pk', 'fields'))
    for row in reader:
        if (int (row['pk']) == -1):
            model_str[row['model']] = row['fields'].split (';')

#
# Load the data with the parsed structure
#
model_data = []
with open ('/tmp/sample.csv', 'r') as f:
    reader = csv.DictReader (f, fieldnames = ('model', 'pk'))
    for row in reader:
        if (int (row['pk']) != -1):
            record = dict ( )
            for field in model_str[row['model']]:
                record[field] = row
            model_data.append
            model_str[row['model']] = row['fields'].split (';')

    out = json.dumps( [ row for row in reader ] )
    print out
