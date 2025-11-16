import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t

# =========================
# 1. Charger le dataset CSV
# =========================
# Remplacez 'data.csv' par le chemin de votre fichier
# La colonne cible doit s'appeler 'y', et les features toutes les autres colonnes
df = pd.read_csv('data.csv')

# Séparer X et y
y = df['y'].values
X = df.drop(columns=['y']).values

n = X.shape[0]  # nombre d'observations
k = X.shape[1]  # nombre de features

# =========================
# 2. Ajouter l'intercept
# =========================
X_const = np.hstack([np.ones((n, 1)), X])  # colonne de 1 pour theta0

# =========================
# 3. Calculer les coefficients (theta) avec pseudo-inverse
# =========================
theta = np.linalg.pinv(X_const) @ y
print("Coefficients (theta0, theta1,...):", theta)

# =========================
# 4. Prédictions
# =========================
y_pred = X_const @ theta

# =========================
# 5. Calculer R²
# =========================
SS_res = np.sum((y - y_pred) ** 2)
SS_tot = np.sum((y - np.mean(y)) ** 2)
R2 = 1 - SS_res / SS_tot
print("R²:", R2)

# =========================
# 6. Calculer F-statistic
# =========================
SS_reg = SS_tot - SS_res
F = (SS_reg / k) / (SS_res / (n - k - 1))
print("F-statistic:", F)

# =========================
# 7. Calculer p-values
# =========================
MSE = SS_res / (n - k - 1)  # Mean Squared Error
var_theta = MSE * np.linalg.pinv(X_const.T @ X_const)
SE = np.sqrt(np.diag(var_theta))

t_stats = theta / SE
p_values = [2 * (1 - t.cdf(np.abs(ti), df=n-k-1)) for ti in t_stats]
print("p-values:", p_values)

# =========================
# 8. Résumé clair des résultats
# =========================
feature_names = ['Intercept'] + list(df.drop(columns=['y']).columns)
print("\n--- Résultats de la régression ---")
for i, name in enumerate(feature_names):
    print(f"{name}: Coefficient = {theta[i]:.4f}, p-value = {p_values[i]:.4f}")

# =========================
# 9. Visualisation (si une seule feature)
# =========================
if k == 1:
    plt.scatter(X, y, color='blue', label='Données réelles')
    plt.plot(X, y_pred, color='red', label='Régression linéaire')
    plt.xlabel(df.drop(columns=['y']).columns[0])
    plt.ylabel('y')
    plt.title('Régression linéaire')
    plt.text(X.min(), y.max(), f"R² = {R2:.2f}", fontsize=12)
    plt.legend()
    plt.show()

# =========================
# 10. Visualisation des résidus
# =========================
plt.scatter(y_pred, y - y_pred, color='purple')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('y_pred')
plt.ylabel('Résidus')
plt.title('Résidus de la régression')
plt.show()
