# **Nettoyage du DataSet 'Student Depression'**

**Contexte :** 
- Cette section traite du nettoyage du dataset pour assurer la qualité des données.
- Les valeurs manquantes et incohérentes peuvent altérer les analyses et modèles, d'où leur traitement prioritaire.

**Objectif :**
- Identifier, comprendre et corriger les anomalies pour garantir des données fiables et prêtes à l'analyse.

### **Importation du DataSet et Informations Générales**


```python
import pandas as pd

df = pd.read_csv("../donnees/brutes/Student Depression Dataset.csv")

```


```python
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Profession</th>
      <th>Academic Pressure</th>
      <th>Work Pressure</th>
      <th>CGPA</th>
      <th>Study Satisfaction</th>
      <th>Job Satisfaction</th>
      <th>Sleep Duration</th>
      <th>Dietary Habits</th>
      <th>Degree</th>
      <th>Have you ever had suicidal thoughts ?</th>
      <th>Work/Study Hours</th>
      <th>Financial Stress</th>
      <th>Family History of Mental Illness</th>
      <th>Depression</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Male</td>
      <td>33.0</td>
      <td>Visakhapatnam</td>
      <td>Student</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>8.97</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>5-6 hours</td>
      <td>Healthy</td>
      <td>B.Pharm</td>
      <td>Yes</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>No</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()#3 lignes NaN dans 'Financial Stress', on peut dropper
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 27901 entries, 0 to 27900
    Data columns (total 18 columns):
     #   Column                                 Non-Null Count  Dtype  
    ---  ------                                 --------------  -----  
     0   id                                     27901 non-null  int64  
     1   Gender                                 27901 non-null  object 
     2   Age                                    27901 non-null  float64
     3   City                                   27901 non-null  object 
     4   Profession                             27901 non-null  object 
     5   Academic Pressure                      27901 non-null  float64
     6   Work Pressure                          27901 non-null  float64
     7   CGPA                                   27901 non-null  float64
     8   Study Satisfaction                     27901 non-null  float64
     9   Job Satisfaction                       27901 non-null  float64
     10  Sleep Duration                         27901 non-null  object 
     11  Dietary Habits                         27901 non-null  object 
     12  Degree                                 27901 non-null  object 
     13  Have you ever had suicidal thoughts ?  27901 non-null  object 
     14  Work/Study Hours                       27901 non-null  float64
     15  Financial Stress                       27898 non-null  float64
     16  Family History of Mental Illness       27901 non-null  object 
     17  Depression                             27901 non-null  int64  
    dtypes: float64(8), int64(2), object(8)
    memory usage: 3.8+ MB
    


```python
df = df.dropna()
```

### **Description des colonnes du DataSet**

- **Academic Pressure** : Pression académique (0 = aucune, 5 = maximum).  
- **Work Pressure** : Pression professionnelle (0 = aucune, 5 = maximum).  
- **Sleep Duration** : Durée de sommeil.  
- **Dietary Habits** : Habitudes alimentaires.  
- **Study Satisfaction** : Satisfaction des études (0 = pas satisfait, 5 = très satisfait).  
- **Job Satisfaction** : Satisfaction professionnelle (0 = pas satisfait, 5 = très satisfait).  
- **Financial Stress** : Stress financier (0 = aucun, 5 = maximum).  
- **Family History of Mental Illness** : Antécédent familial de maladie mentale.  
- **Dépression** : Niveau de dépression (0 = pas de signes, 1 = présence de signes).  
- **CGPA** : Moyenne académique cumulée (échelle de 0 à 10).  
   - **9-10** : Excellent.  
   - **7-8.9** : Très bon.  
   - **5-6.9** : Moyen, nécessite des efforts.  
   - **<5** : Faible, nécessitant une attention urgente.  
   - Le CGPA peut refléter un stress académique, lié à des performances faibles ou à la pression pour maintenir un haut niveau.

### **Suppression des colonnes inutiles**


```python
# Suppression de la colonne `id`
df= df.drop('id', axis = 1)
```


```python
# Colonne 'Work Pressure'
df[df['Work Pressure'] == 0] # 27895 lignes valeur 0 > colonne à supprimer

