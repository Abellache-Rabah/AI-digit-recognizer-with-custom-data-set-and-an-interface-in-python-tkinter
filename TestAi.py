import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('digit_recognizer_tf')

input_vector =[45, 21, 34, 0, 0, 11, 24, 47, 0, 0, 0, 12, 26, 0, 0, 12, 34, 0, 0, 11, 38, 28, 22, 30, 24]

input_data = np.array([input_vector])  

predictions = model.predict(input_data)

index = np.argmax(predictions[0]) 
print(index)


print("acc :" , predictions[0][index])

