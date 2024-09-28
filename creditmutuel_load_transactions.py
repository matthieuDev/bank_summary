import pandas as pd

def load_from_creditmutuel_pandas(filename) :
    return pd.read_csv(filename, sep=';')

#autres catégories: "Sous-catégorie"
def load_from_creditmutuel_file(filename, cat_column="Catégorie"):
    df = load_from_creditmutuel_pandas(filename)
    df = df[["Date opération", cat_column, "Montant"]]
    df.columns = ['date', 'category', 'balance']
    
    df["balance"] = df["balance"].map(lambda x : float(x.replace(',', '.').strip()))
    df["date"] = df["date"].map(lambda x : x.replace('/', ' '))
    
    return df.to_dict('records')

def date2month(date) :
    return '/'.join(date.split('/')[1:])

def load_from_creditmutuel_pandas(filename,
    filter_date=None, filter_date_month=None,
    filter_category=None, filter_subcategory=None,
) :
    df = pd.read_csv(filename, sep=';')
    for col, filter_value in [
        ('Date opération', filter_date),
        ('Catégorie', filter_category),
        ('Sous-catégorie', filter_subcategory),
    ] :
        if not filter_value is None :
            df = df[df[col] == filter_value]
            
    if not filter_date_month is None :
        df = df[df['Date opération'].map(date2month) == filter_date_month]
    return df