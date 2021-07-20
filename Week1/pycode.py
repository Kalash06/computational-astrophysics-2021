import numpy as np
import csv
import math
filename = 'Starfish_Data.csv'
field = []
rows = []

avgd = 0
totprob = 0
with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
            d = (10**(0.2 * (float(row[0]) + 2.5*float(row[1]) + 0.17))) * (float(row[2]))
            avgd += d
            totprob += float(row[2])
print(avgd/totprob)

#for row in rows
#    print(row[0])
#for row in rows:
#    d = (math.exp((1/5)((row[0]) + 2.5*(row[1]) + 0.17))) * (row[2] / 100)
#    avgd += d
#print(avgd)
