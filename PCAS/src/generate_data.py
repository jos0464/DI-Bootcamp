import os
import numpy as np
import pandas as pd

def generate_users(num_users=50):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "../data")
    os.makedirs(data_dir, exist_ok=True)

    names = [f"User{i}" for i in range(1, num_users+1)]
    ages = np.random.randint(18, 60, size=num_users)

    # 15 intérêts réels
    interests_list = [
        "technology 1", "fitness 2", "music 3", "art 4", "gaming 5",
        "science 6", "reading 7", "cooking 8", "sports 9", "photography 10",
        "travel 11", "movies 12", "writing 13", "gardening 14", "dancing 15"
    ]

    # Mapping intérêt → activité correspondante
    interest_to_activity = {interest: f"Activity {i+1}" for i, interest in enumerate(interests_list)}

    # Affichage du mapping pour référence
    print("Mapping intérêt → activité :")
    for interest, activity in interest_to_activity.items():
        print(f"{interest} → {activity}")

    data = []
    for i in range(num_users):
        # 1 à 3 intérêts choisis aléatoirement
        interests = list(np.random.choice(interests_list, size=np.random.randint(1,4), replace=False))
        
        # Générer les activités correspondantes aux intérêts choisis
        activity_log = []
        for interest in interests:
            activity_log += [interest_to_activity[interest] for _ in range(np.random.randint(1,3))]
        
        data.append({
            "name": names[i],
            "age": ages[i],
            "interests": interests,
            "activity_log": activity_log
        })

    df = pd.DataFrame(data)

    # Sauvegarder le CSV
    df.to_csv(os.path.join(data_dir, "users.csv"), index=False)
    print("\nDataset generated: users.csv")
    return df

# Exemple d'utilisation
if __name__ == "__main__":
    df = generate_users(50)
    print(df.head())
