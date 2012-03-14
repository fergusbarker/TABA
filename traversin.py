#!/usr/bin/env python
# For generating sentence split CSV files from plain text
import csv

# Main function
def gencsv(file):
    
    # Opens the file and splits it
    array = file.read()
    array = array.split(".")
    
    # Closes the file, only working from array now
    file.close()
    
    # Creating CSV
    newcsv = opem('sentences.csv', 'w')
    writer = csv.writer(newcsv, delimiter='|')
    
    # Writing CSV
    writer.writerow(array)
    
    # Closing
    newcsv.close()


hobbit = open("thehobbit.txt", 'r')

gencsv(hobbit)

# Stops closing on some systems
raw_input()
