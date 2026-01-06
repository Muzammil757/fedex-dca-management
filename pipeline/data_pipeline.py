""" Sample Data Pipeline for DCA Case Management  """
from models.risk_model import predict_recovery_probability
def process_case(case):
    probability = predict_recovery_probability(
        case["aging_days"],
        case["overdue_amount"]
    )

    return {
        "case_id": case["case_id"],
        "recovery_probability": probability,
        "priority": "High" if probability < 0.5 else "Normal"
    }
