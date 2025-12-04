import pandas as pd
import numpy as np
import io, base64
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 🔹 Lire CSV + analyse de base (head, describe, info)
# ---------------------------------------------------------
def read_csv(file) -> dict:
    """Lit un CSV, convertit intelligemment les types et renvoie df + head + describe + info."""
    df = pd.read_csv(file)

    # ---------- Nettoyage général des chaînes ----------
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str).str.replace(",", ".", regex=False).str.strip()

    # ---------- Conversion numérique sécurisée ----------
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors="ignore")
        except:
            pass

    # ---------- Détection dates (sécurisé, jamais d'erreur) ----------
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore", infer_datetime_format=True)
            except:
                pass

    # ---------- Détection automatique colonnes binaires ----------
    for col in df.columns:
        if df[col].dtype == object and df[col].nunique() == 2:
            df[col] = df[col].astype("category").cat.codes  # → 0/1

    # ---------- head ----------
    head = df.head().to_dict(orient="list")

    # ---------- describe ----------
    try:
        describe = df.describe(include="all").to_dict()
    except:
        describe = {"error": "describe() impossible sur ce fichier"}

    # ---------- info ----------
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    return {
        "df": df,
        "head": head,
        "describe": describe,
        "info": info_str
    }


# ---------------------------------------------------------
# 🔹 Statistiques avancées
# ---------------------------------------------------------
def calculate_statistics(df: pd.DataFrame) -> dict:
    numeric_cols = df.select_dtypes(include='number').columns
    stats = {}

    if len(numeric_cols) > 0:
        stats = df[numeric_cols].describe().to_dict()

        percentiles = [10, 25, 50, 75, 90]
        for col in numeric_cols:
            for p in percentiles:
                stats[col][f"p{p}"] = np.percentile(df[col], p)

    else:
        stats["message"] = "Aucune colonne numérique détectée dans ce CSV."

    return stats


# ---------------------------------------------------------
# 🔹 Graphiques (histogrammes, boxplots, heatmap, séries temporelles)
# ---------------------------------------------------------
def generate_plots(df: pd.DataFrame) -> dict:
    plots = {}
    numeric_cols = df.select_dtypes(include='number').columns
    date_cols = df.select_dtypes(include='datetime').columns

    # Histogrammes
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Histogramme de {col}")
        plots[f"{col}_hist"] = fig_to_base64(fig)

    # Boxplots
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.boxplot(y=df[col], ax=ax)
        ax.set_title(f"Boxplot de {col}")
        plots[f"{col}_box"] = fig_to_base64(fig)

    # Heatmap
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(6,5))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title("Heatmap de corrélation")
        plots["correlation"] = fig_to_base64(fig)

    # Séries temporelles
    for dcol in date_cols:
        for ncol in numeric_cols:
            fig, ax = plt.subplots(figsize=(7,3))
            sns.lineplot(data=df, x=dcol, y=ncol, marker='o', ax=ax)
            ax.set_title(f"{ncol} en fonction de {dcol}")
            plots[f"{ncol}_vs_{dcol}_line"] = fig_to_base64(fig)

    return plots


# ---------------------------------------------------------
# 🔹 Convertir un plot en base64
# ---------------------------------------------------------
def fig_to_base64(fig):
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close(fig)
    return img_str
