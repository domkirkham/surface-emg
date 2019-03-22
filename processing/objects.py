import numpy as np

class AccelRec:
    # sample_array
    def __init__(self, x_array, y_array, z_array, abs_array=None, sample_times=None, title=None, data_array=None):
        self.x_array=x_array
        self.y_array=y_array
        self.z_array=z_array
        self.sample_times=sample_times
        self.title=title
        self.abs_array=abs_array
        self.data_array=data_array

    def abs_acc(self):
        length = len(self.x_array)
        self.abs_array = [0] * length

        for i in range(length):
            self.abs_array[i] = np.sqrt(self.x_array[i]**2 + self.y_array[i]**2 + self.z_array[i]**2)

    def generate_learn_array(self):
        self.data_array = [[self.x_array, self.y_array, self.z_array]]