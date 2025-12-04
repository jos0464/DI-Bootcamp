import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Données d'exemple
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Ajouter l'intercept pour statsmodels
X_const = sm.add_constant(X)

# Créer le modèle OLS (Ordinary Least Squares)
model = sm.OLS(y, X_const).fit()

# Prédictions
y_pred = model.predict(X_const)

# Afficher résumé statistique
print(model.summary())

# Visualisation
plt.scatter(X, y, color='blue', label='Données réelles')
plt.plot(X, y_pred, color='red', label='Régression linéaire')

# Ajouter R² sur le graphique
plt.text(1, 5.2, f"R² = {model.rsquared:.2f}", fontsize=12)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Régression linéaire avec R²')
plt.legend()
plt.show()
