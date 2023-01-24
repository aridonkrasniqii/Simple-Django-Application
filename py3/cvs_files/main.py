import csv

# reader()

"""
with open('/home/teknikashi/Downloads/Sacramentorealestatetransactions.csv', 'r') as csv_file:
    csv_content = csv.reader(csv_file)

    with open('new_real_estate_file.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)

        for line in csv_content:
            csv_writer.writerow(line)

with open('new_real_estate_file.csv', 'r') as new_csv_file:
    csv_content = csv.reader(new_csv_file)
    for line in csv_content:
        print(line)
"""

# DictReader => { Dictionary }
columns = []
with open('new_real_estate_file.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    i = 0
    for line in csv_reader:
        if i == 0:
            i = i + 1
            for key in line.keys():
                columns.append(key)

        print(line)

# DictWriter

# To copy a file first you need to read the file than to write content to another content
with open('new_real_estate_file.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('real_estate.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=columns, delimiter="\t")
        # first write the columns
        csv_writer.writeheader()

        for line in csv_reader:
            # here we can also delete a column,
            # column will not be copied
            del line[columns[0]]
            csv_writer.writerow(line)
