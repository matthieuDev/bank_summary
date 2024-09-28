'''
Pour charger les transactions de la banque Populaire
'''
from bs4 import BeautifulSoup

def content2_transaction_list(html):
    '''
    Convertit le contenu HTML d'une page banque populaire en une liste de transactions.
    
    Args:
        html (str): Le contenu HTML à analyser.
        
    Returns:
        list: Liste de transactions sous forme de dictionnaires avec date, catégorie et solde.
    '''
    soup = BeautifulSoup(html, features="html.parser")
    transactions_soup = soup.find_all('div', {"class": "transaction"})

    transactions = []
    for tsoup in transactions_soup:
        date = parse_date(tsoup.find_all('div', {"class": "date"}))
        category = check_one_and_get(tsoup.find_all('div', {"class": "category"})).getText()
        balance = parse_balance(tsoup.find_all('span', {"class": "balance"}))

        transactions.append({'date': date, 'category': category, 'balance': balance})
        
    return transactions

def load_from_file(filepath):
    '''
    Charge les transactions à partir d'un fichier HTML.
    
    Args:
        filepath (str): Chemin vers le fichier HTML à lire.
        
    Returns:
        list: Liste de transactions sous forme de dictionnaires.
    '''
    with open(filepath, encoding='utf8') as f:
        html = f.read()

    return content2_transaction_list(html)

def check_one_and_get(findall):
    '''
    Vérifie qu'il y a exactement un élément dans la liste et le retourne.
    
    Args:
        findall (list): Liste d'éléments trouvés.
        
    Returns:
        Element: L'élément trouvé.
        
    Raises:
        AssertionError: Si la liste ne contient pas exactement un élément.
    '''
    assert len(findall) == 1
    return findall[0]

def parse_balance(findall_soup):
    '''
    Extrait et parse le solde à partir d'un élément HTML.
    
    Args:
        findall_soup (list): Liste d'éléments contenant le solde.
        
    Returns:
        float: Le solde converti en nombre à virgule flottante.
        
    Raises:
        AssertionError: Si le solde n'est pas au format attendu.
    '''
    balance = check_one_and_get(findall_soup).getText()
    assert balance[-1] == '€'  # Vérifie que le solde se termine par '€'
    return float(balance.strip('€').strip().replace(',', '.').replace('\xa0', '').replace('\u202f', ''))

def parse_date(findall_soup):
    '''
    Extrait et parse la date à partir d'un élément HTML.
    
    Args:
        findall_soup (list): Liste d'éléments contenant la date.
        
    Returns:
        str: La date au format 'jj/mm/aaaa'.
    '''
    date = check_one_and_get(findall_soup).getText()
    return date.split('-')[0].strip()  # Extrait la partie de la date avant le tiret
