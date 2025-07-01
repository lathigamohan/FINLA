import json

with open('data/banks.json', 'r') as file:
    banks = json.load(file)
    print(type(banks))  # Should print <class 'list'>
    for bank in banks:
        print(bank)