# Colonne 'Job Satisfaction'
df[df['Job Satisfaction'] == 0] # 27890 lignes valeur 0 > colonne à supprimer

# Suppression des colonnes
df = df.drop(['Job Satisfaction', 'Work Pressure'], axis = 1)
```


```python
# Colonne 'Student'
df = df[df['Profession'] == 'Student'] #27870 lignes = filtrage par Student puis colonne à supprimer
df = df.drop('Profession', axis = 1)
```

### **Traduction en Français des valeurs et intitulés de Colonnes**

- **Objectif** : Traduire le df en français pour faciliter la lecture et l'analyse

#### **Traduction des intitulés de colonnes**


```python
#Traduction des colonnes
df = df.rename(columns = {'Gender' : 'Genre', 'City' : 'Ville', 'Academic Pressure' : 'Pression Académique', 'Study Satisfaction' : 'Satisfaction Académique', 'Sleep Duration' : 'Temps de sommeil', 'Dietary Habits' : 'Habitudes Alimentaires', 
       'Have you ever had suicidal thoughts ?' : 'Pensées Suicidaires', 'Work/Study Hours' : 'Temps études/jour(heures)', 'Financial Stress' : 'Stress Financier', 'Family History of Mental Illness' : 'Antécédents familiaux mentaux', 'Depression' : 'Dépression'})

```

#### **Définition de la fonction de Traduction des valeurs de Cellule**


```python
def traduction(x):
    if x == '5-6 hours':
        return '5-6 heures'
    elif x == '7-8 hours':
        return '7-8 heures'
    elif x == 'Less than 5 hours':
        return 'Moins de 5 heures'
    elif x == 'More than 8 hours':
        return 'Plus de 8 heures'
    elif x == 'Others':
        return 'Autre'
    elif x == 'Healthy':
        return 'Saines'
    elif x == 'Moderate':
        return 'Modérées'
    elif x == 'Unhealthy':
        return 'Mauvaises'
    elif x == 'Male':
        return 'Homme'
    elif x == 'Female':
        return 'Femme'
