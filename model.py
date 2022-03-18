import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


df = pd.read_csv("carsdataset.csv")
df = df[["wheelbase", "carlength", 
             "carwidth", "carheight", "curbweight", 
             "enginesize", "boreratio", "stroke", 
             "compressionratio", "horsepower", "peakrpm", 
              "price"]]
x = np.array(df.drop(['price'], axis=1))
y = np.array(df['price'])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)
model.score(xtest, predictions)

pickle_out = open("classifier.pkl", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()