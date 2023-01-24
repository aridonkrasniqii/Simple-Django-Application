import csv

# Copy a text file into new_file
with open('txt.txt', 'r') as file:
    offset = 100
    file_content = file.read(100)
    with open('new_txt.txt', 'w') as new_file:
        while len(file_content) > 0:
            new_file.write(file_content)
            file_content = file.read(100)

# Copy a csv file
# With csv.reader()
with open('/home/teknikashi/Downloads/Sacramentorealestatetransactions.csv', 'r') as file:
    csv_content = csv.reader(file)

    with open('new_real_estate_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_content:
            csv_writer.writerow(line)

# Copy a csv file
# With DictReader


with open('/home/teknikashi/Downloads/Sacramentorealestatetransactions.csv', 'r') as file:
    csv_dict = csv.DictReader(file)

    columns = []
    for line in csv_dict:
        for key in line.keys():
            columns.append(key)
        break
    print(columns)
    with open('new_real_estate_file.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=columns)

        for line in csv_dict:
            csv_writer.writerow(line)
