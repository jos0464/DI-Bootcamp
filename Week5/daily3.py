# 📦 Import des bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Modèles
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from IPython.display import display



# 🔹 Charger le dataset
df = pd.read_csv('breast_cancer_data.csv')  # adapte le nom du fichier
print("Taille du dataset :", df.shape)
display(df.head())

# 1️⃣ Nettoyage et prétraitement
# Supprimer colonne inutile
if 'Unnamed: 32' in df.columns:
    df.drop('Unnamed: 32', axis=1, inplace=True)

# Supprimer lignes avec NaN
df.dropna(how='any', inplace=True)

print("Taille après nettoyage :", df.shape)
print("Valeurs manquantes :\n", df.isnull().sum())

# Convertir la cible 'diagnosis' en numérique : M -> 1, B -> 0
df['diagnosis'] = df['diagnosis'].map({'M':1, 'B':0})

# Visualisation : distribution de la cible
sns.countplot(x='diagnosis', data=df, palette='magma')
plt.title("Distribution des diagnostics (0=B, 1=M)")
plt.show()

# Séparer features / target
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

print("Taille X :", X.shape)
print("Taille y :", y.shape)

# Normalisation des features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2️⃣ Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 3️⃣ Entraîner et évaluer les modèles

# 🔹 Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# 🔹 K Nearest Neighbours
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))

# 🔹 Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# 🔹 Support Vector Machine
svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))

# 🔹 Comparaison des modèles
results = {
    'Logistic Regression': accuracy_score(y_test, y_pred_lr),
    'KNN': accuracy_score(y_test, y_pred_knn),
    'Random Forest': accuracy_score(y_test, y_pred_rf),
    'SVM': accuracy_score(y_test, y_pred_svm)
}

best_model = max(results, key=results.get)
print("\nMeilleur modèle :", best_model, "avec une accuracy de", results[best_model])
