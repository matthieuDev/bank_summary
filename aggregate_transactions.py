def group_transactions_by_month(transactions, ignore_balance_positif=True):
    group_by_month = {}
    for transaction in transactions :
        month = ' '.join(transaction['date'].split(' ')[1:])
        balance = transaction['balance']
        if not ignore_balance_positif or balance < 0 :
            group_by_month[month] = group_by_month.get(month, 0) +  transaction['balance']
    return group_by_month

def group_transactions_by_category(transactions):
    group_by_category = {}
    for transaction in transactions :
        category = transaction['category']
        if not category in group_by_category :
            group_by_category[category] = 0
        group_by_category[category] += transaction['balance']
    return group_by_category

def group_transactions_by_month_category(transactions):
    group_by_month_cat = {}
    for transaction in transactions :
        month = ' '.join(transaction['date'].split(' ')[1:])
        category = transaction['category']
        if not month in group_by_month_cat :
            group_by_month_cat[month] = {}
        if not category in group_by_month_cat[month] :
            group_by_month_cat[month][category] = 0
        group_by_month_cat[month][category] += transaction['balance']
        
        
    return group_by_month_cat