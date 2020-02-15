#Use MOVE
#######
#Imports two csv files containing the long record and the short record
#CSV format for this example is: column 1 = years, column 2 = flows
#imports the MOVE.py module and calls comp_extended_record function
#writes results to a new csv file named 'extended_short_record.csv"
#the input csvs can be swapped for other stations provided they are in the
#same format as the example data
#this script has only been tested on the example data in Appendix 8 of
#Guidelines for Determining Flood Flow Frequency Bulletin 17C
#Version 1.1 published May 2019 - USGS
#Results provided by this script are slightly different than those in the
#example due to rounding


import MOVE
import csv

with open('Suwanee.csv', 'r') as f:
    reader = csv.reader(f)
    y = list(reader)
    
    short_years = [int(y1[0]) for y1 in y]
    short_record = [int(y1[1]) for y1 in y]

with open('Etowah.csv', 'r') as f:
    reader = csv.reader(f)
    x = list(reader)
    
    long_years = [int(x1[0]) for x1 in x]
    long_record = [int(x1[1]) for x1 in x]


out = MOVE.comp_extended_record(short_years, short_record, long_years, long_record)

with open('extended_short_record.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(out[1],out[0]))

