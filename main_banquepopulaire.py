from banquepopulaire_load_transactions import *
from aggregate_transactions import *

if __name__ == '__main__' :
    filepath = 'Comptes Espace Client Banque Populaire.htm'
    transactions = load_from_file(filepath)
    print(group_transactions_by_month(transactions, True))