```

#### **Traduction des Colonnes**


```python
# Colonne Genre
df['Genre'] = df['Genre'].apply(traduction)
```


```python
# Colonne Temps de Sommeil
df['Temps de sommeil'] = df['Temps de sommeil'].apply(traduction)
```


```python
# Colonne Habitudes Alimentaires
df['Habitudes Alimentaires'] = df['Habitudes Alimentaires'].apply(traduction)
```

### **Changement de Type**

**Objectif :**
- S'assurer du bon format des valeurs numériques et textuelles en vue du machine learning et des calculs éventuels sur PowerBI


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 27867 entries, 0 to 27900
    Data columns (total 14 columns):
     #   Column                         Non-Null Count  Dtype  
    ---  ------                         --------------  -----  
     0   Genre                          27867 non-null  object 
     1   Age                            27867 non-null  float64
     2   Ville                          27867 non-null  object 
     3   Pression Académique            27867 non-null  float64
     4   CGPA                           27867 non-null  float64
     5   Satisfaction Académique        27867 non-null  float64
     6   Temps de sommeil               27867 non-null  object 
     7   Habitudes Alimentaires         27867 non-null  object 
     8   Degree                         27867 non-null  object 
     9   Pensées Suicidaires            27867 non-null  object 
     10  Temps études/jour(heures)      27867 non-null  float64
     11  Stress Financier               27867 non-null  float64
     12  Antécédents familiaux mentaux  27867 non-null  object 
     13  Dépression                     27867 non-null  int64  
    dtypes: float64(6), int64(1), object(7)
    memory usage: 3.2+ MB
    


```python
# Colonnes 'Float' à transformer en 'INT'
df['Age'] = df['Age'].astype(int)
df['Temps études/jour(heures)'] = df['Temps études/jour(heures)'].astype(int)
df['Pression Académique'] = df['Pression Académique'].astype(int)
df['Satisfaction Académique'] = df['Satisfaction Académique'].astype(int)
df['Stress Financier'] = df['Stress Financier'].astype(int)
```

### **Suppression des lignes inutiles**

**Objectif :**
- Supprimer les lignes non pertinentes, incomplètes et où les valeurs ne sont pas représentatives.

#### **Colonne 'Ville'**


```python
# Colonne 'Ville'
df['Ville'].value_counts()
```




    Ville
    Kalyan                1564
    Srinagar              1372
    Hyderabad             1338
    Vasai-Virar           1289
    Lucknow               1155
    Thane                 1139
    Ludhiana              1109
    Agra                  1092
    Surat                 1078
    Kolkata               1065
    Jaipur                1034
    Patna                 1006
    Visakhapatnam          968
    Pune                   968
    Ahmedabad              949
    Bhopal                 933
    Chennai                884
    Meerut                 822
    Rajkot                 815
    Delhi                  767
    Bangalore              766
    Ghaziabad              744
    Mumbai                 698
    Vadodara               693
    Varanasi               684
    Nagpur                 651
    Indore                 643
    Kanpur                 607
    Nashik                 547
    Faridabad              461
    Saanvi                   2
    Bhavna                   2
    City                     2
    Harsha                   2
    Kibara                   1
    Nandini                  1
    Nalini                   1
    Mihir                    1
    Nalyan                   1
    M.Com                    1
    ME                       1
    Rashi                    1
    Gaurav                   1
    Reyansh                  1
    Harsh                    1
    Vaanya                   1
    Mira                     1
    Less than 5 Kalyan       1
    3.0                      1
    Less Delhi               1
    M.Tech                   1
    Khaziabad                1
    Name: count, dtype: int64




```python
# Suppression des villes n'ayant que 1 ou 2 étudiants renseignés pour permettre un mapping pertinent
df = df[df['Ville'].map(df['Ville'].value_counts()) > 2]
```

#### **Colonne 'Temps de sommeil'**


```python
df['Temps de sommeil'].unique() #Seulement 4 catégories + 'Others': on traduit les catégories et on drop les others
```




    array(['5-6 heures', 'Moins de 5 heures', '7-8 heures',
           'Plus de 8 heures', 'Autre'], dtype=object)




```python
df['Temps de sommeil'].value_counts()
```




    Temps de sommeil
    Moins de 5 heures    8295
    7-8 heures           7327
    5-6 heures           6169
    Plus de 8 heures     6032
    Autre                  18
    Name: count, dtype: int64




```python
# Suppression des 18 lignes 'Autre'
df = df[df['Temps de sommeil'] != 'Autre']
```

#### **Colonne 'Habitudes Alimentaires'**


```python
df['Habitudes Alimentaires'].value_counts()
```




    Habitudes Alimentaires
    Mauvaises    10287
    Modérées      9897
    Saines        7627
    Autre           12
    Name: count, dtype: int64




```python
# Suppression des 12 lignes 'Autre'
df = df[df['Habitudes Alimentaires'] != 'Autre']
```

#### **Colonne 'CGPA'**


```python
# Suppressoin de 9 lignes valeurs nulles
df = df[df['CGPA'] > 0] 
```

### **Catégorisation de la colonne 'Degree'**


```python
# Valeurs uniques dans df['Degree']
df['Degree'].unique()
```




    array(['B.Pharm', 'BSc', 'BA', 'BCA', 'M.Tech', 'PhD', 'Class 12', 'B.Ed',
           'LLB', 'BE', 'M.Ed', 'MSc', 'BHM', 'M.Pharm', 'MCA', 'MA', 'B.Com',
           'MD', 'MBA', 'MBBS', 'M.Com', 'B.Arch', 'LLM', 'B.Tech', 'BBA',
           'ME', 'MHM', 'Others'], dtype=object)



**Objectif :**
- Regrouper les différents diplômes contenus dans la colonne `Degree` pour faciliter l'analyse.

**Méthodologie :**
- La colonne `Degree` recueille les différents diplômes visés par les étudiants de l'enquête.
- Un regroupement doit être fait par ***Niveau de diplôme***, afin de pouvoir filtrer et analyser plus facilement.
- Création d'une colonne `Niveau d'Etude` puis suppression de la colonne `Degree`


```python
# Diplomes 'Others'
len(df[df['Degree'] == 'Others'])
```




    35



