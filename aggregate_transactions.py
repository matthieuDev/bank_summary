'''
Pour regrouper les données chargées
'''

def group_transactions_by_month(transactions, ignore_balance_positif=True):
    '''
    Regroupe les transactions par mois et cumule les soldes.
    
    Args:
        transactions (list): Liste des transactions sous forme de dictionnaires.
        ignore_balance_positif (bool): Indique s'il faut ignorer les soldes positifs.
        
    Returns:
        dict: Dictionnaire avec les mois comme clés et le solde cumulé comme valeurs.
    '''
    group_by_month = {}
    for transaction in transactions:
        # Extrait le mois et l'année
        month = ' '.join(transaction['date'].split(' ')[1:])
        balance = transaction['balance']
        if not ignore_balance_positif or balance < 0:
            group_by_month[month] = group_by_month.get(month, 0) + transaction['balance']
    return group_by_month

def group_transactions_by_category(transactions):
    '''
    Regroupe les transactions par catégorie et cumule les soldes.
    
    Args:
        transactions (list): Liste des transactions sous forme de dictionnaires.
        
    Returns:
        dict: Dictionnaire avec les catégories comme clés et le solde cumulé comme valeurs.
    '''
    group_by_category = {}
    for transaction in transactions:
        category = transaction['category']
        if not category in group_by_category:
            group_by_category[category] = 0
        group_by_category[category] += transaction['balance']
    return group_by_category

def group_transactions_by_month_category(transactions):
    '''
    Regroupe les transactions par mois et par catégorie, et cumule les soldes.
    
    Args:
        transactions (list): Liste des transactions sous forme de dictionnaires.
        
    Returns:
        dict: Dictionnaire avec les mois comme clés et les soldes par catégorie comme valeurs.
    '''
    group_by_month_cat = {}
    for transaction in transactions:
        # Extrait le mois et l'année
        month = ' '.join(transaction['date'].split(' ')[1:])
        category = transaction['category']
        if not month in group_by_month_cat :
            group_by_month_cat[month] = {}
        if not category in group_by_month_cat[month] :
            group_by_month_cat[month][category] = 0
        group_by_month_cat[month][category] += transaction['balance']
        
    return group_by_month_cat
