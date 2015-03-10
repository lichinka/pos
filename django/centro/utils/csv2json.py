import csv
import json


f = open( '/tmp/sample.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "id","name","lat","lng" ) )
out = json.dumps( [ row for row in reader ], sort_keys=True, indent=4 )
print out
