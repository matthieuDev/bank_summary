'''
Pour charger les transactions du Crédit Mutuel
'''
import pandas as pd

def load_from_creditmutuel_pandas(filename):
    '''
    Charge un fichier CSV du Crédit Mutuel en utilisant pandas.
    
    Args:
        filename (str): Chemin vers le fichier CSV.
        
    Returns:
        DataFrame: Un DataFrame pandas contenant les données du fichier.
    '''
    return pd.read_csv(filename, sep=';')

# Autres catégories: "Sous-catégorie"
def load_from_creditmutuel_file(filename, cat_column="Catégorie"):
    '''
    Charge les données d'un fichier CSV du Crédit Mutuel et les transforme.
    
    Args:
        filename (str): Chemin vers le fichier CSV.
        cat_column (str): Nom de la colonne pour la catégorie (par défaut "Catégorie", l'autre valeur conseillé est "Sous-catégorie").
        
    Returns:
        list: Une liste de dictionnaires représentant les enregistrements.
    '''
    df = load_from_creditmutuel_pandas(filename)
    df = df[["Date opération", cat_column, "Montant"]]
    df.columns = ['date', 'category', 'balance']
    
    # Convertit le montant en float après remplacement de la virgule par un point
    df["balance"] = df["balance"].map(lambda x: float(x.replace(',', '.').strip()))
    
    # Remplace les '/' dans la date pour un format plus uniforme
    df["date"] = df["date"].map(lambda x: x.replace('/', ' '))
    
    return df.to_dict('records')

def date2month(date):
    '''
    Convertit une date au format 'jj/mm/aaaa' en 'mm/aaaa'.
    
    Args:
        date (str): La date à convertir.
        
    Returns:
        str: La date convertie au format 'mm/aaaa'.
    '''
    return '/'.join(date.split('/')[1:])

def load_from_creditmutuel_pandas(filename,
                                   filter_date=None, filter_date_month=None,
                                   filter_category=None, filter_subcategory=None):
    '''
    Charge et filtre les données d'un fichier CSV du Crédit Mutuel.
    
    Args:
        filename (str): Chemin vers le fichier CSV.
        filter_date (str, optional): Filtre pour la date d'opération.
        filter_date_month (str, optional): Filtre pour le mois de la date d'opération.
        filter_category (str, optional): Filtre pour la catégorie.
        filter_subcategory (str, optional): Filtre pour la sous-catégorie.
        
    Returns:
        DataFrame: Un DataFrame pandas filtré contenant les données.
    '''
    df = pd.read_csv(filename, sep=';')
    
    # Applique les filtres sur les colonnes appropriées
    for col, filter_value in [
        ('Date opération', filter_date),
        ('Catégorie', filter_category),
        ('Sous-catégorie', filter_subcategory),
    ]:
        if filter_value is not None:
            df = df[df[col] == filter_value]
            
    # Applique un filtre supplémentaire basé sur le mois si fourni
    if filter_date_month is not None:
        df = df[df['Date opération'].map(date2month) == filter_date_month]
    
    return df
