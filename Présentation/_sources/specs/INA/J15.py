SPEC = [
    {"k": "title", "tag": "Jour 15 / 30 · Séance de 2 heures", "title": "Cas intégrateurs (1) : FAKO et MUNGO",
     "sub": "Des faits incomplets, parfois trompeurs, comme dans la réalité.",
     "right": "Partie IV · Chapitre C21 §21.1-21.2"},
    {"k": "synthese", "title": "Rappel de la séance précédente", "kicker": "Jour 14 · Rapport (2)", "items": [
        "Synthèse : trois points, une pièce clé",
        "**Annexe G** : toutes les empreintes",
        "Sous pression : répondre par **la pièce**",
    ]},
    {"k": "agenda", "items": [
        ("10 min", "**Mode d'emploi** des cas intégrateurs"),
        ("50 min", "**FAKO** : cadrage, système, qualification"),
        ("45 min", "**MUNGO** : deepfakes, conservation, déontologie"),
        ("15 min", "**Débriefing** : ce que chaque cas mobilise"),
    ]},
    {"k": "chapitre", "num": "C21", "short": "Chapitre 21", "part": "PARTIE IV · FORENSIQUE OPÉRATIONNELLE",
     "title": "Applications et cas intégrateurs",
     "question": "Savez-vous tout mobiliser à la fois : le droit, la méthode, la technique et la déontologie ?"},
    {"k": "steps", "title": "Comment travailler un cas", "kicker": "Mode d'emploi du chapitre", "items": [
        ("Brief", "Les faits tels qu'ils arrivent : incomplets, parfois trompeurs."),
        ("Investigation guidée", "Des questions qui mobilisent tout le cours."),
        ("Révélations", "Des indices nouveaux à mesure que l'enquête avance."),
        ("Rapport", "Un livrable juridiquement structuré."),
    ]},
    {"k": "scenario", "title": "Opération FAKO : le brief", "label": "CAMEROON AGRO SA, Buea · 10 mars 2026", "text": [
        "**47 millions FCFA** de virements non autorisés en février, depuis Sage 100 (Windows Server 2019).",
        "Trois comptes avaient accès aux virements : **EBOA Claire** (DAF), **BAFUT Jonas** (comptable senior), **MBAH Inès** (comptable junior), en arrêt maladie depuis le 1er mars.",
        "Mandat du parquet après plainte : identifier l'auteur."]},
    {"k": "points", "title": "FAKO, étape 1 : cadrage", "kicker": "PIU E1 à E3", "items": [
        "Matrice de criticité : 47 M FCFA, risque pénal correctionnel, plusieurs suspects : **avancé**",
        "Autorisations : perquisition et copie (loi n° 2010/012, art. 52-53), réquisitions (art. 57)",
        "Ordre RFC 3227 : **RAM** du serveur allumé, puis journaux (rotation **30 jours**), disque, Office 365",
        "Risque de destruction : suspects en poste, rotation des journaux : **exporter tout de suite**",
    ]},
    {"k": "scenario", "title": "FAKO : deux révélations", "label": "Journaux et réponse de Microsoft", "text": [
        "Événements **4624** : MBAH_INES, connexions réseau à **02:17** le 14 février et **03:05** le 21 février, depuis **41.202.XXX.XXX** (Lagos).",
        "Microsoft (portail LEA, 5 jours) : le compte s'est connecté de Lagos à 02:17 le 14 février et n'a lu qu'un courriel, la **réinitialisation VPN** envoyée la veille.",
        "Le même compte se connecte de **Douala à 08:30**, six heures plus tard."]},
    {"k": "points", "title": "FAKO : raisonner", "kicker": "Étapes 2 et 3", "items": [
        "Cinq hypothèses (ACH) : elle-même ; **identifiants volés** ; un collègue ; un prestataire ; une erreur",
        "La plus cohérente : **usurpation** après lecture du courriel de réinitialisation",
        "Qualification : accès frauduleux (art. 65), fraude informatique (art. 72), escroquerie (CP 318)",
        "CRO : saisir le téléphone **avant** de notifier, puis entendre selon PEACE",
    ]},
    {"k": "scenario", "title": "Opération MUNGO : le brief", "label": "SCFC · 15 avril 2026", "text": [
        "Une campagne coordonnée vise un candidat aux élections locales du Littoral : **347 faux comptes** Facebook, **12 clips audio deepfake**, 47 publications, 3 faux articles.",
        "Tous créés depuis le même sous-réseau **196.200.XX.0/24** (hébergeur camerounais).",
        "Plainte du candidat le 14 avril ; élection dans **15 jours**."]},
    {"k": "table", "title": "MUNGO : six décisions", "kicker": "Investigation complète", "head": ["Question", "Réponse attendue"], "widths": [3.2, 9.2], "rows": [
        ["Cadrage juridique", "Loi n° 2010/012 et Code pénal ; voix et visage : données personnelles, voire biométriques (loi n° 2024/017)"],
        ["Conservation", "**D'abord** : portail LEA de Meta en urgence, réseau 24/7, avant la suppression des comptes"],
        ["Analyse des MP3", "Métadonnées, spectrogramme, détecteurs ; **l'IA oriente, l'humain constate**"],
        ["Attribution", "Réquisition à l'hébergeur (art. 57) pour l'abonné du sous-réseau"],
        ["Déontologie", "Un concurrent veut « accélérer en privé » : refuser, consigner, informer le parquet"],
        ["CRO", "Publier tôt protège l'électorat mais alerte les auteurs et expose des tiers"],
    ]},
    {"k": "synthese", "items": [
        "**FAKO** : la chronologie (Lagos 02:17, Douala 08:30) dit plus que la personne soupçonnée",
        "Saisir avant de notifier ; cinq hypothèses avant de conclure",
        "**MUNGO** : conserver d'abord ; l'IA oriente ; la déontologie sous pression politique",
    ]},
    {"k": "maison", "lecture": ["Chapitre 21, sections 21.1 et 21.2", "Préparer : sections 21.3 à 21.5 (SANAGA, TANGUE, DIBAMBA)"]},
    {"k": "fin", "next": "Jour 16 · Cas intégrateurs (2)", "items": [
        "SANAGA : un hôpital et une vie en jeu",
        "TANGUE revisitée : diagnostiquer une investigation viciée",
        "DIBAMBA : la simulation d'examen"]},
]
