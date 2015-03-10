import csv
import json

#
# Open the JSON file
#
json_file = open ('%s.json' % file_name, 'r')
json.load (json_file)


#
# Dump the structure of each record
# on lines with PK = -1
#
for entity in json_dict:
    csv_file = open('%s.csv' % entity, 'wb')
    headers = a[entity][0].keys()
    csv_writer = csv.DictWriter(csv_file, headers)
    map(csv_writer.writerow, json_dict[entity])
    csv_file.close()

