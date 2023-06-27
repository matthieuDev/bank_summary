from bs4 import BeautifulSoup
import requests

def content2_transaction_list(html) :
    soup = BeautifulSoup(html)

    transactions_soup = soup.find_all('div' , {"class": "transaction"})

    transactions = []
    for tsoup in transactions_soup :
        date = parse_date(tsoup.find_all('div' , {"class": "date"}))
        category = check_one_and_get(tsoup.find_all('div' , {"class": "category"})).getText()
        balance = parse_balance(tsoup.find_all('span' , {"class": "balance"}))

        transactions.append({ 'date': date, 'category': category, 'balance': balance })
        
    return transactions

def load_from_file(filepath) :
    with open(filepath, encoding='utf8') as f :
        html = f.read()

    return content2_transaction_list(html)

def check_one_and_get(findall) :
    assert len(findall) == 1
    return findall[0]

def parse_balance(findall_soup) :
    balance = check_one_and_get(findall_soup).getText()
    assert balance[-1] == '€'
    return float(balance.strip('€').strip().replace(',', '.').replace('\xa0', '').replace('\u202f', ''))

def parse_date(findall_soup) :
    date = check_one_and_get(findall_soup).getText()
    return date.split('-')[0].strip()