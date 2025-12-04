import pandas as pd
import numpy as np
from scipy import stats
import os

def analyze_data(filepath=None):
    if filepath is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir, "../data/users.csv")
    
    df = pd.read_csv(filepath)
    
    # Convertir les strings en listes Python
    df['interests'] = df['interests'].apply(lambda x: x.strip("[]").replace("'", "").split(", "))
    df['activity_log'] = df['activity_log'].apply(lambda x: x.strip("[]").replace("'", "").split(", "))
    
    # Analyse des âges
    mean_age = df['age'].mean()
    median_age = df['age'].median()
    
    # Chi-square pour intérêts
    all_interests = sum(df['interests'].tolist(), [])
    unique, counts = np.unique(all_interests, return_counts=True)
    chi2_stat, p_val = stats.chisquare(counts)
    
    print("Age: mean =", mean_age, ", median =", median_age)
    print("Interests distribution:", dict(zip(unique, counts)))
    print("Chi-square:", chi2_stat, ", p-value:", p_val)
    
    return df, dict(zip(unique, counts))
