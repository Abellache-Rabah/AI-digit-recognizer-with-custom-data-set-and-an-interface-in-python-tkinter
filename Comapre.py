import numpy as np 
import json
from scipy.spatial.distance import cdist  

with open('data.json') as f:
    dataset = json.load(f)

train_vectors = np.array([sample['vector'] for sample in dataset])
train_labels = np.array([sample['label'] for sample in dataset])

new_vector = [0, 0, 28, 34, 0, 0, 0, 22, 41, 5, 0, 0, 1, 31, 5, 22, 9, 31, 4, 6, 36, 48, 31, 25, 22]

distances = cdist([new_vector], train_vectors)[0]

nearest_idx = np.argmin(distances)

# Look up label 
nearest_label = train_labels[nearest_idx] 
print("Nearest match label:", nearest_label)