- Suppression de 35 lignes non pertinentes


```python
df = df[df['Degree'] != 'Others']
```

#### **Description des diplomes de la colonne `Degree`**

**Diplômes de premier cycle (Undergraduate):**

- B.Pharm - Bachelor of Pharmacy : Diplôme en pharmacie.
- BSc - Bachelor of Science : Diplôme en sciences générales ou spécialisées.
- BA - Bachelor of Arts : Diplôme en sciences humaines et sociales.
- BCA - Bachelor of Computer Applications : Diplôme en informatique.
- B.Ed - Bachelor of Education : Diplôme en pédagogie/enseignement.
- BE - Bachelor of Engineering : Diplôme en ingénierie.
- BHM - Bachelor of Hotel Management : Diplôme en gestion hôtelière.
- B.Com - Bachelor of Commerce : Diplôme en commerce et comptabilité.
- B.Arch - Bachelor of Architecture : Diplôme en architecture.
- B.Tech - Bachelor of Technology : Diplôme technique et d'ingénierie.
- BBA - Bachelor of Business Administration : Diplôme en gestion d’entreprise.

**Diplômes de deuxième cycle (Postgraduate):**

- M.Tech - Master of Technology : Diplôme avancé en technologie.
- M.Ed - Master of Education : Diplôme en enseignement avancé.
- MSc - Master of Science : Diplôme de maîtrise en sciences.
- M.Pharm - Master of Pharmacy : Diplôme avancé en pharmacie.
- MCA - Master of Computer Applications : Diplôme de maîtrise en informatique.
- MA - Master of Arts : Diplôme de maîtrise en sciences humaines.
- MBA - Master of Business Administration : Diplôme de maîtrise en gestion.
- M.Com - Master of Commerce : Diplôme de maîtrise en commerce.
- ME - Master of Engineering : Diplôme de maîtrise en ingénierie.
- MHM - Master of Hotel Management : Diplôme avancé en gestion hôtelière.

**Autres diplômes professionnels ou académiques :**

- PhD - Doctor of Philosophy : Doctorat dans un domaine spécifique.
- LLB - Bachelor of Laws : Diplôme en droit.
- LLM - Master of Laws : Diplôme de maîtrise en droit.
- MD - Doctor of Medicine : Diplôme médical avancé.
- MBBS - Bachelor of Medicine, Bachelor of Surgery : Diplôme de base en médecine.
- Class 12 - Equivalent du baccalauréat (niveau pré-universitaire).

#### **Catégorisation des diplômes**


```python
#Les 'Degrees' peuvent être regroupés en niveau d'étude comme suit:
bachelors = ['BSc', 'BA', 'BCA', 'BE', 'BTech', 'B.Pharm', 'B.Ed', 'B.Com', 'B.Arch', 'BHM', 'BBA', 'Class 12', 'LLB', 'MBBS', "B.Tech"]
masters = ["MSc", "MA", "MCA", "MBA", "MTech", "ME", "M.Ed", "M.Com", "M.Pharm", "MHM", "LLM", "M.Tech"]
doctors = ["PhD", "MD"]

#Fonction pour nouvelle colonne:
def niv_etude(x):
    if x in bachelors:
        return 'Bachelor'
    elif x in masters:
        return 'Master'
    elif x in doctors:
        return 'Doctorat'
```


```python
# Création de la colonne 'Niveau d'étude':
df['Niveau étude'] = df['Degree'].apply(niv_etude)
```


```python
df['Niveau étude'].value_counts()
```




    Niveau étude
    Bachelor    19352
    Master       7328
    Doctorat     1087
    Name: count, dtype: int64




```python
# Suppression de la colonne 'Degree' inutile
df = df.drop('Degree', axis = 1)
```

### **Colonnes Booléennes**

**Objectif :**
- Transformer les colonnes possédant seulement 2 valeurs uniques (Yes ou No) en booléen pour préparer le machine learning.

#### **Colonne 'Pensées Suicidaires'**


```python
df['Pensées Suicidaires'].unique()
```




    array(['Yes', 'No'], dtype=object)




```python
df['Pensées Suicidaires'] = df['Pensées Suicidaires'].apply(lambda x : True if x == 'Yes' else False)
```

