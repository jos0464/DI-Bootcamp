from generate_data import generate_users
from analysis import analyze_data
from visualization import plot_interests, plot_interests_pie, plot_activity_heatmap
from recommender import recommend_top3_for_user
from collections import Counter

# -------------------------------
# 0️⃣ Définir les intérêts et mapping
# -------------------------------
interests_list = [
    "technology 1", "fitness 2", "music 3", "art 4", "gaming 5",
    "science 6", "reading 7", "cooking 8", "sports 9", "photography 10",
    "travel 11", "movies 12", "writing 13", "gardening 14", "dancing 15"
]

interest_to_activity = {interest: f"Activity {i+1}" for i, interest in enumerate(interests_list)}

print("Mapping intérêt → activité :")
for interest, activity in interest_to_activity.items():
    print(f"{interest} → {activity}")

# -------------------------------
# 1️⃣ Générer dataset
# -------------------------------
df = generate_users()

# -------------------------------
# 2️⃣ Analyser dataset
# -------------------------------
df, interests_count = analyze_data()

# -------------------------------
# Compter toutes les activités
# -------------------------------
all_activities = [act for sublist in df['activity_log'] for act in sublist]
activity_counts = Counter(all_activities)
top_5_activities = activity_counts.most_common()
print("Interests counter :", interests_count)
print("Activities counter :", top_5_activities)

# -------------------------------
# 3️⃣ Visualisations
# -------------------------------
plot_interests(interests_count)
plot_interests_pie(interests_count)
#plot_activity_heatmap(df)

# -------------------------------
# 4️⃣ Recommandations pour chaque utilisateur
# -------------------------------
df['recommended_activities'] = None

for idx, user in df.iterrows():
    reco = recommend_top3_for_user(user, df, interest_to_activity)
    df.at[idx, 'recommended_activities'] = reco
    print(f"Recommandations pour {user['name']}: {reco}")

# -------------------------------
# 5️⃣ Vérification
# -------------------------------
print(df[['name', 'interests', 'activity_log', 'recommended_activities']].head())
