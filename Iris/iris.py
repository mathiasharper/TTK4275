import pandas as pd
import numpy as np

class_1 = []
class_2 = []
class_3 = []

with open("class_1") as f:
    data = f.readlines()
    for line in data:
        class_1.append([float(line[0:3]), float(line[4:7]), float(line[8:11]), float(line[12:15])])
class_1 = np.array(class_1)

with open("class_2") as f:
    data = f.readlines()
    for line in data:
        class_2.append([float(line[0:3]), float(line[4:7]), float(line[8:11]), float(line[12:15])])
class_2 = np.array(class_2)

with open("class_3") as f:
    data = f.readlines()
    for line in data:
        class_3.append([float(line[0:3]), float(line[4:7]), float(line[8:11]), float(line[12:15])])
class_3 = np.array(class_3)


train_1 = class_1[:30]
train_2 = class_2[:30]
train_3 = class_3[:30]

test_1 = class_1[30:50]
test_2 = class_2[30:50]
test_3 = class_3[30:50]

train = [train_1, train_2, train_3]
test = [test_1, test_2, test_3]

X = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(np.exp(X))