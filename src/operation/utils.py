import csv

with open('src/operations/operationsFiles/operations.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print('Headers: ', headers)
    operations = list(reader)
    print(operations)