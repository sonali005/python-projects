import csv 

with open('names.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file)

    with open('new_names.csv', 'w') as csv_file:   #using writer method
        csv_writer = csv.writer(csv_file, delimiter = '')
        #delimiter, a symbol used to spearate indexes or the data

    for line in csv_reader:
        csv_writer.writerow(line)

    