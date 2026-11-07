import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from courses import GCI

J = GCI["jours"]
_cal1 = [[f"J{d:02d}", J[d][0], J[d][1]] for d in range(1, 9)]
_cal2 = [[f"J{d:02d}", J[d][0], J[d][1]] for d in range(9, 16)]
_mai = [[f"J{d:02d}", ", ".join(J[d][2]) or " · ", ", ".join(J[d][3]) or " · "] for d in range(1, 16)]

SPEC = [
    {"k": "title", "tag": "Vision globale du cours · 30 heures", "title": "IT Governance,\nCOBIT et ITIL",
     "sub": "Gouverner, piloter et servir : la gouvernance des systèmes d'information en contexte africain",
     "right": "UE MSN-2S3-MSI03 · 15 séances de 2 heures", "size": 44},
    {"k": "agenda", "title": "Sommaire", "kicker": "Ce document", "items": [
        ("", "**Pourquoi ce cours** : la double conviction, ce qu'il est et n'est pas"),
        ("", "**Objectifs et compétences** : cinq métiers visés"),
        ("", "**Le plan** : un prologue, six parties, vingt chapitres"),
        ("", "**L'organisation** : 30 heures en présentiel, travail personnel hors présentiel"),
        ("", "**Le calendrier** des quinze séances"),
        ("", "**Le fil rouge**, la méthode pédagogique et l'évaluation"),
    ]},
    {"k": "quote", "kicker": "La définition qui ouvre le cours", "text": "Spécifier les droits de décision et le cadre de responsabilité qui encouragent les comportements souhaitables dans l'usage des technologies de l'information.",
     "author": "Peter Weill et Jeanne Ross, définition de la gouvernance des SI (2004, notre traduction)", "size": 26},
    {"k": "compare", "title": "Pourquoi ce cours ?", "kicker": "Une double conviction",
     "left": {"head": "La gouvernance des SI n'est plus une affaire de spécialistes", "items": ["Banques, opérateurs, administrations, jeunes entreprises du numérique dépendent de systèmes dont la **défaillance arrête tout**", "Quand un système s'arrête, la question est toujours : **qui avait décidé, et qui devait rendre compte ?**"]},
     "right": {"head": "Cette discipline ne s'importe pas telle quelle", "items": ["COBIT, ITIL et les normes ISO sont des acquis précieux, pensés dans **d'autres contextes**", "Les appliquer suppose de les relire à la lumière du **droit camerounais et communautaire** (CEMAC, OHADA) et de nos organisations"]},
     "bottom": "Ce cours n'est **ni un résumé** des publications d'ISACA ou de PeopleCert, **ni une préparation à une certification** : les référentiels y sont cités avec exactitude et discutés là où leur transposition pose problème."},
    {"k": "cards", "title": "Gouverner, piloter, servir", "kicker": "Trois ambitions", "cols": 3, "items": [
        {"head": "Gouverner", "badge": "1", "text": "Comprendre **pourquoi** et **par qui** les décisions sur le SI sont prises : gouvernance d'entreprise, agence, alignement, valeur, droits de décision."},
        {"head": "Piloter", "badge": "2", "text": "Concevoir un système de gouvernance avec **COBIT 2019**, le confronter aux **normes ISO** et au **droit camerounais et africain**, l'**auditer**."},
        {"head": "Servir", "badge": "3", "text": "Gérer les services au quotidien avec **ITIL 4** : incidents, problèmes, changements, niveaux de service, continuité, fournisseurs."},
    ]},
    {"k": "table", "title": "Compétences visées par partie", "kicker": "Du niveau fondamental au niveau expert", "head": ["Partie", "Thème", "Compétences visées", "Niveau"], "widths": [1.6, 3.6, 4.8, 1.6], "rows": [
        ["Prologue", "Trois jours sans banque", "Distinguer une cause technique d'une cause de gouvernance", "Base"],
        ["I", "Fondements de la gouvernance des SI", "Définir, situer et justifier la gouvernance des SI", "Base"],
        ["II", "COBIT 2019", "Concevoir et évaluer un système de gouvernance", "Base à moyen"],
        ["III", "Cadre normatif et juridique", "Identifier les obligations et auditer la conformité", "Base"],
        ["IV", "ITIL 4 et processus", "Organiser et mesurer la gestion des services", "Moyen à expert"],
        ["V", "Défis avancés", "Gouverner l'agilité, le nuage, les données et l'IA", "Expert"],
        ["VI", "Recherche", "Lire et produire la recherche sur la gouvernance des SI", "Expert"],
    ]},
    {"k": "cards", "title": "Cinq métiers visés", "kicker": "Les fiches métier du cours", "cols": 3, "items": [
        {"head": "DSI", "badge": "1", "text": "Éclairer le conseil, proposer des arbitrages, alerter par écrit, présenter un portefeuille."},
        {"head": "Responsable GRC", "badge": "2", "text": "Cartographier les obligations, choisir les référentiels, piloter la feuille de route."},
        {"head": "Auditeur SI", "badge": "3", "text": "Évaluer une capacité, tester les contrôles, rédiger des constats en cinq éléments."},
        {"head": "Responsable des services IT", "badge": "4", "text": "Organiser incidents, changements, niveaux de service et fournisseurs selon ITIL 4."},
        {"head": "RSSI", "badge": "5", "text": "Inscrire la sécurité dans la gouvernance : ISO/IEC 27001, nuage, dépendances critiques."},
    ]},
    {"k": "table", "title": "Le plan du cours", "kicker": "Un prologue, six parties, vingt chapitres traités en présentiel", "head": ["Partie", "Thème", "Chapitres", "Séances"], "widths": [1.6, 6, 1.8, 1.8], "rows": [
        ["Prologue", "Trois jours sans banque, quand personne n'a décidé", "P00", "J01"],
        ["Partie I", "Fondements de la gouvernance des SI", "C01 – C04", "J02 – J05"],
        ["Partie II", "COBIT 2019 : le référentiel de la gouvernance", "C05 – C08", "J05 – J07"],
        ["Partie III", "Cadre normatif, juridique et déontologique", "C09 – C11", "J08 – J10"],
        ["Partie IV", "ITIL 4 et pratique opérationnelle", "C12 – C17", "J10 – J14"],
        ["Partie V", "Défis avancés : agilité, DevOps, cloud, données, IA", "C18 – C19", "J14 – J15"],
        ["Partie VI", "Recherche : mesurer la gouvernance des SI", "C20", "J15"],
    ], "note": "Les séances commencent et finissent parfois au milieu d'un chapitre, pour équilibrer la charge des quinze séances."},
    {"k": "stats", "title": "L'organisation des enseignements", "kicker": "30 heures en présentiel, du travail personnel hors présentiel", "items": [
        ("15 × 2 h", "séances en présentiel, une par jour de cours, jamais plus de deux heures"),
        ("30 h", "tout le traité, du prologue à la Partie VI, réparti harmonieusement"),
        ("21", "ateliers de questions-réponses, un par chapitre, sur NDAP SUKULU"),
        ("10", "labs pratiques d'une heure sur NDAP SUKULU, avec corrigés"),
    ], "bottom": "Ateliers et labs sont du **travail personnel**, **hors des 30 heures**. Leur répartition entre les séances est **indicative** ; chaque séance se termine par la liste de ce qu'il faut faire avant la suivante."},
    {"k": "steps", "title": "Le déroulé type d'une séance de deux heures", "kicker": "Une trame commune aux quinze séances", "items": [
        ("Ouvrir", "**Rappel** de la séance précédente, **déroulé** de la séance, **objectifs**."),
        ("Questionner", "La **question directrice** du chapitre, posée par un épisode du **fil rouge**."),
        ("Enseigner", "Définitions, modèles, tableaux, **fiches métier** et **exigences de contrôle**."),
        ("Pratiquer", "Un **exercice en séance**, en binôme ou en groupe, corrigé en notes d'orateur."),
        ("Conclure", "**Synthèse**, **travail à la maison** (ateliers, labs, lecture) et **prochaine séance**."),
    ]},
    {"k": "table", "title": "Le calendrier des séances (1/2)", "kicker": "Jours 1 à 8", "head": ["Jour", "Thème de la séance", "Contenu du traité"], "widths": [1.1, 6.4, 3.9], "rows": _cal1},
    {"k": "table", "title": "Le calendrier des séances (2/2)", "kicker": "Jours 9 à 15", "head": ["Jour", "Thème de la séance", "Contenu du traité"], "widths": [1.1, 6.4, 3.9], "rows": _cal2},
    {"k": "table", "title": "Le travail personnel, séance par séance (1/2)", "kicker": "Ateliers de questions-réponses et labs de NDAP SUKULU · répartition indicative", "head": ["Après", "Ateliers (fiches GCI-FICHE-…)", "Labs (GCI-LAB-…)"], "widths": [1.4, 5.4, 4.6], "rows": _mai[:8]},
    {"k": "table", "title": "Le travail personnel, séance par séance (2/2)", "kicker": "Hors des 30 heures de présentiel", "head": ["Après", "Ateliers (fiches GCI-FICHE-…)", "Labs (GCI-LAB-…)"], "widths": [1.4, 5.4, 4.6], "rows": _mai[8:]},
    {"k": "table", "title": "Les dix labs de NDAP SUKULU", "kicker": "Une heure chacun, corrigés automatiquement", "head": ["Lab", "Intitulé", "Chapitres"], "widths": [1.6, 7.8, 2], "rows": [
        ["LAB-01", "Arbitrer le portefeuille de l'ANPP", "C03"],
        ["LAB-02", "Fixer les capacités cibles de la BANQUE SANAGA", "C05, C07"],
        ["LAB-03", "Dérouler la cascade des objectifs de la BANQUE SANAGA", "C06, C07"],
        ["LAB-04", "Évaluer la capacité de BAI06 et de DSS02", "C08"],
        ["LAB-05", "Tester les contrôles généraux informatiques de l'ANPP", "C11"],
        ["LAB-06", "Prioriser et analyser les tickets de KRIBILOG", "C13"],
        ["LAB-07", "Évaluer et décider un changement de la BANQUE SANAGA", "C14"],
        ["LAB-08", "Disponibilité, pénalités et reprise du suivi des conteneurs", "C15"],
        ["LAB-09", "Construire la matrice RACI du modèle de NOUN PAY", "C16"],
        ["LAB-10", "Synthèse des quatre cas : feuilles de route chiffrées", "C17"],
    ]},
    {"k": "cards", "title": "Quatre organisations fictives, un fil rouge", "kicker": "Des cas ancrés dans la réalité camerounaise", "cols": 2, "items": [
        {"head": "Opération SANAGA", "badge": "S", "text": "La **BANQUE SANAGA**, Douala : une migration du système central qui tourne à la paralysie. Gouvernance, COBIT, changements, COBAC."},
        {"head": "Opération KRIBI", "badge": "K", "text": "**KRIBILOG SA**, Kribi et Douala : infogérance, tickets, niveaux de service, certification ISO/IEC 20000-1."},
        {"head": "Opération MEFOU", "badge": "M", "text": "L'**ANPP**, établissement public : portefeuille de 14 milliards FCFA, contrôles d'accès, Chambre des comptes."},
        {"head": "Opération NOUN", "badge": "N", "text": "**NOUN PAY**, Bafoussam : nuage, données personnelles, notation de crédit par IA, levée de fonds."},
    ]},
    {"k": "cards", "title": "Les outils du cours", "kicker": "Ce que vous retrouverez à chaque séance", "cols": 3, "items": [
        {"head": "Les trois questions réflexes", "badge": "?", "text": "Qui décide, qui exécute, qui rend compte : devant tout projet, changement ou défaillance."},
        {"head": "La grille des dix erreurs", "badge": "10", "text": "Chaque erreur de gouvernance reliée à un signal, une question à poser et un objectif COBIT."},
        {"head": "Le constat en cinq éléments", "badge": "5", "text": "Constatation, critère, cause, conséquence, recommandation : la base de tout rapport."},
        {"head": "Les fiches métier", "badge": "M", "text": "Le concept traduit en démarche pour le DSI, la GRC, l'auditeur, les services IT et le RSSI."},
        {"head": "Les exigences de contrôle", "badge": "✓", "text": "Les pièces qu'un auditeur doit trouver pour établir qu'un dispositif fonctionne."},
        {"head": "Le diagnostic en six volets", "badge": "6", "text": "Organes, valeur, COBIT, conformité, services, fournisseurs : la méthode des cas intégrateurs."},
    ]},
    {"k": "points", "title": "L'évaluation", "kicker": "Hors des 30 heures de présentiel", "items": [
        "Les modalités d'évaluation suivent le **règlement des études** de l'ENSPY pour l'UE MSN-2S3-MSI03",
        "La **simulation d'examen** du chapitre C17 (séance J14) donne le **format type** : un cas, quatre questions, trois heures",
        "Ce qui est attendu : constatations séparées des analyses, **références précises**, recommandations qui traitent des **causes**, gouvernance **proportionnée**",
        "Les ateliers et les labs, à faire régulièrement, sont la meilleure **préparation**",
    ], "side": {"head": "Les ressources", "text": ["Le traité **GCI** (PDF) et son livret de correction.", "**NDAP SUKULU**, code MSN-2S3-MSI03 : fiches d'auto-évaluation et labs.", "Le dossier **Normes** : COBIT 2019, ITIL 4, ISO, textes de loi."], "tone": "green"}},
    {"k": "fin", "next": "Jour 1 · Ouverture du cours et Trois jours sans banque", "label": "PREMIÈRE SÉANCE", "items": [
        "Douala, lundi 9 mars 2026, 7 h 30 : une panne qui n'était pas technique",
        "Les trois questions réflexes ; gouvernance et management",
        "Ce que COBIT et ITIL auraient changé",
    ], "foot": "Bienvenue dans le cours · questions ?"},
]
