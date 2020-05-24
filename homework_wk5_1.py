# Exercise 1
import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)

df.head()
df.head()["original_title"]


# Exercise 2
df.loc[df["revenue"] >  df["budget"],"profitable"] = 1
df.loc[df["revenue"] <=  df["budget"],"profitable"] = 0
df["profitable"] = pd.to_numeric(df["profitable"]).astype(int)
regression_target = "revenue"
classification_target = "profitable"


len(df.loc[df["profitable"] == 1]) 
len(df.loc[df["profitable"] == 0])

df["profitable"].head()


# Exercise 3
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

len(df)
print(df)


# Exercise 4
unique_genres = []

for genre_row in df["genres"]:
    genres = genre_row.split(",")
    for genre in genres:
        if genre.strip() not in unique_genres:
            unique_genres.append(genre.strip())
            

for genre in unique_genres:
    df[genre] = df['genres'].str.contains(genre).astype(int)


print(df["genres"].head())
len(unique_genres)


# Exercise 5
continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]

axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
       color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))

plt.tight_layout()
plt.show() 

df[outcomes_and_continuous_covariates].skew()


# Exercise 6
df.budget = np.log10(1 + df.budget)
df.popularity = np.log10(1 + df.popularity)
df.runtime = np.log10(1 + df.runtime)
df.vote_count = np.log10(1 + df.vote_count)
df.revenue = np.log10(1 + df.revenue)

df[outcomes_and_continuous_covariates].skew()


# Exercise 7
df.to_csv("movies_clean.csv")