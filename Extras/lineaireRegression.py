import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# =========================
# 1. Exemple de dataset
# =========================
# Remplacez ces données par votre dataset réel
X = np.array([[1, 2],
              [2, 3],
              [3, 4],
              [4, 5],
              [5, 6]])  # Variables indépendantes
y = np.array([2, 3, 5, 4, 6])  # Variable dépendante

n = X.shape[0]  # nombre d'observations
k = X.shape[1]  # nombre de variables indépendantes

# =========================
# 2. Ajouter l'intercept
# =========================
X_const = np.hstack([np.ones((n, 1)), X])  # colonne de 1 pour theta0

# =========================
# 3. Calculer les coefficients (theta) avec pseudo-inverse
# =========================
theta = np.linalg.pinv(X_const) @ y  # Utilisation de la pseudo-inverse
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
SE = np.sqrt(np.diag(var_theta))  # Erreur standard

t_stats = theta / SE  # t-statistics
p_values = [2 * (1 - t.cdf(np.abs(ti), df=n-k-1)) for ti in t_stats]
print("p-values:", p_values)

# =========================
# 8. Visualisation (si 1 seule feature)
# =========================
if k == 1:
    plt.scatter(X, y, color='blue', label='Données réelles')
    plt.plot(X, y_pred, color='red', label='Régression linéaire')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Régression linéaire')
    plt.text(X.min(), y.max(), f"R² = {R2:.2f}", fontsize=12)
    plt.legend()
    plt.show()

# =========================
# 9. Visualisation des résidus
# =========================
plt.scatter(y_pred, y - y_pred, color='purple')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('y_pred')
plt.ylabel('Résidus')
plt.title('Résidus de la régression')
plt.show()
