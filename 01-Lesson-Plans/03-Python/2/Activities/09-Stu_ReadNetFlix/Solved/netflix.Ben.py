#Import modules
import csv
import os
import string
#create path to file
accountingFilePath =  os.path.join("../Resources/" + "netflix_ratings.csv")
#prompt the user for movie
user_movie  = input("what do you want to watch? ")
#read csv
with open(accountingFilePath ) as csvFile:
	#create csv reader
	csvReader = csv.reader(csvFile)
	# print the csv reader object
	for row in csvReader:
		if(row[0].lower() == user_movie.lower()):
			print(f"{row[0]} is rated {row[1]} with a user rating of {row[5]}")