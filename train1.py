import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from ipl import input as inp

sns.set()

from tensorflow.keras.utils import plot_model

import ipl.dataprep as dataprep

#Callbacks for early stopping and to save the model after each epoch
#early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0.01, patience=15, verbose=0, mode='auto', baseline=None)
save = tf.keras.callbacks.ModelCheckpoint('weights.{epoch:02d}-{val_loss:.2f}.hdf5', monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)


#Constructs the model


#model.add(tf.keras.layers.LSTM(200, input_shape=(3,1000), return_sequences=True))
#model.add(tf.keras.layers.LSTM(200, dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
#model.add(tf.keras.layers.LSTM(100, dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
#model.add(tf.keras.layers.Dense(1000, activation="linear"))

#model.compile(loss='mean_squared_error', optimizer='nadam', metrics=['accuracy'])

#Prints the model summary which shows input and output dimensions etc, similar to the plot below
#print(model.summary())

#Plots the model architecture with graphviz (output in docs)
#plot_model(model, to_file='modelvis3.png', show_shapes=True, show_layer_names=False)

# Generate training and testing data

print("Training data parsed")
#Augmentation of the dataset with window slicing

print("Training data sliced")

#Data must be in arrays to be used in the model

#Converts the classes of the labels to categorical classes as required
train_x, train_y, test_x, test_y, x = inp.sort_data('/Users/dominickirkham/Documents/Projects/sEMG/surface-emg/pdb')

train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

model = tf.keras.Sequential()

model.add(tf.keras.layers.LSTM(4, input_shape=(1,3)))
model.add(tf.keras.layers.Dense(1, activation="linear"))

model.compile(loss='mean_squared_error', optimizer='adam')

print(train_x.shape, train_y.shape)

#assert train_x.shape == train_set.shape, "Data different shapes"

print(model.summary())

# The model always expects an array with 3 dimensions (as it expects features as inputs, but since using a CNN this dim
# remains empty
#train_data = np.expand_dims(train_data, axis=2)

#test_data = np.expand_dims(test_data, axis=2)

#Option here to split training data into training and validation sets
history = model.fit(train_x, train_y, epochs=150, batch_size=1, verbose=2)

# Plot summarize history for loss
plt.figure(figsize=(10,5))
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('loss.png', dpi=300)


test_predict = model.predict(test_x)

prediction = [np.nan]*699
prediction.append(test_predict)

plt.figure(figsize=(10,5))
plt.title("Tremor prediction")
plt.ylabel('Sample number')
plt.plot(x)
plt.plot(prediction)
plt.legend(["Tremor", "Tremor prediction"], loc="upper left")
plt.savefig('pred.png', dpi=300)

#Returns the loss and accuracy of the model on the test data
#scores = model.evaluate(test_data, test_labels, batch_size=128)

#print(scores)