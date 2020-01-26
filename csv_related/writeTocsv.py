# how to write list into csv by row/column

import csv

A = [1,1,1,1,1,1]
B = [2,2,2,2,2,2]
C = [3,3,3,3,3,3]
D = [4,4,4,4,4,4]

# write by row
def writeIntocsv_row():
    with open('record0.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(A)
        writer.writerow(B)
        writer.writerow(C)
        writer.writerow(D)
    csvFile.close()

# write by column
def writeIntocsv_column():
    New_list = []
    LENGTH = len(A)
    i = 0
    while i < LENGTH:
        New_list.append([A[i], B[i], C[i], D[i]])
        i += 1
    with open('record1.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for i in New_list:
            writer.writerow(i)
    csvFile.close()

writeIntocsv_row()
writeIntocsv_column()
print('write finish')
