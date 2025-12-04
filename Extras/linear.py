import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Créer un mini dataset
x = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
y = np.array([2, 4, 6, 8, 10])

# Créer et entraîner un modèle simple
model = LinearRegression()
model.fit(x, y)

print("Prédiction pour 6 :", model.predict([[6]]))
