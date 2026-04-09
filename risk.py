def get_risk(age, income, experience):
    score = 0

    if age < 30:
        score += 3
    elif age < 50:
        score += 2
    else:
        score += 1

    if income > 50000:
        score += 2

    if experience == "high":
        score += 3
    elif experience == "medium":
        score += 2
    else:
        score += 1

    if score >= 7:
        return "High Risk"
    elif score >= 4:
        return "Medium Risk"
    else:
        return "Low Risk"