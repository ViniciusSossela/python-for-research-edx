# DO NOT EDIT
import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


# Exercise 1
import pandas as pd

df = pd.read_csv('https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@wine.csv')
print(numeric_data.head())


# Exercise 2
numeric_data = df.rename(columns={"color": "is_red"})
numeric_data.loc[numeric_data.is_red == 'red', 'is_red'] = 1
numeric_data.loc[numeric_data.is_red == 'white', 'is_red'] = 0

numeric_data[numeric_data.is_red == 1].count()


# Exercise 3
import sklearn.preprocessing as sp
scaled_data = sp.scale(numeric_data)
numeric_data = pd.DataFrame(data = scaled_data, columns = numeric_data.columns)

import sklearn.decomposition as sd
pca = sd.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)


# Exercise 4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2, c = numeric_data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


# Exercise 5
from sklearn.metrics import accuracy_score
import numpy as np 
np.random.seed(1) # do not change

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)

def accuracy(predictions, outcomes):
    return accuracy_score(predictions, outcomes) * 100

accuracy(x,y)
    

# Exercise 6
predictions = [0] * len(df['high_quality'])
accuracy(predictions, df['high_quality'])
    

# Exercise 7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, df['high_quality'])
library_predictions = knn.predict(numeric_data)
accuracy(library_predictions, df['high_quality'])


# Exercise 8
n_rows = df.shape[0]
import random

random.seed(123)
selection = random.sample(range(n_rows), 10)

print(selection)


# Exercise 9
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(df["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]]
percentage = accuracy(my_predictions, df.high_quality[selection])

print(percentage)