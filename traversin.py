import csv

hobbit = open("thehobbit.txt", 'r')

y = hobbit.read()

y = y.split(".")

for i in y:
	
    print i + "."

hobbit.close()

newcsv = open('sentences.csv','w')
writer = csv.writer(newcsv, delimiter="|")

writer.writerow(y)

# Goonies forever
raw_input()
