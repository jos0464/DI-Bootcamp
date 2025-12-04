from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
from scipy import stats
import io
import matplotlib.pyplot as plt
import base64
import ast

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# -----------------------------
# VARIABLE GLOBALE
# -----------------------------
data_df = None

# -----------------------------
# UTILITAIRES
# -----------------------------
def get_numeric_data():
    global data_df
    if data_df is None:
        return None
    return data_df.select_dtypes(include="number")

def dict_to_html_table(title, data_dict):
    df = pd.DataFrame(list(data_dict.items()), columns=["Colonne", title])
    return df.to_html(classes="table table-bordered table-striped", index=False)

def plot_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches='tight')
    buffer.seek(0)
    img_b64 = base64.b64encode(buffer.read()).decode("utf-8")
    plt.close()
    return img_b64

def html_result(title, params_dict, sample=None, plot=False):
    html = dict_to_html_table(title, params_dict)
    if sample is not None:
        df_sample = pd.DataFrame({"Sample": sample}).to_html(classes="table table-striped", index=False)
        html += f"<h4>Échantillon</h4>{df_sample}"
    if plot:
        plt.figure(figsize=(5,4))
        if sample is not None:
            plt.hist(sample, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        img_b64 = plot_to_base64()
        html += f'<h4>Distribution</h4><img src="data:image/png;base64,{img_b64}" width="400">'
    return html

# -----------------------------
# PAGE PRINCIPALE
# -----------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "columns": [], "result": None})

# -----------------------------
# UPLOAD CSV
# -----------------------------
@app.post("/upload-csv/", response_class=HTMLResponse)
async def upload_csv(request: Request, file: UploadFile = File(...)):
    global data_df
    data_df = pd.read_csv(file.file)
    numeric_cols = get_numeric_data().columns.tolist()
    return templates.TemplateResponse("index.html", {"request": request, "columns": numeric_cols, "result": "<b>CSV chargé !</b>"})

# -----------------------------
# SAISIE ARRAY MANUEL
# -----------------------------
@app.post("/input-array/", response_class=HTMLResponse)
async def input_array(request: Request, array_text: str = Form(...)):
    global data_df
    try:
        array = ast.literal_eval(array_text)  # Convertir string en list
        data_df = pd.DataFrame({"Col1": array})
        numeric_cols = get_numeric_data().columns.tolist()
        return templates.TemplateResponse("index.html", {"request": request, "columns": numeric_cols, "result": "<b>Données chargées depuis array !</b>"})
    except:
        return templates.TemplateResponse("index.html", {"request": request, "columns": [], "result": "<b>Erreur dans la saisie !</b>"})


# -----------------------------
# STATISTIQUES DESCRIPTIVES
# -----------------------------
@app.get("/mean", response_class=HTMLResponse)
def calc_mean(request: Request):
    data = get_numeric_data()
    if data is None: return templates.TemplateResponse("index.html", {"request": request, "columns": [], "result": "Upload CSV ou saisie array d'abord !"})
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Moyenne", data.mean().to_dict(), plot=True)})

@app.get("/median", response_class=HTMLResponse)
def calc_median(request: Request):
    data = get_numeric_data()
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Médiane", data.median().to_dict(), plot=True)})

@app.get("/mode", response_class=HTMLResponse)
def calc_mode(request: Request):
    data = get_numeric_data()
    mode_values = {col: stats.mode(data[col], keepdims=True)[0][0] for col in data.columns}
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Mode", mode_values, plot=True)})

@app.get("/variance", response_class=HTMLResponse)
def calc_variance(request: Request):
    data = get_numeric_data()
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Variance", data.var().to_dict(), plot=True)})

@app.get("/std", response_class=HTMLResponse)
def calc_std(request: Request):
    data = get_numeric_data()
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Écart-type", data.std().to_dict(), plot=True)})

@app.get("/range", response_class=HTMLResponse)
def calc_range(request: Request):
    data = get_numeric_data()
    range_values = (data.max() - data.min()).to_dict()
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Étendue", range_values, plot=True)})

@app.get("/quartiles", response_class=HTMLResponse)
def calc_quartiles(request: Request):
    data = get_numeric_data()
    q1 = data.quantile(0.25).to_dict()
    q3 = data.quantile(0.75).to_dict()
    result = {col: f"Q1={q1[col]} | Q3={q3[col]}" for col in data.columns}
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Quartiles", result, plot=True)})

@app.get("/iqr", response_class=HTMLResponse)
def calc_iqr(request: Request):
    data = get_numeric_data()
    iqr_values = (data.quantile(0.75) - data.quantile(0.25)).to_dict()
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("IQR", iqr_values, plot=True)})


# -----------------------------
# DISTRIBUTIONS PROBABILITÉ
# -----------------------------
@app.get("/normale", response_class=HTMLResponse)
def dist_normale(request: Request):
    data = get_numeric_data()
    if data is None: return templates.TemplateResponse("index.html", {"request": request, "columns": [], "result": "Upload CSV ou saisie array d'abord !"})
    col = data.columns[0]  # utiliser la première colonne pour exemple
    sample = data[col].values
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    plt.hist(sample, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    return templates.TemplateResponse("index.html", {"request": request, "columns": data.columns.tolist(), "result": html_result("Distribution Normale (fit)", {"mean": mean, "std": std}, sample, plot=True)})

# Les autres distributions peuvent être ajoutées de la même façon :
# Bernoulli, Binomiale, Poisson, Uniforme, Exponentielle...
