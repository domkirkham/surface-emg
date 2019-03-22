import os
import pandas as pd


def data_parse_txt(filename):

    (root, extension) = os.path.splitext(filename)

    if extension != ".txt":
        print("File is not a raw text file")
        return

    file = open(filename, 'r')

    lines = file.readlines()

    file.close()

    raw_data = []
    metadata = []

    x_values = []
    y_values = []
    z_values = []


    for line in lines:
        if line[0] == '#':
            metadata.append(line)
        elif line[0] == '\n':
            continue
        else:
            raw_data.append(line)

    for line in raw_data:
        x, y, z, step = line.split(" ")
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)


    print(raw_data)

#data_parse_txt('2_UPDRS0.txt')

def data_parse_xlsx(filename):

    (root, extension) = os.path.splitext(filename)


    if extension != ".xlsx":
        print("File is not an Excel file")
        return

    file = pd.read_excel(filename, header=None)

    file.columns = ["x", "y", "z"]

    x_values = file['x'].tolist()
    y_values = file['y'].tolist()
    z_values = file['z'].tolist()

    return x_values, y_values, z_values
