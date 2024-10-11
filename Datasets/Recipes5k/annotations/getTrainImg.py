import csv
import os

imgIdArr=[]
data=[]

#ID
with open('train_images.txt', 'r') as in_file:
    for line in in_file:
        className = line.split('/')[0]
        data.append([line.rstrip(),className])
        
with open('train.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["id","class"])
    writer.writerows(data)