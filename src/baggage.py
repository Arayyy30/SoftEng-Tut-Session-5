<<<<<<< HEAD
def validate_baggage(baggage_type):
    max_weight = 0
    if baggage_type == 'carry-on':
        max_weight = 7
=======
_SUCCESS_MESSAGES = {"domestic": "Checked in successful.", 
                        "international": "Checked in successful. Passport is required"}

def isDomestic(type):
    if (type == "international"):
        return False
    else:
        return True

def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item):
    if isDomestic(flight_type):
        return _SUCCESS_MESSAGES["domestic"]
    else:
        return _SUCCESS_MESSAGES["international"]



>>>>>>> 2dad4d761b2b13bf8b670b334d68732b30e78535
