SPEC = [
    {"k": "title", "tag": "Jour 16 / 30 · Séance de 2 heures", "title": "Cas intégrateurs (2) : SANAGA, TANGUE, DIBAMBA",
     "sub": "Une action sans base légale, une constatation sans source : zéro point, même juste.",
     "right": "Partie IV · Chapitre C21 §21.3-21.5"},
    {"k": "synthese", "title": "Rappel de la séance précédente", "kicker": "Jour 15 · FAKO et MUNGO", "items": [
        "FAKO : la **chronologie** désigne l'usurpation",
        "Saisir avant de notifier ; **cinq hypothèses**",
        "MUNGO : **conserver d'abord** ; déontologie sous pression",
    ]},
    {"k": "agenda", "items": [
        ("35 min", "**SANAGA** : rançongiciel à l'hôpital, dix minutes pour décider"),
        ("25 min", "**TANGUE revisitée** : neuf violations"),
        ("40 min", "**DIBAMBA** : simulation d'examen"),
        ("20 min", "**Débriefing** · fiche C21 · présentation du lab de synthèse"),
    ]},
    {"k": "scenario", "title": "Opération SANAGA : le brief", "label": "Hôpital des Sept Collines (fictif), Yaoundé · 22 mars 2026, 06 h 30", "text": [
        "Rançongiciel : bloc chirurgical, pharmacie, dossiers patients paralysés ; **15 bitcoins** exigés en 48 heures.",
        "Données de santé de **12 000 patients** peut-être exfiltrées.",
        "Un patient en soins intensifs dépend d'un équipement connecté au réseau compromis ; la « sauvegarde d'hier » est introuvable."]},
    {"k": "table", "title": "SANAGA : décisions immédiates et médiates", "kicker": "Vous arrivez à 07 h 00", "head": ["Question", "Réponse attendue"], "widths": [3.2, 9.2], "rows": [
        ["La vie du patient", "Elle prime : laisser l'équipe médicale isoler ou basculer l'équipement ; ne rien faire qui le menace ; documenter"],
        ["Les 30 premières minutes", "Photographier, **RAM** (clés, processus), connexions, isolement sans couper le vital, journaux, disques"],
        ["Données de santé", "Notification sans délai (loi n° 2024/017, art. 22), sécurité (art. 27), patients informés"],
        ["La rançon", "L'investigateur **expose** les faits et les risques ; la décision appartient à la direction et aux autorités"],
        ["Volatility", "winword → mshta → cmd → WannaCryptor : document piégé exécutant un HTA"],
        ["Bitcoin", "Blockchain, plateforme de sortie, conservation et gel, entraide"],
    ]},
    {"k": "scenario", "title": "TANGUE revisitée : le procès-verbal fautif", "label": "Section 21.4 · trouvez les erreurs", "text": [
        "L'OPJ BITA **allume le PC** pour constater, photographie l'écran, l'éteint. Le lendemain, il le confie à l'analyste SONG, **sans document**.",
        "L'analyste ouvre l'image avec l'**Explorateur Windows** avant Autopsy.",
        "Le rapport : « l'accusé a **dissimulé** 127 fichiers ; il est **coupable** de fraude informatique selon l'art. 72 ». Les empreintes ne sont **que dans l'E01**."]},
    {"k": "table", "title": "TANGUE : diagnostic", "kicker": "Irrecevable, ou régularisable ?", "head": ["Violation", "Règle", "Effet"], "widths": [4.0, 3.6, 4.8], "rows": [
        ["PC allumé avant acquisition", "ACPO 1, erreur 1", "Contamination prouvable : irrecevabilité probable"],
        ["Transfert sans document", "Custody, erreur 3", "Rupture ; documenter a posteriori, revérifier l'empreinte"],
        ["Explorateur Windows", "Erreur 2", "Contestable ; vérifier l'empreinte, consigner"],
        ["Versions absentes", "Erreur 4", "Régularisable si retrouvées"],
        ["Empreintes dans l'E01 seul", "Erreur 5", "Intégrité non démontrable indépendamment"],
        ["« Dissimulé », « coupable »", "Constatation, rôle du juge", "Réécrire : faits, puis analyse, sans qualification"],
    ]},
    {"k": "scenario", "title": "DIBAMBA : la simulation d'examen", "label": "5 mai 2026, 23 h 45 · trois heures", "text": [
        "MTN signale des transactions MoMo anormales : **234 clients**, **68 millions FCFA** en vingt minutes, au profit d'un seul numéro qui a subi un **SIM swap à 23 h 30**.",
        "L'écoute légale montre des données de l'IMEI vers un serveur parisien, port **8443**, à 23 h 31 ; domaine **mtn-verification.cm**, enregistré le 29 avril.",
        "Il est 01 h 00 ; les journaux de l'hébergeur risquent la rotation dans **deux heures**."]},
    {"k": "steps", "title": "DIBAMBA : la méthode attendue", "kicker": "Trois parties, trois heures", "items": [
        ("A · Cadrage", "Avancé systématique ; réquisition d'urgence à MTN (art. 57) ; **conservation** chez l'hébergeur par le 24/7 (Budapest art. 29) avant la rotation."),
        ("B · Technique", "SIM swap = SMS et OTP détournés ; port 8443 : filtres Wireshark ; réquisitions au bureau d'enregistrement et à l'hébergeur."),
        ("C · Rapport", "Qualifications (art. 72, 86, 65 ; CP 318 ; 2024 art. 63), cinq constatations, deux analyses, synthèse d'une page."),
    ]},
    {"k": "points", "title": "Le lab de synthèse INA-LAB-12", "kicker": "Le plus long des labs : trois heures", "items": [
        "Il reprend **DIBAMBA** sur pièces : SIM swap, transactions, écoute légale, WHOIS, DNS passif",
        "Il ajoute TANGUE, le **benchmarking**, le **quantique**, le **cadre CLO** et la **lecture critique** d'un protocole",
        "Sept parties, A à G : tout le cours",
        "À faire après la séance 30, quand toute la Partie VI aura été vue",
    ]},
    {"k": "synthese", "items": [
        "**SANAGA** : la vie d'abord ; la RAM avant l'isolement ; l'expert n'est pas le décideur",
        "**TANGUE** : neuf violations, deux fatales, plusieurs régularisables",
        "**DIBAMBA** : conserver avant la rotation, qualifier par textes, rapporter par pièces",
    ]},
    {"k": "maison", "lecture": ["Chapitre 21 entier", "NDAP SUKULU : **fiche C21**"]},
    {"k": "fin", "next": "Jour 17 · Anti-forensique (1)", "items": [
        "Principes de l'anti-forensique",
        "Détecter les tentatives sur le système",
        "Désactivation et camouflage réseau"]},
]
