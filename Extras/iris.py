# 1️⃣ Importation des librairies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 2️⃣ Chargement du dataset Iris
from sklearn.datasets import load_iris
iris = load_iris()

# Conversion en DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("🔹 Aperçu des données :")
print(df.head())

# 3️⃣ Analyse exploratoire
sns.pairplot(df, hue="species", diag_kind="hist")
plt.suptitle("Relations entre les caractéristiques", y=1.02)
plt.show()

# 4️⃣ Séparation des features et des labels
X = df.drop(columns=["species"])
y = df["species"]

# 5️⃣ Division train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6️⃣ Normalisation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7️⃣ Entraînement du modèle
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# 8️⃣ Évaluation
y_pred = model.predict(X_test_scaled)

print("\n✅ Précision :", accuracy_score(y_test, y_pred))
print("\n📋 Rapport de classification :\n", classification_report(y_test, y_pred))
print("\n🧩 Matrice de confusion :\n", confusion_matrix(y_test, y_pred))

# 9️⃣ Visualisation de la matrice de confusion
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap="Blues",
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.title("Matrice de confusion - Iris")
plt.show()
