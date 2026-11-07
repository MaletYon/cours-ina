"""Métadonnées du cours INA et répartition des 30 séances de 2 heures (60 heures)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

INA = {
    "sigle": "INA",
    "code": "SEC4052",
    "titre": "Investigation Numérique Avancée",
    "sous_titre": "Forensique opérationnelle, anti-forensique et fondements cryptographiques de la preuve",
    "master": "Département de Génie Informatique · HN4",
    "bandeau": "Université de Yaoundé I",
    "logo_g": "uy1",
    "logo_d": "enspy",
    "n_jours": 30,
    "annee": "2026-2027",
    "dossier": COURS + r"\SEC4052\Présentation",
    "fil_rouge": "MVOM, BAOBAB, WOURI, MBONGO, FAKO, MUNGO, SANAGA, DIBAMBA",
    "parties": [
        ("Partie IV", "Forensique opérationnelle", "C14–C21"),
        ("Partie V", "Anti-forensique, IA et défis émergents", "C22–C25"),
        ("Partie VI", "Crypto-forensique et contributions originales", "C26–C32"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · Forensique système (1)", "Présentation + C14 §14.1-14.3", [], []),
        2: ("Forensique système (2) : Linux et timeline", "C14 §14.4-14.6", ["C14"], ["LAB-01"]),
        3: ("Forensique réseau (1) : sonde, flux, exfiltration", "C15 §15.1-15.3", [], ["LAB-02"]),
        4: ("Forensique réseau (2) : sessions, journaux, corrélation", "C15 §15.4-15.6", ["C15"], ["LAB-03"]),
        5: ("Forensique mobile (1) : Android et SQLite", "C16 §16.1-16.3", [], []),
        6: ("Forensique mobile (2) : Mobile Money, iOS, Autopsy", "C16 §16.4-16.6", ["C16"], ["LAB-04"]),
        7: ("Forensique cloud (1) : modèles, journaux, SaaS", "C17 §17.1-17.3", [], []),
        8: ("Forensique cloud (2) : éphéméralité, multi-fournisseurs", "C17 §17.4-17.6", ["C17"], ["LAB-05"]),
        9: ("Forensique IoT (1) : architecture, routeur, firmware", "C18 §18.1-18.3", [], []),
        10: ("Forensique IoT (2) : caméras, box, custody IoT", "C18 §18.4-18.6", ["C18"], ["LAB-06"]),
        11: ("OSINT (1) : cadre, personnes, infrastructures, traçage", "C19 §19.1-19.5", [], []),
        12: ("OSINT (2) : documenter, lire une attaque, BAOBAB 2", "C19 §19.6-19.10", ["C19"], ["LAB-07"]),
        13: ("Le rapport forensique (1) : principes et structure", "C20 (1re moitié)", [], []),
        14: ("Le rapport forensique (2) : annexes, pièges, relecture", "C20 (2e moitié)", ["C20"], ["LAB-08"]),
        15: ("Cas intégrateurs (1) : FAKO et MUNGO", "C21 §21.1-21.2", [], []),
        16: ("Cas intégrateurs (2) : SANAGA, TANGUE, DIBAMBA", "C21 §21.3-21.5", ["C21"], []),
        17: ("Anti-forensique (1) : principes, système, réseau", "C22 §22.1-22.3", [], []),
        18: ("Anti-forensique (2) : mobile, IoT, rapport", "C22 §22.4-22.5", ["C22"], ["LAB-09"]),
        19: ("IA et forensique : outil, objet, limites", "C23", ["C23"], ["LAB-10"]),
        20: ("Conteneurs (1) : architecture, acquisition, Kubernetes", "C24 §24.1-24.3", [], []),
        21: ("Conteneurs (2) : vecteurs d'attaque, capture en production", "C24 §24.4-24.5", ["C24"], ["LAB-11"]),
        22: ("Benchmarking mondial des pratiques forensiques", "C25", ["C25"], []),
        23: ("L'impact du quantique sur l'investigation", "C26", [], []),
        24: ("Le Trilemme CRO formalisé (1) : information, cadre CLO", "C27 §27.1-27.3", [], []),
        25: ("Le Trilemme CRO formalisé (2) : capacité, cas, conception", "C27 §27.4-27.7", [], []),
        26: ("Les primitives selon le cadre CLO", "C28", [], []),
        27: ("ZK-NR : lire une recherche en cours", "C29", [], []),
        28: ("Conception et cryptanalyse", "C30", [], []),
        29: ("Analyse formelle et audit d'un protocole multi-couches", "C31 + C32", ["C32"], []),
        30: ("Synthèse du cours · lab de synthèse · clôture", "Synthèse C14-C32", [], ["LAB-12"]),
    },
}

ALL = {"INA": INA}
