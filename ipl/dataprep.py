import numpy as np

def augment_data(recordings, length, stride):

    augmented_list = []
    for i in range(len(recordings)):
        rec_length = len(recordings[i][0][0])
        if stride == length:
            num_slices = rec_length // length
            for slice_num in range(0, num_slices):
                a = slice_num * length
                b = (slice_num+1) * length
                augmented_list.append([recordings[i][0][0][a:b], recordings[i][0][1][a:b], recordings[i][0][2][a:b]])

        else:
            num_slices = (rec_length - length) // stride
            for slice_num in range(0, num_slices):
                a = slice_num * stride
                b = (slice_num * stride) + length
                augmented_list.append([recordings[i][0][a:b], recordings[i][1][a:b], recordings[i][2][a:b]])

    return augmented_list

def train_test_split(data, split):
    split = int(len(data) * (1-split))

    train_x = data[0:split]
    test_x = data[split:]

    train_x = np.swapaxes(np.array(train_x), 1, 2)
    train_y = train_x
    test_x = np.swapaxes(np.array(test_x), 1, 2)
    test_y = np.swapaxes(np.array(test_y), 1, 2)

    return train_x, train_set, test_x, test_set

def augment_mag_data(recordings, length, stride):

    aug_x_list = []
    aug_y_list = []
    for i in range(len(recordings)):
        rec_length = len(recordings[i])
        if stride == length:
            num_slices = rec_length // length
            for slice_num in range(0, num_slices):
                a = slice_num * length
                b = (slice_num+1) * length
                aug_x_list.append([recordings[i][a:b]])

        else:
            num_slices = (rec_length - length) // stride
            for slice_num in range(0, num_slices):
                a = slice_num * stride
                b = (slice_num * stride) + length
                aug_x_list.append([recordings[i][a:b]])

    return aug_x_list[0]

def generate_set(list, lookback):
    dataX, dataY = [], []
    for i in range(len(list) - lookback - 1):
        a = list[i:(i + lookback)]
        dataX.append(a)
        dataY.append(list[i + lookback])
    return np.array(dataX), np.array(dataY)