import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------------------
# Histogramme des intérêts
# -------------------------------
def plot_interests(interests_count):
    categories = list(interests_count.keys())
    counts = list(interests_count.values())
    
    plt.figure(figsize=(8,5))
    plt.barh(categories, counts, color='skyblue')  # Histogramme horizontal
    plt.title("Distribution of Interests (Horizontal Bar Chart)")
    plt.xlabel("Number of Users")
    plt.ylabel("Interest Categories")
    plt.tight_layout()
    plt.show()
    
# -------------------------------
# Pie chart des intérêts
# -------------------------------
def plot_interests_pie(interests_count):
    labels = list(interests_count.keys())
    sizes = list(interests_count.values())
    
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribution of Interests (Pie Chart)")
    plt.show()

# -------------------------------
# Heatmap des activités
# -------------------------------
def plot_activity_heatmap(df):
    """
    Affiche une heatmap de l'intensité des activités par utilisateur.
    """
    # Préparer un dataframe utilisateur x activité
    activity_set = sorted(list({act for acts in df['activity_log'] for act in acts}))
    heat_data = pd.DataFrame(0, index=df['name'], columns=activity_set)
    
    for idx, row in df.iterrows():
        for act in row['activity_log']:
            heat_data.loc[row['name'], act] += 1
    
    plt.figure(figsize=(10,6))
    sns.heatmap(heat_data, annot=True, cmap='Blues', cbar_kws={'label': 'Activity Count'})
    plt.title("User Activity Heatmap")
    plt.ylabel("User")
    plt.xlabel("Activity")
    plt.tight_layout()
    plt.show()
