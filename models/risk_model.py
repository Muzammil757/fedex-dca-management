""" Sample model Ai for recovery prediction """
def predict_recovery_probability(aging_days, overdue_amount):
    if aging_days <= 30:
        return 0.9
    elif aging_days <= 60:
        return 0.6
    else:
        return 0.3
