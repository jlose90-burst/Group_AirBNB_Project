from lib.sms_service import format_phone

def test_uk_mobile_with_space_becomes_international():
    assert format_phone("07700 900123") == "+447700900123"

def test_uk_mobile_with_dashes_becomes_international():
    assert format_phone("07700-900-123") == "+447700900123"

def test_already_international_number_unchanged():
    assert format_phone("+447700900123") == "+447700900123"