import csv

with open("names.csv", "r") as file:
    dict_content = csv.DictReader(file)
    list_content = list(dict_content)

for content in list_content:
    for key in content.keys():
        print(content[key], end='')
    print()

with open('names.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # To skip a line we can skip it with next() method
    # next(csv_reader)
    # for loop will start at the second line

    # This is an object , we need to loop through each element
    # print(csv_reader)
    # Each line is a list
    for line in csv_reader:
        # print(line)
        # If we want to print a column
        print(line[0])

#
#
#
#
# Let's save the values to new csv file but use dashed instead of commas for the dilimeter

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

