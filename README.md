# Investigation Numérique Avancée (INA)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](INA_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE SEC4052** · École Nationale Supérieure Polytechnique de l'Université de Yaoundé I · Département de Génie Informatique · 60 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Une constatation a une source ; une analyse a un niveau de confiance.*

Ce cours prolonge l'UE SEC4031 (Introduction à l'investigation numérique). Il passe de la méthode à la pratique : forensique des systèmes Windows et Linux, de la mémoire, du réseau, des téléphones, du cloud et des objets connectés, sources ouvertes, rédaction du rapport d'expertise et cas intégrateurs. Il traite ensuite les défis émergents : anti-forensique, intelligence artificielle, conteneurs et cloud-native, comparaison internationale des systèmes d'investigation. Il se termine par les fondements cryptographiques de la preuve : impact du quantique, Trilemme CRO formalisé (cadre CLO), analyse de primitives, lecture critique d'un protocole en cours de recherche, cryptanalyse, méthode formelle et étude de la signature BLS. Les affaires camerounaises (MVOM, FAKO, MUNGO, SANAGA, TANGUE, DIBAMBA…) sont fictives, mais leurs mécanismes juridiques et techniques sont exacts.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`INA_main.pdf`](INA_main.pdf) | Traité complet (Parties IV à VI, 19 chapitres, annexes), compilé depuis [`INA_main.tex`](INA_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 31 présentations PowerPoint : vision d'ensemble et 30 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 19 fiches de 40 questions au format texte, une par chapitre, en complément de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie4/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_IN.sty`](Style_IN.sty) | Sources du livre |

## Organisation du cours (60 heures, 30 séances de 2 heures)

| Partie | Chapitres | Séances | Fichiers |
|---|---|---|---|
| **IV. Forensique opérationnelle** | 14. Forensique système · 15. Réseau · 16. Mobile · 17. Cloud · 18. IoT et embarqué · 19. OSINT et compréhension des attaques · 20. Rapport forensique · 21. Cas intégrateurs | J01 – J16 | [`partie4/`](partie4/) |
| **V. Défis émergents** | 22. Anti-forensique · 23. Intelligence artificielle · 24. Conteneurs et cloud-native · 25. Benchmarking international | J17 – J22 | [`partie5/`](partie5/) |
| **VI. Fondements théoriques** | 26. Impact du quantique · 27. Trilemme CRO · 28. Analyse des primitives · 29. Protocole ZK-NR · 30. Conception et cryptanalyse · 31. Méthode formelle · 32. Cas pratique BLS | J23 – J29 | [`partie6/`](partie6/) |
| **Synthèse** | Retour sur le cours, lancement du lab intégrateur INA-LAB-12 | J30 | |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles de documents · D. Textes de loi · E. Bibliographie · F. Contacts | | [`annexes/`](annexes/) |

Les chapitres de la Partie IV occupent deux séances chacun ; ceux des Parties V et VI, une ou deux. La séance qui clôt un chapitre renvoie à sa fiche d'auto-évaluation et, s'il y en a un, à son lab, à faire hors présentiel.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et douze laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **SEC4052**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-ina/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-ina/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-ina/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-ina/raw/main/ndap-sukulu/NDAP_SUKULU_INA_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré ; il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet, pour l'étudiant et pour l'enseignant, est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md). Les fiches de 40 questions au format texte restent disponibles dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| INA-LAB-01 | 14 | Forensique système : timeline Linux et Windows |
| INA-LAB-02 | 15 | Forensique réseau : beaconing et courriel frauduleux |
| INA-LAB-03 | 15 | Journaux réseau sans capture : DNS, proxy, pare-feu |
| INA-LAB-04 | 16 | Forensique mobile : SMS, appels, EXIF |
| INA-LAB-05 | 17 | Forensique cloud : CloudTrail et fenêtre aveugle |
| INA-LAB-06 | 18 | Objets connectés : micrologiciel de routeur et NVR |
| INA-LAB-07 | 19 | Sources ouvertes : domaines, profils, cryptoactifs |
| INA-LAB-08 | 20 | Le rapport forensique : relecture avant dépôt |
| INA-LAB-09 | 22 | Anti-forensique : timestomping et journaux effacés |
| INA-LAB-10 | 23 | L'IA en forensique : mesurer un outil, examiner des clips |
| INA-LAB-11 | 24 | Conteneurs : audit Kubernetes et conteneur évincé |
| INA-LAB-12 | Tout le cours | Synthèse (3 heures) : Opération DIBAMBA, du dossier intégrateur à la preuve vérifiable |

## Compiler le livre

Avec une distribution LaTeX : `pdflatex INA_main`, `biber INA_main`, `makeindex INA_main`, puis deux fois `pdflatex INA_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py INA all` (Python 3 et python-pptx).

## Normes et documents sous licence

Les normes ISO/IEC et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
