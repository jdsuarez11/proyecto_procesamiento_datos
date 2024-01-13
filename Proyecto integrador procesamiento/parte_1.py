from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset['train']
age = np.array(data['age'])
print(age.mean())
