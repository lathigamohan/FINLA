def auto_tag(description):
    desc = description.lower()

    categories = {
        "Food": [
            "coffee", "tea", "lunch", "snack", "pizza", "swiggy", "zomato",
            "burger", "dinner", "breakfast", "food", "restaurant", "cafe",
            "eatery", "meal", "groceries", "market", "shopping", "supermarket",
            "grocery", "vegetables", "fruits", "dairy", "meat", "fish", "pantry", "bakery"
        ],
        "Travel": [
            "uber", "ola", "train", "bus", "flight", "taxi", "cab", "ride", "trip",
            "journey", "travel", "transport", "commute", "car", "bike", "bicycle", 
            "scooter", "motorcycle", "walk", "run"
        ],
        "Bills": [
            "electricity", "recharge", "wifi", "rent", "water", "gas", "internet",
            "mobile", "phone", "bill", "payment", "fee", "subscription", "service",
            "utility", "maintenance", "insurance", "loan", "debt", "credit", "debit",
            "card", "bank", "atm", "cash", "wallet", "purse", "money"
        ],
        "Shopping": [
            "amazon", "flipkart", "clothes", "clothing", "fashion", "shoes", 
            "accessories", "jewellery", "gifts", "toys", "electronics", "gadgets", 
            "home", "furniture"
        ],
        "Education": [
            "book", "fees", "tuition", "class", "course", "exam", "test", "study",
            "library", "college", "university", "school", "academy", "institute", 
            "training", "seminar", "workshop", "conference", "event"
        ],
        "Entertainment": [
            "netflix", "hotstar", "game", "movie", "entertainment", "fun", "party", 
            "club", "night", "out", "theater", "cinema", "play", "sport", "gym",
            "fitness", "yoga", "meditation", "music", "concert", "show", "festival",
            "holiday", "vacation", "adventure", "explore", "discover"
        ]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in desc:
                return category

    return "Others"
