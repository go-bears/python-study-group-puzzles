#D3 workshop assignment:
# Please write code that counts the number of entries for each species *
# https://github.com/vicapow/d3-1-day-workshop/blob/master/setosa.tsv

# Please write code that finds the average petal length of each species *
# https://github.com/vicapow/d3-1-day-workshop/blob/master/setosa.tsv

import csv
from collections import Counter
import numpy as np

f1 = open('setosa.csv')
setosa = csv.reader(f1)

species = []

setosa_len = []
versicolor_len = []
virginica_len = []

for row in setosa:
    if len(row[4]) > 0 and row[4] != "species":
		species.append(row[4])

		if row[4] == 'setosa' and len(row[2]) > 0:
			setosa_len.append(float(row[2]))
		
		if row[4] == 'versicolor' and len(row[2]) > 0:
			versicolor_len.append(float(row[2]))

		if row[4] == 'virginica' and len(row[2]) > 0:
			virginica_len.append(float(row[2]))


print Counter(species)


print "setosa petal length average: ", np.mean(setosa_len)
print "versicolor petal length average: ", np.mean(versicolor_len)
print "virginica petal length average: ", np.mean(virginica_len)
