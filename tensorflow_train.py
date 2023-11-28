import tensorflow as tf
import numpy as np
import json
from sklearn.model_selection import train_test_split

# Load the data
with open('data.json') as f:
    dataset = json.load(f)

X = np.array([sample['vector'] for sample in dataset])
y = np.array([sample['label'] for sample in dataset])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Build model
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(64, activation='relu', input_shape=(25,)),
  tf.keras.layers.Dense(50, activation='relu'),
  tf.keras.layers.Dense(50, activation='sigmoid'),

  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile & train
model.compile(
  optimizer=tf.keras.optimizers.Adam(),
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=100)

# Evaluate
print("Test accuracy:", model.evaluate(X_test, y_test)[1])

model.save('digit_recognizer_tf')