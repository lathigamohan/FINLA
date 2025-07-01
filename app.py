from flask import Flask, render_template, request, redirect, url_for
import csv
import json
from collections import defaultdict
from utils.categorize import auto_tag
from utils.karma import karma_score
from utils.finance import compute_bank_balances
from utils.quotes import get_quote

app = Flask(__name__)

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    import csv
    from utils.quotes import get_quote
    from utils.finance import compute_bank_balances

    good_karma = 0
    bad_karma = 0
    total_spent = 0
    transactions = []

    try:
        with open('data/transactions.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                karma = row.get('Karma', 'neutral')
                if karma == 'good':
                    good_karma += 1
                elif karma == 'bad':
                    bad_karma += 1
                amount = float(row.get('Amount', 0))
                total_spent += amount
                transactions.append(row)
    except FileNotFoundError:
        pass

    # 💡 Budget Breakdown (Assume default salary for now)
    salary = 10000  # You can ask the user to enter this later
    budget = {
        "needs": round(salary * 0.5, 2),
        "wants": round(salary * 0.3, 2),
        "savings": round(salary * 0.2, 2)
    }

    quote = get_quote()
    banks = compute_bank_balances()

    return render_template("index.html",
                           transactions=transactions,
                           good_karma=good_karma,
                           bad_karma=bad_karma,
                           quote=quote,
                           budget=budget,
                           banks=banks)


# ------------------ FILE UPLOAD ------------------
@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file and uploaded_file.filename.endswith(('.csv', '.txt')):
        data = uploaded_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(data)
        transactions = []

        for row in reader:
            description = row.get('Description', '')
            amount = row.get('Amount', '')
            date = row.get('Date', '')
            category = auto_tag(description)
            karma = karma_score(description)

            transactions.append({
                'Date': date,
                'Description': description,
                'Amount': amount,
                'Category': category,
                'Karma': karma
            })

        with open('data/transactions.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Date', 'Description', 'Amount', 'Category', 'Karma'])
            writer.writeheader()
            writer.writerows(transactions)

    return redirect('/')

# ------------------ CHART VIEW ------------------
@app.route('/charts')
def charts():
    category_totals = defaultdict(float)

    try:
        with open('data/transactions.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row.get('Category', 'Others')
                amount = float(row.get('Amount', 0))
                category_totals[category] += amount
    except FileNotFoundError:
        category_totals = {"No data": 0}

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    return render_template("charts.html", labels=labels, values=values)

# ------------------ BANK MANAGEMENT ------------------
@app.route('/add_bank', methods=['POST'])
def add_bank():
    platforms = request.form.getlist('linked_platforms')

    new_bank = {
        "bank_name": request.form['bank_name'],
        "balance": int(request.form['balance']),
        "min_balance": int(request.form['min_balance']),
        "linked_platforms": platforms
    }

    try:
        with open('data/banks.json', 'r') as file:
            banks = json.load(file)
    except FileNotFoundError:
        banks = []

    banks.append(new_bank)

    with open('data/banks.json', 'w') as file:
        json.dump(banks, file, indent=2)

    return redirect('/banks')

@app.route('/banks')
def view_banks():
    banks = compute_bank_balances()
    return render_template("banks.html", banks=banks)

# ------------------ GOALS ------------------
@app.route('/goals')
def goals():
    try:
        with open('data/goals.json', 'r') as file:
            goals = json.load(file)
    except FileNotFoundError:
        goals = []

    return render_template("goals.html", goals=goals)

@app.route('/add-goal', methods=['POST'])
def add_goal():
    new_goal = {
        "name": request.form['name'],
        "target": float(request.form['target']),
        "current": float(request.form['current']),
        "date": request.form['date']
    }

    try:
        with open('data/goals.json', 'r') as file:
            goals = json.load(file)
    except:
        goals = []

    goals.append(new_goal)

    with open('data/goals.json', 'w') as file:
        json.dump(goals, file, indent=4)

    return redirect('/goals')

# ------------------ SERVER START ------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
