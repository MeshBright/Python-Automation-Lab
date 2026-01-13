import numpy as np

# data = np.zeros((10, 10))
# data_count = data.shape[0]
#for i in range(data_count):
#    data[i] = i

#modified_data = data[[4, 5, 6, 7]]
#print(modified_data)
#print(data)

data_1 = np.array([3, 4, 5, 6])
data_2 = np.array([7, 8, 9, 10])
print(np.concatenate((data_1, data_2)))

