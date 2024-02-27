import tensorflow as tf
import numpy as np
import json
from sklearn.model_selection import train_test_split

with open('data.json') as f:
    dataset = json.load(f)
  
with open('testdata.json') as f:
    testdataset = json.load(f)

for sample in dataset:
   sample['vector'] = [e / 100 for e in sample['vector']]

for sample in testdataset:
   sample['vector'] = [e / 100 for e in sample['vector']]

# Create the training and testing sets
X_train = np.array([sample['vector'] for sample in dataset])
y_train = np.array([sample['label'] for sample in dataset])

X_test = np.array([sample['vector'] for sample in testdataset])
y_test = np.array([sample['label'] for sample in testdataset])

print(X_train)







model = tf.keras.models.Sequential([
    

  tf.keras.layers.Dense(128, activation='relu', input_shape=(25,)),
  tf.keras.layers.Dense(200, activation='sigmoid'),


  tf.keras.layers.Dense(10, activation='softmax')
  
])

# Compile & train
model.compile(
  optimizer=tf.keras.optimizers.Adam(),
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=250)

print("Test accuracy : ", model.evaluate(X_test, y_test)[1])

model.save('digit_recognizer_tf')