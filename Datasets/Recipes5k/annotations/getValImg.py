import csv
import os

imgIdArr=[]
data=[]

#ID
with open('val_images.txt', 'r') as in_file:
    for line in in_file:
        className = line.split('/')[0]
        data.append([line.rstrip(),className])

#Create CSV for id and class
with open('val.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["id","class"])
    writer.writerows(data)