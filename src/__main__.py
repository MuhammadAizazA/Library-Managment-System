import csv

if __name__=='__main__':
    csv_file = open('Data/admin.csv','r')
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row[0])
    csv_file.close()