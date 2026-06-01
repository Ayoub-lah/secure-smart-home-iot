"""
Secure Smart Home — Détection de cyberattaques par IA
Module : IoT et Applications — Master SBD S2
Pr. M. EL BRAK | FST Tanger 2025/2026
"""

import json
import random
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# ─────────────────────────────────────────────
# 1. GÉNÉRATION DE DONNÉES D'ENTRAÎNEMENT
# ─────────────────────────────────────────────

def generer_donnees_normales(n=500):
    """Simule des données IoT normales d'une maison intelligente"""
    data = {
        "temperature": np.random.uniform(18, 28, n),        # normale : 18-28°C
        "mouvement":   np.random.choice([0, 1], n, p=[0.7, 0.3]),  # 30% détection
        "porte":       np.random.choice([0, 1], n, p=[0.8, 0.2]),  # 20% ouverte
        "fumee":       np.random.choice([0, 1], n, p=[0.98, 0.02]) # 2% fumée
    }
    return pd.DataFrame(data)

def generer_attaques(n=50):
    """Simule des cyberattaques / comportements anormaux"""
    attaques = []
    
    for _ in range(n):
        type_attaque = random.choice(["spoofing_temp", "injection", "intrusion"])
        
        if type_attaque == "spoofing_temp":
            # Injection de fausse température très haute
            attaques.append({
                "temperature": random.uniform(60, 90),
                "mouvement": 0,
                "porte": 0,
                "fumee": 0,
                "type": type_attaque
            })
        elif type_attaque == "injection":
            # Toutes les valeurs à 1 simultanément (impossible en conditions normales)
            attaques.append({
                "temperature": random.uniform(45, 60),
                "mouvement": 1,
                "porte": 1,
                "fumee": 1,
                "type": type_attaque
            })
        elif type_attaque == "intrusion":
            # Mouvement + porte ouverte la nuit (valeurs hors plage normale)
            attaques.append({
                "temperature": random.uniform(15, 17),
                "mouvement": 1,
                "porte": 1,
                "fumee": 0,
                "type": type_attaque
            })
    
    return pd.DataFrame(attaques)

# ─────────────────────────────────────────────
# 2. ENTRAÎNEMENT DU MODÈLE
# ─────────────────────────────────────────────

print("=" * 55)
print("  🏠 Secure Smart Home — Détection d'Anomalies IA")
print("=" * 55)

# Générer les données
df_normal = generer_donnees_normales(500)
df_attaques = generer_attaques(50)

print(f"\n✅ Données normales générées     : {len(df_normal)} échantillons")
print(f"🚨 Données attaques générées     : {len(df_attaques)} échantillons")

# Préparer les features pour l'entraînement
features = ["temperature", "mouvement", "porte", "fumee"]
X_train = df_normal[features].values

# Normaliser les données
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Entraîner le modèle Isolation Forest
print("\n🤖 Entraînement du modèle Isolation Forest...")
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,   # On s'attend à 5% d'anomalies
    random_state=42
)
model.fit(X_train_scaled)
print("✅ Modèle entraîné avec succès !")

# ─────────────────────────────────────────────
# 3. ÉVALUATION SUR LES ATTAQUES SIMULÉES
# ─────────────────────────────────────────────

print("\n" + "-" * 55)
print("  🔍 TEST SUR DONNÉES D'ATTAQUES SIMULÉES")
print("-" * 55)

X_attaques = df_attaques[features].values
X_attaques_scaled = scaler.transform(X_attaques)
predictions = model.predict(X_attaques_scaled)
scores = model.score_samples(X_attaques_scaled)

detectees = sum(1 for p in predictions if p == -1)
print(f"\n📊 Résultats de détection :")
print(f"   Total attaques testées  : {len(predictions)}")
print(f"   ✅ Anomalies détectées  : {detectees}")
print(f"   ❌ Non détectées        : {len(predictions) - detectees}")
print(f"   🎯 Taux de détection    : {(detectees/len(predictions)*100):.1f}%")

# Détail par type
print("\n📋 Détail par type d'attaque :")
for i, row in df_attaques.iterrows():
    label = "🔴 ANOMALIE" if predictions[i] == -1 else "🟢 NORMAL  "
    print(f"   {label} | {row['type']:<20} | T={row['temperature']:.1f}°C | score={scores[i]:.3f}")

# ─────────────────────────────────────────────
# 4. SIMULATION EN TEMPS RÉEL (depuis MQTT)
# ─────────────────────────────────────────────

def analyser_message_mqtt(payload_json: str) -> dict:
    """
    Analyser un message MQTT reçu depuis Node-RED.
    Retourne un dict avec le résultat de la détection.
    
    Utilisation dans Node-RED :
    - Nœud 'exec' : python ia_detection_anomalies.py
    - Ou via API Flask (voir bas du fichier)
    """
    try:
        data = json.loads(payload_json)
    except Exception:
        return {"erreur": "JSON invalide", "anomalie": False}

    # Construire le vecteur de features
    # Valeurs par défaut si capteur absent
    features_vec = np.array([[
        data.get("temperature", 22),
        data.get("mouvement", 0),
        data.get("porte", 0),
        data.get("fumee", 0)
    ]])

    features_scaled = scaler.transform(features_vec)
    prediction = model.predict(features_scaled)[0]
    score = float(model.score_samples(features_scaled)[0])

    resultat = {
        "timestamp": datetime.now().isoformat(),
        "anomalie": prediction == -1,
        "score": round(score, 4),
        "niveau": "DANGER" if prediction == -1 else "NORMAL",
        "donnees": data
    }
    return resultat

# ─────────────────────────────────────────────
# 5. TEST DE SIMULATION TEMPS RÉEL
# ─────────────────────────────────────────────

print("\n" + "-" * 55)
print("  ⚡ SIMULATION DÉTECTION TEMPS RÉEL")
print("-" * 55)

messages_test = [
    '{"temperature": 23.5, "mouvement": 0, "porte": 0, "fumee": 0}',  # Normal
    '{"temperature": 75.0, "mouvement": 0, "porte": 0, "fumee": 0}',  # Spoofing temp
    '{"temperature": 22.0, "mouvement": 1, "porte": 1, "fumee": 1}',  # Injection
    '{"temperature": 24.1, "mouvement": 1, "porte": 0, "fumee": 0}',  # Normal
    '{"temperature": 88.0, "mouvement": 1, "porte": 1, "fumee": 1}',  # Attaque totale
]

print()
for msg in messages_test:
    res = analyser_message_mqtt(msg)
    icone = "🔴 ALERTE  " if res["anomalie"] else "🟢 Normal  "
    data = res["donnees"]
    print(f"  {icone} | T={data.get('temperature')}°C | "
          f"Mvt={data.get('mouvement')} Porte={data.get('porte')} Fumée={data.get('fumee')} "
          f"| score={res['score']}")

print("\n✅ Module IA prêt. Intégration Node-RED via nœud 'exec' ou API Flask.")
print("=" * 55)
