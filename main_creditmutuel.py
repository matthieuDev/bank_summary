from creditmutuel_load_transactions import *
from aggregate_transactions import *

if __name__ == '__main__' :
    filename = 'export-operations-202409271701.csv'
    transactions = load_from_creditmutuel_file(filename)
    print(group_transactions_by_month(transactions, True))

    print(load_from_creditmutuel_pandas(
        filename,
        filter_date_month="09/2024", filter_category='A catégoriser'
    ).to_markdown())