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