import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('digit_recognizer_tf')

# Input vector 
input_vector = [0, 26, 26, 21, 33, 23, 17, 0, 0, 29, 44, 24, 0, 0, 33, 50, 0, 0, 6, 30, 19, 27, 26, 27, 0]

# Wrap input vector in a numpy array  
input_data = np.array([input_vector])  

# Now pass this to model.predict 
predictions = model.predict(input_data)

# Print prediction
index = np.argmax(predictions[0]) 
print(index)


print("acc :" , predictions[0][index])

