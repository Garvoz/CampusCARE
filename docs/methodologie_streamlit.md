# Méthodologie de développement de l'application Streamlit pour CampusCARE.

## Objectif
Ce document présente les étapes clés pour réaliser l'application streamlit du projet CampusCARE.

---

## 1. Réflexion sur la partie machine learning.
1. L'objectif principal sera de fournir une prédiction par un modèle de machine learning sur l'état dépressif d'un étudiant indien.
2. On utilisera toutes les colonnes pertinentes 
2. Etudier la possibilité de faire cette prédiction même si toutes les informations ne sont pas fournies.

---

## 2. Réflexions de cosm'esthétisme : Ajout de pages
1. Une page accueil contenant un mot d'accueil et la présentation du projet.
2. Une page statistiques pour présenter le travail de modélisation des données.
3. Réflexions sur le thème général du site.

---

## 3. Mise en place des modèles de Machine Learning. 
1. On va ici faire une classification: Le modèle va devoir prédire un choix binaire, dépressif ou non dépressif.
2. Il faudra passer par une standardisation des variables numériques (modèle StandardScaler pour sauvegarder cette standardisation) et un encodage des variables catégorielles.
3. Pour la prédiction on entrainera un modèle de régression logistique après avoir scoré la qualité de notre modèle grâce à un train_test_plit.
4. Ces modèles entrainés seront stockés dans un fichier pickle pour les importer dans le streamlit sans avoir besoin de les réentrainer.

---

## 4. Mise en place du streamlit
1. Importation des différentes bibliothèques (pas besoin de celles de ML car modèles dans fichier pickle).
2. Définition du st.set_page_config en premier lieu.
3. Importation des fichier et définition de la fonction de prédiction dans des encart st.cache pour améliorer la performance
4. Codage de la sidebar avec un option_menu puis de la page principale en fonction du choix de ce menu

---

## 5. Thèmes et images
1. Recherche d'images pour améliorer la qualité visuelle grâce à de l'IA générative.
2. Mise en place de codes CSS pour la décoration.

---

## Conclusion
Ce récapitulatif de la mise en place du streamlit permet de lister les différentes étapes de réalisation du livrable.

