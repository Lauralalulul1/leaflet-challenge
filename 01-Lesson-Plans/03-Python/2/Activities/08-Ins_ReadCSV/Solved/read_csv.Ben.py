#Import modules
import csv
import os
#create path to file
accountingFilePath =  os.path.join("..","Resources","accounting.csv")
#read csv
with open(accountingFilePath ) as csvFile:
	#create csv reader
	csvReader = csv.reader(csvFile)
	# print the csv reader object
	for row in csvReader:
		print(row)