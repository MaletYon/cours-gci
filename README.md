# IT Governance, COBIT et ITIL (GCI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](GCI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE MSN-2S3-MSI03** · Master Professionnel en Management des Systèmes d'Information · Semestre 3
Chaire UNESCO d'Afrique Centrale ACCES-TIC, sous la tutelle académique de l'École Nationale Supérieure Polytechnique de l'Université de Yaoundé I
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Gouverner, piloter et servir : la gouvernance des systèmes d'information en contexte africain.*

Quand un système d'information s'arrête, la question décisive n'est pas technique. Elle porte sur qui avait décidé, et qui devait rendre compte. Ce cours apprend à y répondre avant la panne. Il s'appuie sur les standards internationaux (ISO, ISACA, IIA, INTOSAI) et sur le droit camerounais et communautaire (CEMAC, OHADA). Quatre organisations fictives servent de fil rouge : la BANQUE SANAGA (Douala), KRIBILOG (Kribi), l'ANPP (administration) et NOUN PAY (fintech, Bafoussam).

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`GCI_main.pdf`](GCI_main.pdf) | Traité complet (prologue, 21 chapitres, annexes), compilé depuis [`GCI_main.tex`](GCI_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations PowerPoint : vision d'ensemble et 15 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 21 fiches de 40 questions au format texte, à distribuer en attendant l'ouverture de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_GCI.sty`](Style_GCI.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | 0. Trois jours sans banque | [`partie0/`](partie0/) |
| **I. Fondements de la gouvernance des SI** | 1. De la gouvernance d'entreprise à la gouvernance des SI · 2. Grandes défaillances et leçons de gouvernance · 3. Alignement, valeur et décision · 4. Panorama et articulation des référentiels | [`partie1/`](partie1/) |
| **II. COBIT 2019** | 5. Principes et architecture · 6. Les 40 objectifs de gouvernance et de management · 7. Concevoir un système de gouvernance sur mesure · 8. Capacité, maturité et feuille de route | [`partie2/`](partie2/) |
| **III. Cadre normatif, juridique et déontologique** | 9. Les normes internationales · 10. Cadre juridique camerounais et africain · 11. Audit, contrôle et assurance | [`partie3/`](partie3/) |
| **IV. ITIL 4 et pratique opérationnelle** | 12. Le système de valeur des services · 13. Centre de services, incidents, problèmes et demandes · 14. Changements, mises en production et configuration · 15. Niveaux de service, continuité et fournisseurs · 16. Processus, RACI et mesure · 17. Études de cas intégrateurs | [`partie4/`](partie4/) |
| **V. Défis avancés** | 18. Agilité, DevOps et cloud · 19. Gouvernance des données et de l'IA | [`partie5/`](partie5/) |
| **VI. Recherche** | 20. Mesurer la gouvernance des SI : état de la recherche · 21. Contributions et pistes de recherche | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles de documents · D. Textes législatifs · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et dix laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **MSN-2S3-MSI03**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-gci/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-gci/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-gci/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-gci/raw/main/ndap-sukulu/NDAP_SUKULU_GCI_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré ; il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet, pour l'étudiant et pour l'enseignant, est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md). Les fiches de 40 questions au format texte restent disponibles dans [`fiches/`](fiches/).

| Lab | Sujet | Chapitre |
|---|---|---|
| GCI-LAB-01 | Arbitrer le portefeuille de projets de l'ANPP | 3 |
| GCI-LAB-02 | Fixer les capacités cibles de la BANQUE SANAGA | 7 |
| GCI-LAB-03 | Dérouler la cascade des objectifs de la BANQUE SANAGA | 7 |
| GCI-LAB-04 | Évaluer la capacité de BAI06 et de DSS02 | 8 |
| GCI-LAB-05 | Tester les contrôles généraux informatiques de l'ANPP | 11 |
| GCI-LAB-06 | Prioriser et analyser les tickets de KRIBILOG | 13 |
| GCI-LAB-07 | Évaluer et décider un changement de la BANQUE SANAGA | 14 |
| GCI-LAB-08 | Disponibilité, pénalités et reprise du suivi des conteneurs | 15 |
| GCI-LAB-09 | Construire la matrice RACI du modèle de NOUN PAY | 16 |
| GCI-LAB-10 | Synthèse des quatre cas : feuilles de route chiffrées | 17 |

## Compiler le livre

Avec une distribution LaTeX (MiKTeX ou TeX Live) : `pdflatex GCI_main`, `biber GCI_main`, `makeindex GCI_main`, puis deux fois `pdflatex GCI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py GCI all` (Python 3 et python-pptx).

## Normes et documents sous licence

Les normes ISO, le référentiel COBIT et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt. Le livre en cite de courts extraits et les reformule.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
