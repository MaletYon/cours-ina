SPEC = [
    {"k": "title", "tag": "Jour 14 / 30 · Séance de 2 heures", "title": "Le rapport forensique (2) : annexes, pièges, audience",
     "sub": "Toute modification après l'acquisition aurait changé l'empreinte.",
     "right": "Partie IV · Chapitre C20 §20.4-20.7"},
    {"k": "synthese", "title": "Rappel de la séance précédente", "kicker": "Jour 13 · Rapport (1)", "items": [
        "Trois niveaux, trois lecteurs",
        "**Constatation** vérifiable, **analyse** avec confiance",
        "Six parties du rapport technique",
    ]},
    {"k": "agenda", "items": [
        ("20 min", "**La synthèse exécutive** : rédiger pour un magistrat"),
        ("20 min", "**Le dossier probatoire** et l'annexe G"),
        ("25 min", "**Six pièges** de rédaction"),
        ("25 min", "**Le rapport sous pression** : trois questions de la défense"),
        ("30 min", "**Exercice** : rédiger des constatations · fiche C20 · LAB-08"),
    ]},
    {"k": "points", "title": "La synthèse exécutive", "kicker": "Niveau 1 : rédiger pour un magistrat", "items": [
        "**Deux à quatre pages**, aucun jargon non défini",
        "**Trois points** et **une pièce clé**",
        "Chaque conclusion avec son **niveau de confiance**",
        "Les **limites** dites clairement",
    ]},
    {"k": "table", "title": "Le dossier probatoire", "kicker": "Niveau 3 · exemple MVOM", "head": ["Annexe", "Contenu"], "widths": [2.0, 10.4], "rows": [
        ["A", "Extraits de journaux cités dans les constatations"],
        ["B", "Export CSV du $UsnJrnl filtré"],
        ["C", "Rapport PECmd (Prefetch)"],
        ["D", "Captures Volatility"],
        ["E", "Attestation de l'entreprise victime"],
        ["F", "Formulaires de custody EV-001 et EV-001bis"],
        ["**G**", "**Empreintes SHA-256 de toutes les pièces**, identiques à l'acquisition et à l'analyse"],
    ]},
    {"k": "table", "title": "Six pièges de rédaction", "kicker": "Section 20.6", "head": ["Piège", "Exemple", "Correction"], "widths": [3.0, 4.6, 4.8], "rows": [
        ["Certitude excessive", "« L'attaquant est X. »", "Confiance graduée, alternatives"],
        ["Jargon non défini", "« Le rançongiciel a modifié la MFT et l'USN. »", "Définir ou reformuler"],
        ["Conclusion sans preuve", "« L'accès a été obtenu par force brute. »", "Citer les échecs puis la réussite"],
        ["Source non citée", "« Les journaux montrent… »", "Quel journal, quel outil, quelle annexe"],
        ["Hypothèse non réfutée", "« Le suspect est coupable. »", "Présenter et réfuter les alternatives"],
        ["Qualification par l'expert", "« Ce fait constitue l'infraction de l'art. 65. »", "Laisser la qualification au magistrat"],
    ]},
    {"k": "scenario", "title": "Le rapport sous pression (1)", "label": "Affaire MVOM · la contre-expertise attaque", "text": [
        "« Prouvez que les journaux n'ont pas été modifiés par votre client après l'incident. »",
        "Réponse : « Exportés de l'image E01 (EV-001), dont les empreintes ont été calculées à l'acquisition le 13 mars à 15 h 03 (annexe F). L'empreinte recalculée à l'analyse le 15 mars est **identique** (annexe G). Toute modification l'aurait changée. »"]},
    {"k": "scenario", "title": "Le rapport sous pression (2)", "label": "Deux autres questions de la défense", "text": [
        "« Volatility ne modifie-t-il pas la mémoire ? » : la **capture**, faite en premier (RFC 3227), modifie quelques kilo-octets ; c'est consigné (ACPO 2) ; Volatility, lui, analyse un fichier.",
        "« L'IP 185.220.XX.XX n'est-elle pas un VPN ? » : le rapport ne dit pas qui ; il constate un point du réseau. L'**attribution** n'est pas établie, et c'est écrit."]},
    {"k": "exercice", "title": "Rédiger des constatations", "duree": "25 minutes, individuel",
     "text": "MVOM : AnyDesk exécuté 3 fois (UserAssist) ; PID 4892 vers 185.220.XX.XX:4444 ; root connecté à 02:14:09 ; liste de fichiers chiffrés créée à 02:18:31.",
     "questions": [
        "Rédigez cinq constatations : fait, source, annexe.",
        "Ajoutez une phrase d'analyse avec niveau de confiance.",
     ],
     "notes": "Corrigé (exercice 20.2). Un fait par constatation, horodaté, outil et version, annexe ; aucun adjectif. Analyse séparée, confiance élevée sur la séquence, aucune attribution."},
    {"k": "synthese", "items": [
        "**Synthèse** : trois points, une pièce clé, la confiance",
        "**Annexe G** : les empreintes de toutes les pièces",
        "**Six pièges** : certitude, jargon, preuve, source, alternative, qualification",
        "Sous pression : répondre par **la pièce**, jamais par la conviction",
    ]},
    {"k": "maison", "lecture": ["Chapitre 20 et son encadré « Notions mobilisées par le laboratoire INA-LAB-08 »", "NDAP SUKULU : **fiche C20** et **INA-LAB-08** (relecture avant dépôt)"]},
    {"k": "fin", "next": "Jour 15 · Cas intégrateurs (1)", "items": [
        "Opération FAKO : fraude comptable interne",
        "Opération MUNGO : trafic d'influence et deepfakes",
        "Des révélations progressives"]},
]
