from lib.booking import Booking

def test_booking_constructs():
    booking = Booking('2026-01-12',1,True,2,1)
    assert booking.id == 1
    assert booking.date == '2026-01-12'
    assert booking.location_id == 1
    assert booking.booker_id == 2
    assert booking.confirmed == True

def test_booking_formats():
    booking = Booking('2026-01-12',1,True,2,1)
    assert str(booking) == "Booking(2026-01-12, 1, True, 2, 1)"

def test_booking_are_equal():
    booking = Booking('2026-01-12',1,True,2,1)
    booking2 = Booking('2026-01-12',1,True,2,1)
    assert booking == booking2