import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.layers import Dense
from keras.models import Sequential
from keras.models import load_model
from keras.callbacks import EarlyStopping
import pandas as pd

data = pd.read_csv('hourly_wages.csv')
predictors = data.drop(['construction'], axis=1).as_matrix()
n_cols = predictors.shape[1]
target = to_categorical(data.construction)
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping_monitor = EarlyStopping(patience=2)
model_training = model.fit(predictors, target, epochs=15, validation_split=0.1)

model_2 = Sequential()
model_2.add(Dense(100, activation='relu', input_shape = (n_cols,)))
model_2.add(Dense(100, activation='relu'))
model_2.add(Dense(100, activation='relu'))
model_2.add(Dense(2, activation='softmax'))
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping_monitor = EarlyStopping(patience=2)
model_2_training = model.fit(predictors, target, epochs=15, validation_split=0.1)

plt.plot(model_training.history['val_loss'], 'b')
plt.plot(model_2_training.history['val_loss'], 'r')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()
