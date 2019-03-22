# Created 10/11/18
# Author: Dom Kirkham
# Description: Handles input from Arduino


import argparse
import os
from emgio import parsers
import processing.objects as objects
import numpy as np
import ipl.dataprep as dataprep
from vis import plotting


def sort_data(input):
    """Parses accelerometer data"""

    recordings = {}
    # Load all files in an input directory
    directory = input
    assert os.path.isdir(
        directory), "Input Path is not directory"
    # Get paths to all top-level files/dirs in input directory
    pathsToParse = os.listdir(directory)

    # Also append paths to files only in subdirectories (1 level deep)
    for path in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, path)):
            for subPath in os.listdir(os.path.join(directory, path)):
                pathsToParse.append(os.path.join(path, subPath))

    for filename in sorted(pathsToParse):
        # Parse based on file extension
        if os.path.splitext(filename)[1] == ".xlsx":
            name = filename.split("_")[0]
            x, y, z = parsers.data_parse_xlsx(os.path.join(directory, filename))
            recordings[name] = objects.AccelRec(x_array=x, y_array=y, z_array=z, title=name)
            recordings[name].generate_learn_array()
            plotting.plot_from_obj(recordings[name])

            print(x[0])

        elif os.path.splitext(filename)[1] == ".txt":
            print("Skipping file (.txt)")
            continue
        else:
            print("Parser failed on: " + os.path.join(directory, filename) + " (ignoring file and continuing)")

    rec_list = []
    #for rec in recordings.values():
        #rec_list.append(rec.data_array)

    #new_list = dataprep.augment_data(rec_list, 1000, 1000)

    #train_x, train_y, test_x, test_y = dataprep.train_test_split(new_list, 0.2)

    for rec in recordings.values():
        rec_list.append(rec.abs_array)

    x = dataprep.augment_mag_data(rec_list, 1000, 1000)

    train_x = x[0][0:700]
    test_x = x[0][700:]

    train_x, train_y = dataprep.generate_set(train_x, 3)

    test_x, test_y = dataprep.generate_set(test_x, 3)

    #train_x, train_y, test_x, test_y = dataprep.train_test_split(new_list, 0.2)

    return np.array(train_x), np.array(train_y), np.array(test_x), np.array(test_y), np.array(x[0])
