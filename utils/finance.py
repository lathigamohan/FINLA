import csv
import json

def compute_bank_balances():
    # Load banks
    try:
        with open('data/banks.json', 'r') as file:
            banks = json.load(file)
    except FileNotFoundError:
        return []

    # Load transactions
    try:
        with open('data/transactions.csv', 'r') as file:
            transactions = list(csv.DictReader(file))
    except FileNotFoundError:
        transactions = []

    updated_banks = []

    for bank in banks:
        # Safely get the original balance
        starting_balance = float(bank.get('starting_balance', 0))
        linked_upis = [p.lower() for p in bank.get('linked_platforms', [])]

        # Deduct matching UPI transactions
        current_balance = starting_balance
        for tx in transactions:
            desc = tx.get('Description', '').lower()
            amt = float(tx.get('Amount', 0))
            if any(upi in desc for upi in linked_upis):
                current_balance -= amt

        bank['current_balance'] = round(current_balance, 2)
        bank['alert'] = current_balance < float(bank.get('min_balance', 0))
        updated_banks.append(bank)

    return updated_banks
