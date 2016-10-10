import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('file:///Users/dlin/Projects/test/iris.data', header=None)

#df = pd.read_csv('https://archive.ics.uci.edu/ml/'
#        'machine-learning-databases/iris/iris.data', header=None)
#print(df.tail())

y = df.iloc[0:100,4].values
#print(y)
y = np.where(y == "Iris-setosa", -1, 1)
#print(y)
X = df.iloc[0:100, [0, 2]].values
#print(X)

w_ = np.zeros(1 + X.shape[1])
print(w_)

for xi, target in zip(X, y):
	print(xi, target);
	update = 3;
	w_[1:] += update * xi
	w_[0] += update
	print(w_)


#    update = self.eta * (target - self.predict(xi))
#    self.w_[1:] += update * xi
#    self.w_[0] += update
#    errors += int(update != 0.0)