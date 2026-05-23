_FAILED_MESSAGES = {
    "hazardous": "Hazardous items detected. Can't proceed further.",
}

def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item):
    """
    Business Rules:
    - Carry-on baggage max 7 kg
    - Checked baggage max 30 kg
    - Business class gets extra 10 kg allowance for checked baggage
    - Hazardous items are prohibited
    """

    if hazardous_item:
        return _FAILED_MESSAGES["hazardous"]