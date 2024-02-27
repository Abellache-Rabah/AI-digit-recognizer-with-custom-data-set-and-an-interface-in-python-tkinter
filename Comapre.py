import numpy as np 
import json
from scipy.spatial.distance import cdist  

with open('data.json') as f:
    dataset = json.load(f)

train_vectors = np.array([sample['vector'] for sample in dataset])
train_labels = np.array([sample['label'] for sample in dataset])

new_vector = [0, 25, 36, 22, 38, 25, 10, 0, 0, 30, 27, 0, 0, 0, 31, 21, 0, 0, 21, 11, 35, 21, 30, 16, 0]

distances = cdist([new_vector], train_vectors)[0]

nearest_idx = np.argmin(distances)

# Look up label 
nearest_label = train_labels[nearest_idx] 
print("Nearest match label:", nearest_label)