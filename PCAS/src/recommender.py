def recommend_top3_for_user(user, df, interest_to_activity):
    """
    Génère 3 nouvelles recommandations pour un utilisateur.
    
    - user : ligne du DataFrame (pd.Series) avec ses intérêts et activités
    - df : dataset complet
    - interest_to_activity : mapping intérêt → activité
    """
    user_interests = set(user['interests'])
    user_activities = set(user['activity_log'])
    
    # 1️⃣ Considérer les autres utilisateurs
    other_users = df[df['name'] != user['name']]
    
    # 2️⃣ Calculer la moyenne d'apparition des activités pour chaque intérêt
    interest_scores = {}
    for interest in interest_to_activity:
        if interest not in user_interests:
            # Moyenne d'apparition de l'activité correspondant à cet intérêt
            activity = interest_to_activity[interest]
            count = other_users['activity_log'].apply(lambda x: x.count(activity)).mean()
            interest_scores[interest] = count
    
    # 3️⃣ Trier par score décroissant et prendre les 3 premiers
    top3_interests = sorted(interest_scores, key=interest_scores.get, reverse=True)[:3]
    
    # Retourner les activités correspondantes
    recommendations = [interest_to_activity[i] for i in top3_interests]
    
    return recommendations