#### **Colonne 'Pensées Suicidaires'**


```python
df['Antécédents familiaux mentaux'].unique()
```




    array(['No', 'Yes'], dtype=object)




```python

df['Antécédents familiaux mentaux'] = df['Antécédents familiaux mentaux'].apply(lambda x : True if x == 'Yes' else False)
```

### **Finalisation du DataFrame et Exportation**


```python
#Réorganisation des colonnes
df = df[['Genre', 'Age', 'Ville', 'Niveau étude', 'Pression Académique', 'CGPA', 'Satisfaction Académique', 'Temps de sommeil', 'Habitudes Alimentaires',
       'Pensées Suicidaires', 'Temps études/jour(heures)', 'Stress Financier', 'Antécédents familiaux mentaux', 'Dépression']]
```


```python
df = df.reset_index().drop('index', axis = 1)
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 27767 entries, 0 to 27766
    Data columns (total 14 columns):
     #   Column                         Non-Null Count  Dtype  
    ---  ------                         --------------  -----  
     0   Genre                          27767 non-null  object 
     1   Age                            27767 non-null  int32  
     2   Ville                          27767 non-null  object 
     3   Niveau étude                   27767 non-null  object 
     4   Pression Académique            27767 non-null  int32  
     5   CGPA                           27767 non-null  float64
     6   Satisfaction Académique        27767 non-null  int32  
     7   Temps de sommeil               27767 non-null  object 
     8   Habitudes Alimentaires         27767 non-null  object 
     9   Pensées Suicidaires            27767 non-null  bool   
     10  Temps études/jour(heures)      27767 non-null  int32  
     11  Stress Financier               27767 non-null  int32  
     12  Antécédents familiaux mentaux  27767 non-null  bool   
     13  Dépression                     27767 non-null  int64  
    dtypes: bool(2), float64(1), int32(5), int64(1), object(5)
    memory usage: 2.1+ MB
    


```python
df.to_csv('../donnees/nettoyees/student_depression_dataset_nettoyees.csv', index = False)
```

**Conclusion**
- Le DataFrame nettoyé peut maintenant être utilisé pour l'analyse exploratoire et le machine learning.

### **BONUS : Incorporation des coordonnées géographiques pour mapping**


```python
# import du df_ville
df_ville = pd.read_csv("../donnees/nettoyees/coordonnees_ville_inde.csv")
```


```python
df_ville.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ville</th>
      <th>Etat</th>
      <th>Population</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agra</td>
      <td>Uttar Pradesh</td>
      <td>1585704</td>
      <td>27.1800</td>
      <td>78.0100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ahmedabad</td>
      <td>Gujarat</td>
      <td>5577940</td>
      <td>23.0300</td>
      <td>72.5800</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bangalore</td>
      <td>Karnataka</td>
      <td>15386000</td>
      <td>12.9789</td>
      <td>77.5917</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bhopal</td>
      <td>Madhya Pradesh</td>
      <td>1798218</td>
      <td>23.2600</td>
      <td>77.4100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Chennai</td>
      <td>Tamil Nadu</td>
      <td>4646732</td>
      <td>13.0700</td>
      <td>80.2400</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merger les datasets sur la colonne 'Ville'
