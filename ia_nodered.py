"""
Script IA — Détection d'anomalies en temps réel
Utilisé par Node-RED via le nœud 'exec'
Lit les données depuis stdin
"""

import sys
import json
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# ── DONNÉES D'ENTRAÎNEMENT ────────────────────
np.random.seed(42)
n = 500
X_train = np.column_stack([
    np.random.uniform(18, 28, n),
    np.random.choice([0, 1], n, p=[0.7, 0.3]),
    np.random.choice([0, 1], n, p=[0.8, 0.2]),
    np.random.choice([0, 1], n, p=[0.98, 0.02])
])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
model = IsolationForest(n_estimators=100, contamination=0.15, random_state=42)
model.fit(X_scaled)

# ── LECTURE DONNÉES (stdin OU argv) ──────────
try:
    raw = ""

    # Essayer stdin d'abord
    if not sys.stdin.isatty():
        raw = sys.stdin.read().strip()

    # Sinon utiliser argv
    if not raw and len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:]).strip()

    if not raw:
        raise ValueError("Aucune donnée reçue")

    # Nettoyer le JSON
    raw = raw.strip().strip("'\"")
    data = json.loads(raw)

    temperature = float(data.get("temperature", 22))
    mouvement   = int(data.get("mouvement", 0))
    porte       = int(data.get("porte", 0))
    fumee       = int(data.get("fumee", 0))

    # ── PRÉDICTION ────────────────────────────
    X_test = np.array([[temperature, mouvement, porte, fumee]])
    X_test_scaled = scaler.transform(X_test)

    prediction = int(model.predict(X_test_scaled)[0])
    score = float(model.score_samples(X_test_scaled)[0])
    anomalie = bool(score < -0.50)

    # ── TYPE D'ATTAQUE ────────────────────────
    type_attaque = "normal"
    niveau = "NORMAL"

    if anomalie:
        if temperature > 40 and mouvement == 0:
            type_attaque = "spoofing_temperature"
            niveau = "DANGER"
        elif mouvement == 1 and porte == 1 and fumee == 1:
            type_attaque = "injection_donnees"
            niveau = "CRITIQUE"
        elif mouvement == 1 and porte == 1 and temperature < 18:
            type_attaque = "intrusion"
            niveau = "DANGER"
        else:
            type_attaque = "anomalie_inconnue"
            niveau = "WARNING"

    resultat = {
        "anomalie": anomalie,
        "score": round(score, 4),
        "niveau": niveau,
        "type_attaque": type_attaque,
        "donnees": {
            "temperature": temperature,
            "mouvement": mouvement,
            "porte": porte,
            "fumee": fumee
        }
    }

    print(json.dumps(resultat))

except Exception as e:
    print(json.dumps({
        "anomalie": False,
        "score": 0,
        "niveau": "ERROR",
        "type_attaque": "erreur",
        "erreur": str(e)
    }))
