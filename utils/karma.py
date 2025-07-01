def karma_score(description):
    desc = description.lower()

    good_keywords = [
        "donate", "donated", "charity", "gift", "temple", "dog", "stray", "help", "volunteer",
        "old age", "orphan", "poor", "need", "support", "tip", "gave", "contribution", 
        "alms", "philanthropy", "generosity", "kindness"
    ]

    bad_keywords = [
        "junk", "unnecessary", "impulse", "late night", "overpriced", "fast food", "waste", 
        "overspent", "splurge", "extra fries", "fine", "penalty", "late fee", "late payment", "late charge"
    ]

    if any(word in desc for word in good_keywords):
        return "good"
    elif any(word in desc for word in bad_keywords):
        return "bad"
    else:
        return "neutral"