df_kpi = pd.merge(df, df_ville, how='left', left_on='Ville', right_on='Ville')
```


```python
df_kpi.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Genre</th>
      <th>Age</th>
      <th>Ville</th>
      <th>Niveau étude</th>
      <th>Pression Académique</th>
      <th>CGPA</th>
      <th>Satisfaction Académique</th>
      <th>Temps de sommeil</th>
      <th>Habitudes Alimentaires</th>
      <th>Pensées Suicidaires</th>
      <th>Temps études/jour(heures)</th>
      <th>Stress Financier</th>
      <th>Antécédents familiaux mentaux</th>
      <th>Dépression</th>
      <th>Etat</th>
      <th>Population</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Homme</td>
      <td>33</td>
      <td>Visakhapatnam</td>
      <td>Bachelor</td>
      <td>5</td>
      <td>8.97</td>
      <td>2</td>
      <td>5-6 heures</td>
      <td>Saines</td>
      <td>True</td>
      <td>3</td>
      <td>1</td>
      <td>False</td>
      <td>1</td>
      <td>Andhra Pradesh</td>
      <td>969608</td>
      <td>17.7000</td>
      <td>83.2500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Femme</td>
      <td>24</td>
      <td>Bangalore</td>
      <td>Bachelor</td>
      <td>2</td>
      <td>5.90</td>
      <td>5</td>
      <td>5-6 heures</td>
      <td>Modérées</td>
      <td>False</td>
      <td>3</td>
      <td>2</td>
      <td>True</td>
      <td>0</td>
      <td>Karnataka</td>
      <td>15386000</td>
      <td>12.9789</td>
      <td>77.5917</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Homme</td>
      <td>31</td>
      <td>Srinagar</td>
      <td>Bachelor</td>
      <td>3</td>
      <td>7.03</td>
      <td>5</td>
      <td>Moins de 5 heures</td>
      <td>Saines</td>
      <td>False</td>
      <td>9</td>
      <td>1</td>
      <td>True</td>
      <td>0</td>
      <td>Jammu &amp; Kashmir</td>
      <td>1180570</td>
      <td>34.0800</td>
      <td>74.8000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Femme</td>
      <td>28</td>
      <td>Varanasi</td>
      <td>Bachelor</td>
      <td>3</td>
      <td>5.59</td>
      <td>2</td>
      <td>7-8 heures</td>
      <td>Modérées</td>
      <td>True</td>
      <td>4</td>
      <td>5</td>
      <td>True</td>
      <td>1</td>
      <td>Uttar Pradesh</td>
      <td>1198491</td>
      <td>25.3200</td>
      <td>82.9900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Femme</td>
      <td>25</td>
      <td>Jaipur</td>
      <td>Master</td>
      <td>4</td>
      <td>8.13</td>
      <td>3</td>
      <td>5-6 heures</td>
      <td>Modérées</td>
      <td>True</td>
      <td>1</td>
      <td>1</td>
      <td>False</td>
      <td>0</td>
      <td>Rajasthan</td>
      <td>3073350</td>
      <td>26.9200</td>
      <td>75.7800</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_kpi.isnull().sum()
```




    Genre                            0
    Age                              0
    Ville                            0
    Niveau étude                     0
    Pression Académique              0
    CGPA                             0
    Satisfaction Académique          0
    Temps de sommeil                 0
    Habitudes Alimentaires           0
    Pensées Suicidaires              0
    Temps études/jour(heures)        0
    Stress Financier                 0
    Antécédents familiaux mentaux    0
    Dépression                       0
    Etat                             0
    Population                       0
    Latitude                         0
    Longitude                        0
    dtype: int64




```python
df_kpi.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 27767 entries, 0 to 27766
    Data columns (total 18 columns):
     #   Column                         Non-Null Count  Dtype  
    ---  ------                         --------------  -----  
     0   Genre                          27767 non-null  object 
     1   Age                            27767 non-null  int32  
     2   Ville                          27767 non-null  object 
     3   Niveau étude                   27767 non-null  object 
     4   Pression Académique            27767 non-null  int32  
     5   CGPA                           27767 non-null  float64
     6   Satisfaction Académique        27767 non-null  int32  
     7   Temps de sommeil               27767 non-null  object 
     8   Habitudes Alimentaires         27767 non-null  object 
     9   Pensées Suicidaires            27767 non-null  bool   
     10  Temps études/jour(heures)      27767 non-null  int32  
     11  Stress Financier               27767 non-null  int32  
     12  Antécédents familiaux mentaux  27767 non-null  bool   
     13  Dépression                     27767 non-null  int64  
     14  Etat                           27767 non-null  object 
     15  Population                     27767 non-null  int64  
     16  Latitude                       27767 non-null  float64
     17  Longitude                      27767 non-null  float64
    dtypes: bool(2), float64(3), int32(5), int64(2), object(6)
    memory usage: 2.9+ MB
    


```python
# Export de df_kpi
df_kpi.to_csv('../donnees/nettoyees/df_kpi_final.csv', index=False)
```
