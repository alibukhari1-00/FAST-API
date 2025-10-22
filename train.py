# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset (in real case, load a CSV file)
data = {
    'area_sqft': [500, 700, 900, 1200, 1500, 1800],
    'bedrooms': [1, 2, 2, 3, 3, 4],
    'age': [10, 15, 20, 5, 8, 12],
    'price': [150000, 200000, 250000, 300000, 350000, 400000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['area_sqft', 'bedrooms', 'age']]
y = df['price']

# Train model
model=LinearRegression()
model.fit(X, y)

pickle_model_path="model.pkl"
with open(pickle_model_path,"wb") as f:
    pickle.dump(model,f)