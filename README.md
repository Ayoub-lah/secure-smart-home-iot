# 🏠 Secure Smart Home — AI-based Cyberattack Detection in IoT Environment

<div align="center">

![IoT](https://img.shields.io/badge/IoT-Smart%20Home-blue?style=for-the-badge&logo=home-assistant)
![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-purple?style=for-the-badge&logo=eclipse-mosquitto)
![Node-RED](https://img.shields.io/badge/Node--RED-v4.1.8-red?style=for-the-badge&logo=nodered)
![Python](https://img.shields.io/badge/Python-3.14-yellow?style=for-the-badge&logo=python)
![Firebase](https://img.shields.io/badge/Firebase-Realtime%20DB-orange?style=for-the-badge&logo=firebase)
![ThingsBoard](https://img.shields.io/badge/ThingsBoard-Cloud-green?style=for-the-badge)
![AI](https://img.shields.io/badge/IA-Isolation%20Forest-red?style=for-the-badge&logo=scikit-learn)

**Master SBD S2 — Module IoT et Applications**  
**FST Tanger — Université Abdelmalek Essaâdi — 2025/2026**  
**Encadrant : Pr. M. EL BRAK**

</div>

---

## 📋 Table des matières

- [Description du projet](#-description-du-projet)
- [Architecture globale](#-architecture-globale)
- [Technologies utilisées](#-technologies-utilisées)
- [Prérequis](#-prérequis)
- [Installation et configuration](#-installation-et-configuration)
- [Lancer le projet](#-lancer-le-projet)
- [Tester le projet](#-tester-le-projet)
- [Fichiers du projet](#-fichiers-du-projet)
- [Partie IA — Isolation Forest](#-partie-ia--isolation-forest)
- [Cyberattaques détectées](#-cyberattaques-détectées)
- [Plateformes Cloud](#-plateformes-cloud)
- [Équipe](#-équipe)

---

## 📖 Description du projet

**Secure Smart Home** est un système IoT simulé de maison intelligente qui détecte automatiquement les **cyberattaques** sur ses capteurs IoT grâce à l'**Intelligence Artificielle**.

### Objectifs
- Simuler une maison connectée avec 4 capteurs virtuels
- Transmettre les données via le protocole **MQTT**
- Détecter les comportements anormaux avec **Isolation Forest**
- Stocker et visualiser les données sur **Firebase** et **ThingsBoard**
- Fournir un **dashboard web** professionnel en temps réel

### Type de projet
- ✅ **Projet simulé** (sans matériel physique)
- ✅ **Mode hybride** (Edge + Cloud)
- ✅ **Avec Intelligence Artificielle**

---

## 🏗 Architecture globale

```
┌─────────────────────────────────────────────────────────────┐
│                     EDGE (Local)                            │
│                                                             │
│  ┌──────────────┐    MQTT     ┌─────────────────────────┐  │
│  │   Node-RED   │ ──────────► │  Mosquitto MQTT Broker  │  │
│  │  (Capteurs   │  Publish/   │     localhost:1883       │  │
│  │  Simulés)    │  Subscribe  └─────────────────────────┘  │
│  │              │                         │                 │
│  │ • Température│                         ▼                 │
│  │ • Mouvement  │            ┌─────────────────────────┐   │
│  │ • Porte      │            │    Node-RED Processing  │   │
│  │ • Fumée      │            │  • Détection règles     │   │
│  └──────────────┘            │  • Appel IA Python      │   │
│                              │  • Routage données      │   │
│                              └─────────────────────────┘   │
│                                    │           │            │
│                          ┌─────────┘           └────────┐  │
│                          ▼                              ▼  │
│               ┌──────────────────┐        ┌──────────────┐ │
│               │   Python IA      │        │  HTTP POST   │ │
│               │ Isolation Forest │        │              │ │
│               │ Scikit-learn     │        └──────┬───────┘ │
│               └──────────────────┘               │        │
└─────────────────────────────────────────────────-│--------┘
                                                   │
                    ┌──────────────────────────────┘
                    ▼
┌───────────────────────────────────────────────────────────┐
│                     CLOUD                                  │
│                                                            │
│  ┌─────────────────────────┐   ┌────────────────────────┐ │
│  │  Firebase Realtime DB   │   │   ThingsBoard Cloud    │ │
│  │  • Stockage données IoT │   │  • Dashboard pro IoT   │ │
│  │  • Interface Web HTML   │   │  • Alertes automatiques│ │
│  │  • Temps réel           │   │  • Télémétrie MQTT     │ │
│  └─────────────────────────┘   └────────────────────────┘ │
│                │                                           │
│                ▼                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │           Interface Web Dashboard                    │  │
│  │  smarthome_dashboard.html — Firebase LIVE            │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

---

## 🛠 Technologies utilisées

| Technologie | Version | Rôle |
|-------------|---------|------|
| **Node-RED** | v4.1.8 | Orchestration IoT, simulation capteurs |
| **Mosquitto** | v2.1.2 | Broker MQTT local |
| **Python** | 3.14 | Script IA détection anomalies |
| **Scikit-learn** | 1.8.0 | Algorithme Isolation Forest |
| **NumPy** | 2.4.6 | Traitement données numériques |
| **Pandas** | 3.0.3 | Manipulation données |
| **Firebase** | v10.12.0 | Base de données cloud temps réel |
| **ThingsBoard** | Cloud | Plateforme IoT professionnelle |
| **MQTT** | v3.1.1 | Protocole communication IoT |
| **HTTP/REST** | — | Communication Node-RED → Firebase |
| **JavaScript** | ES6 | Interface web + Node-RED functions |

---

## 📦 Prérequis

### Logiciels à installer

1. **Node.js** (v18+) → https://nodejs.org
2. **Node-RED** → `npm install -g node-red`
3. **Mosquitto MQTT** → https://mosquitto.org/download/
4. **Python 3.14+** → https://www.python.org/downloads/
5. **Git** → https://git-scm.com/download/win

### Comptes cloud nécessaires

1. **Firebase** → https://console.firebase.google.com
2. **ThingsBoard** → https://thingsboard.cloud

---

## ⚙️ Installation et configuration

### Étape 1 — Cloner le projet

```bash
git clone https://github.com/Ayoub-lah/secure-smart-home-iot.git
cd secure-smart-home-iot
```

### Étape 2 — Installer les dépendances Python

```bash
pip install scikit-learn pandas numpy
```

### Étape 3 — Installer les modules Node-RED

```bash
cd ~/.node-red
npm install node-red-dashboard
```

### Étape 4 — Configurer Mosquitto

Créer le fichier de configuration `mosquitto.conf` :

**Windows :** `C:\Program Files\Mosquitto\mosquitto.conf`

```
listener 1883
allow_anonymous true
```

### Étape 5 — Copier les scripts Python

Copier `ia_nodered.py` dans le dossier de travail :

**Windows :**
```cmd
copy ia_nodered.py C:\Users\HP\Downloads\ia_nodered.py
```

**Linux/Mac :**
```bash
cp ia_nodered.py ~/ia_nodered.py
```

### Étape 6 — Importer le flow Node-RED

1. Ouvrir Node-RED → **http://localhost:1880**
2. Menu ☰ → **Import**
3. Sélectionner le fichier `flows_complete.json`
4. Cliquer **Import** → **Deploy**

> ⚠️ **Important :** Adapter les chemins Python dans le nœud exec selon votre système :
> - Windows : `"C:\Users\VotreNom\AppData\Local\Programs\Python\Python314\python.exe"`
> - Linux/Mac : `python3`

---

## 🚀 Lancer le projet

### Étape 1 — Démarrer Mosquitto (Terminal Admin)

**Windows :**
```cmd
mosquitto -c "C:\Program Files\Mosquitto\mosquitto.conf" -v
```

**Linux :**
```bash
sudo systemctl start mosquitto
# ou
mosquitto -c /etc/mosquitto/mosquitto.conf -v
```

✅ Vous devez voir : `mosquitto version 2.1.2 running`

---

### Étape 2 — Démarrer Node-RED (Nouveau terminal)

```bash
node-red
```

✅ Attendez : `Server now running at http://127.0.0.1:1880/`

---

### Étape 3 — Ouvrir les interfaces

| Interface | URL | Description |
|-----------|-----|-------------|
| **Node-RED** | http://localhost:1880 | Flow editor |
| **Dashboard** | http://localhost:1880/ui | Monitoring local |
| **Interface Web** | Ouvrir `smarthome_dashboard.html` | Dashboard principal |
| **Firebase** | https://console.firebase.google.com | Cloud DB |
| **ThingsBoard** | https://thingsboard.cloud | IoT Platform |

---

### Étape 4 — Deploy Node-RED

Ouvrir http://localhost:1880 et cliquer **Deploy** 🚀

---

## 🧪 Tester le projet

### Test 1 — Vérifier MQTT

Ouvrir 2 terminaux :

**Terminal 1 — Subscriber :**
```bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t smarthome/# -v
```

**Terminal 2 — Publisher :**
```bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t smarthome/temperature \
  -m "{\"capteur\":\"temperature\",\"valeur\":25,\"timestamp\":\"2026-05-29T10:00:00Z\"}"
```

✅ Le Terminal 1 doit afficher le message JSON

---

### Test 2 — Vérifier l'IA Python

```bash
# Cas normal
echo {"temperature":23,"mouvement":0,"porte":0,"fumee":0} | python ia_nodered.py
# → {"anomalie": false, "niveau": "NORMAL", ...}

# Spoofing température
echo {"temperature":75,"mouvement":0,"porte":0,"fumee":0} | python ia_nodered.py
# → {"anomalie": true, "niveau": "DANGER", "type_attaque": "spoofing_temperature"}

# Injection de données
echo {"temperature":50,"mouvement":1,"porte":1,"fumee":1} | python ia_nodered.py
# → {"anomalie": true, "niveau": "CRITIQUE", "type_attaque": "injection_donnees"}

# Intrusion
echo {"temperature":16,"mouvement":1,"porte":1,"fumee":0} | python ia_nodered.py
# → {"anomalie": true, "niveau": "DANGER", "type_attaque": "intrusion"}
```

---

### Test 3 — Vérifier Firebase

Aller sur :
```
https://console.firebase.google.com/project/smarthomeiot-fd84c/database/smarthomeiot-fd84c-default-rtdb/data
```

✅ Les données `temperature`, `mouvement`, `porte`, `fumee` doivent apparaître en temps réel.

---

### Test 4 — Tester l'IA dans Node-RED

Dans Node-RED, faire défiler vers le bas du canvas et cliquer :

| Bouton | Résultat attendu |
|--------|-----------------|
| 🧪 Test Normal | `✅ [IA-NORMAL] Aucune anomalie` |
| 🎭 Test Spoofing | `🎭 [IA-DANGER] spoofing_temperature` |
| 💉 Test Injection | `💉 [IA-CRITIQUE] injection_donnees` |
| 🔓 Test Intrusion | `🔓 [IA-DANGER] intrusion` |

---

## 📁 Fichiers du projet

```
secure-smart-home-iot/
│
├── flows_complete.json         # Flow Node-RED complet
│   ├── Capteurs simulés        # Température, Mouvement, Porte, Fumée
│   ├── MQTT Publish/Subscribe  # Mosquitto local + ThingsBoard
│   ├── Firebase HTTP           # Envoi données vers Firebase
│   ├── IA Integration          # Appel script Python via exec
│   └── Node-RED Dashboard      # Widgets UI
│
├── smarthome_flow.json         # Flow Node-RED simplifié
│
├── ia_nodered.py               # Script IA pour Node-RED (stdin)
│   ├── Entraînement            # 500 données normales
│   ├── Prédiction              # Isolation Forest
│   └── Classification          # Spoofing / Injection / Intrusion
│
├── ia_detection_anomalies.py   # Script IA complet avec tests
│   ├── Génération données      # Normales + Attaques simulées
│   ├── Entraînement modèle     # IsolationForest + StandardScaler
│   ├── Évaluation              # Taux détection 64%
│   └── Simulation temps réel  # Analyse messages MQTT
│
├── smarthome_dashboard.html    # Interface Web principale
│   ├── Firebase LIVE           # Données temps réel
│   ├── Graphique Chart.js      # Historique température
│   ├── Simulation attaques     # Spoofing, Injection, Intrusion
│   └── Architecture            # Schéma Edge → Cloud
│
└── README.md                   # Ce fichier
```

---

## 🤖 Partie IA — Isolation Forest

### Algorithme choisi : Isolation Forest

**Pourquoi Isolation Forest ?**
- Algorithme **non supervisé** — pas besoin d'exemples d'attaques étiquetées
- Efficace sur des données **multidimensionnelles**
- Rapide à entraîner et à inférer
- Conçu spécifiquement pour la **détection d'anomalies**

### Paramètres du modèle

```python
model = IsolationForest(
    n_estimators=100,      # 100 arbres de décision
    contamination=0.15,    # 15% de données anormales attendues
    random_state=42        # Reproductibilité
)
```

### Données d'entraînement

| Capteur | Plage normale | Distribution |
|---------|--------------|--------------|
| Température | 18–28°C | Uniforme |
| Mouvement | 0 ou 1 | 70% aucun, 30% détecté |
| Porte | 0 ou 1 | 80% fermée, 20% ouverte |
| Fumée | 0 ou 1 | 98% normal, 2% détectée |

### Scores d'anomalie

| Type | Score | Niveau |
|------|-------|--------|
| Normal | -0.44 | ✅ NORMAL |
| Spoofing température | -0.55 | 🟡 DANGER |
| Intrusion | -0.68 | 🟠 DANGER |
| Injection données | -0.77 | 🔴 CRITIQUE |

> **Seuil :** Score < -0.50 → Anomalie détectée

### Résultats

```
Total attaques testées  : 50
✅ Anomalies détectées  : 32
🎯 Taux de détection    : 64%
```

---

## 🚨 Cyberattaques détectées

### 1. 🎭 Spoofing de température
**Description :** Le hacker injecte une fausse valeur de température très élevée pour déclencher de fausses alarmes ou masquer une intrusion.

```json
{"temperature": 75, "mouvement": 0, "porte": 0, "fumee": 0}
→ score: -0.5524 | DANGER
```

### 2. 💉 Injection de données
**Description :** Tous les capteurs sont activés simultanément — comportement impossible en conditions normales. Indique une manipulation des données IoT.

```json
{"temperature": 50, "mouvement": 1, "porte": 1, "fumee": 1}
→ score: -0.7588 | CRITIQUE
```

### 3. 🔓 Accès non autorisé (Intrusion)
**Description :** Mouvement détecté + porte ouverte + température basse. Signature caractéristique d'une intrusion physique dans la maison.

```json
{"temperature": 16, "mouvement": 1, "porte": 1, "fumee": 0}
→ score: -0.6759 | DANGER
```

---

## ☁️ Plateformes Cloud

### Firebase Realtime Database
- **URL :** https://smarthomeiot-fd84c-default-rtdb.europe-west1.firebasedatabase.app
- **Rôle :** Stockage temps réel des données capteurs
- **Connexion :** HTTP REST depuis Node-RED
- **Usage :** Alimente l'interface web `smarthome_dashboard.html`

### ThingsBoard Cloud
- **URL :** https://thingsboard.cloud
- **Device :** SmartHome-IoT
- **Rôle :** Dashboard IoT professionnel + alertes automatiques
- **Connexion :** MQTT depuis Node-RED (topic: `v1/devices/me/telemetry`)

### Topics MQTT

```
smarthome/
├── temperature          # Données température
├── mouvement           # Données mouvement
├── porte               # Données porte
├── fumee               # Données fumée
├── alertes/ia          # Alertes générées par l'IA
└── actionneurs/
    ├── alarme          # Contrôle alarme
    ├── lumiere         # Contrôle lumière
    └── verrou          # Contrôle verrou
```



## 📚 Références

- [Eclipse Mosquitto Documentation](https://mosquitto.org/documentation/)
- [Node-RED Documentation](https://nodered.org/docs/)
- [Firebase Realtime Database](https://firebase.google.com/docs/database)
- [ThingsBoard Documentation](https://thingsboard.io/docs/)
- [Scikit-learn Isolation Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- [MQTT Protocol Specification](https://mqtt.org/mqtt-specification/)

---

<div align="center">

**🏠 Secure Smart Home** — Master SBD S2 — FST Tanger — 2025/2026

*Pr. M. EL BRAK — Module IoT et Applications*

</div>
