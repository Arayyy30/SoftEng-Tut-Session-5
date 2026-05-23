import pytest
from src.baggage import validate_baggage 

_FAILED_MESSAGES = {"overweight": "Weight surpasses limit.", 
                     "invalid": "Data is invalid."}

def test_carry_on():
    assert validate_baggage(-1, "carry-on", "economy", "domestic", hazardous_item=False) == _FAILED_MESSAGES["invalid"]
    assert validate_baggage(-1, "carry-on", "business", "domestic", hazardous_item=False) == _FAILED_MESSAGES["invalid"]
    assert validate_baggage(7, "carry-on", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(7, "carry-on", "business", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(8, "carry-on", "economy", "domestic", hazardous_item=False) == _FAILED_MESSAGES["overweight"]
    assert validate_baggage(8, "carry-on", "business", "domestic", hazardous_item=False) == _FAILED_MESSAGES["overweight"]