import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config( layout="wide", page_title = "Campus Care", page_icon= '../streamlit/logo.png')

@st.cache_data
def charger_csv(lien):
    return pd.read_csv(lien)

X_final = charger_csv("../donnees/nettoyees/df_encode_ml.csv")

@st.cache_data
def pickl_listes(lien):
    with open(lien, 'rb') as f: 
        villes = pickle.load(f)
        etudes = pickle.load(f)
        pression_satisf = pickle.load(f)
        sommeil = pickle.load(f)
        alim = pickle.load(f)
        stress = pickle.load(f)
    return villes, etudes, pression_satisf, sommeil, alim, stress

villes, etudes, pression_satisf, sommeil, alim, stress = pickl_listes("../donnees/nettoyees/mes_listes.pkl")

@st.cache_data
def pickl_ml(lien):
    with open(lien, 'rb') as f:
        modeles = pickle.load(f)
    SN = modeles['StandardScaler']
    model = modeles['LogisticRegression']
    return SN, model

SN, model = pickl_ml("../donnees/nettoyees/mes_modeles.pkl")

@st.cache_resource
def encodage_predict(df_a_predire):
    X_num = df_a_predire[['Age', 'Pression Académique', 'CGPA', 'Satisfation Académique', 'Temps études/jour(heures)', 'Stress Financier']]
    X_cat = df_a_predire[['Genre', 'Ville', 'Niveau étude', 'Temps de sommeil', 'Habitudes Alimentaires']]
    X_reserve = df_a_predire[['Pensées Suicidaires', 'Antécédents familiaux mentaux']]

    X_num_SN = pd.DataFrame(SN.transform(X_num), columns=X_num.columns)

    X_cat_dummies = pd.get_dummies(X_cat)
    X_encoded_predire = pd.concat([X_num_SN, X_reserve], axis=1)
    X_encoded_predire = pd.concat([X_encoded_predire, X_cat_dummies], axis=1)

    # DataFrame vide qui a les mêmes colonnes que X_final
    X_predict = pd.DataFrame(columns=X_final.columns)

    # On veut que le DataFrame ait le même nombre de lignes que X_encoded_predire
    X_predict = X_predict.reindex(index=X_encoded_predire.index)
    # On met tous les NaN à False
    X_predict = X_predict.fillna(False)

    # On parcourt chaque colonne de X_encoded_predire
    # Si la colonne est présente dans X_final alors on la garde
    # Sinon, on la met à False
    for column in X_final.columns:
        if column in X_encoded_predire.columns:
            X_predict[column] = X_encoded_predire[column]

    return X_predict

@st.cache_data
def booleen(x):
    if x == 'Oui':
        return True
    elif x == 'Non':
        return False

with st.sidebar:
    st.sidebar.image('../streamlit/CampusCare.webp', use_container_width=True)
    st.markdown(
    """
    <style> 
    [data-testid="stSidebar"]{
        background-image: url(https://i.ibb.co/SRzckFS/sidebar.png);
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )


# Utiliser option_menu dans l'application
    page = option_menu(
        menu_title=None,  # Titre du menu
        options=["Accueil", "Calculateur de risque", "Statistiques"]
    )

st.markdown(
    """
    <style> 
    [data-testid="stMain"]{
        background-color:  #E8F5E9;
        background-size: cover;
        background-position: center;
    }
    [data-testid="stHeader"]{
        background-color:  #E8F5E9;
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
if page == "Accueil":
    st.markdown("<h1 style='text-align: center;'>🌟 Bienvenue sur Campus Care 🌟</h1>", unsafe_allow_html=True)
    st.write("""
             
        Votre bien-être mental est essentiel! 
             
        Campus Care est une application innovante conçue pour aider les étudiants à identifier les risques potentiels de dépression dès les premiers signes. 
             
        En analysant les données que vous fournissez, nous estimons le pourcentage de probabilité que vous présentiez des symptômes dépressifs et vous offrons des pistes pour agir en faveur de votre santé mentale.
             
        """)
    st.image('../streamlit/accueil.jpg', use_container_width=True)

if page == "Calculateur de risque":
    st.markdown("<h1 style='text-align: center;'>Risquez vous la dépression ?</h1>", unsafe_allow_html=True)

    st.write('Répondez à ces quelques questions et nous vous dirons : ')

    city = st.selectbox('Dans quelle ville vivez vous ?', villes, index=None, placeholder="Choisissez une ville")
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Sexe :', ['Homme', 'Femme'], index = None,  placeholder="Choisissez une option")
        age = st.number_input("Age :", min_value=0, max_value=120, step=1, format="%d")
        niv = st.selectbox("Quel est votre niveau d'étude ? ", etudes, index = None,  placeholder="Choisissez une option")
        sleep = st.selectbox('Quelle est votre temps de sommeil moyen ?', sommeil, index=None, placeholder="Choisissez parmis la sélection :")
        
        

    with col2:
        pression = st.select_slider("Notez la pression académique subie : ", [0,1,2,3,4,5])
        satisf = st.select_slider("Notez votre satisfaction de vos études : ", [0,1,2,3,4,5])
        finance = st.select_slider("Notez le stress financier que vous subissez : ", [0,1,2,3,4,5])
        cgpa = st.slider( "Votre indice CGPA : ", min_value=0.0, max_value=10.0, step=0.01, format="%.2f")
        
        
    with col3:
        work = st.number_input("Nombre d'heures d'études journalières :", min_value=0, max_value=14, step=1, format="%d")
        food = st.selectbox('Comment jugez-vous vos habitudes alimentaires ?', alim, index=None, placeholder="Choisissez une option")
        illness = st.selectbox('Antécédents familiaux de maladies mentales ?', ['Oui', 'Non'], index=None, placeholder="Choisissez une option")
        suicide = st.selectbox('Avez-vous déjà eu des pensées suicidaires ?', ['Oui', 'Non'], index=None, placeholder="Choisissez une option")

    if (city != None) and (gender != None) and (age != 0) and (niv != None) and (sleep != None) and (cgpa != 0) and (food != None) and (illness != None) and (suicide != None):

        dico = {
            'Genre' : gender,
            'Age' : age, 
            'Ville' : city, 
            'Niveau étude' : niv, 
            'Pression Académique' : pression, 
            'CGPA' : cgpa,
            'Satisfation Académique' : satisf,
            'Temps de sommeil' : sleep, 
            'Habitudes Alimentaires' : food,
            'Pensées Suicidaires' : booleen(suicide), 
            'Temps études/jour(heures)' : work, 
            'Stress Financier' : finance,
            'Antécédents familiaux mentaux' : booleen(illness)
        }

        df_predict = pd.DataFrame([dico])
        predict = encodage_predict(df_predict)
        proba = float(np.round(model.predict_proba(predict)[0, 1] * 100, 2))

        st.markdown("<h2 style='text-align: center;'>Probabilité que vous soyez en dépression : </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{proba} %</h3>", unsafe_allow_html=True)

        if proba > 45:
            st.markdown(f"<h3 style='text-align: center;'>N'hésitez pas : Consultez rapidement votre médecin</h3>", unsafe_allow_html=True)
