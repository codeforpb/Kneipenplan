# known bugs: does not include links
import csv

with open('food.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
  for row in spamreader:
    print ('- name: "',row[0],'"')
    print ('  description: "', row[1], '"')
    print ('  special: "', row[2], '"')
    print ('  url: "', row[3], '"')
    print ('  lat: ', row[4])
    print ('  lon: ', row[5])
    print ('')
