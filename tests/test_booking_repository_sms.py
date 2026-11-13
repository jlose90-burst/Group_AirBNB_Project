from datetime import date
from lib.booking import Booking
from lib.booking_repository import BookingRepository

def test_create_returns_new_booking_id(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    repo = BookingRepository(db_connection)
    assert repo.create(Booking(date(2026, 12, 1), 6, False, 4)) == 1
    assert repo.create(Booking(date(2026, 12, 2), 6, False, 4)) == 2

def test_find_booking_details_returns_guest_and_lair(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    repo = BookingRepository(db_connection)
    repo.create(Booking(date(2026, 12, 1), 6, False, 4))

    details = repo.find_booking_details(1)
    assert details['guest_id'] == 4
    assert details['username'] == 'DrDoom'
    assert details['phone'] == '07513589444'
    assert details['location_name'] == 'Island Volcano Cavity Base'
    assert details['date'] == date(2026, 12, 1)

def test_find_booking_details_missing_returns_none(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    assert BookingRepository(db_connection).find_booking_details(999) is None

def test_find_other_requests_only_same_lair_and_date(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    repo = BookingRepository(db_connection)
    repo.create(Booking(date(2026, 12, 1), 6, False, 4))   # id 1 - DrDoom
    repo.create(Booking(date(2026, 12, 1), 6, False, 1))   # id 2 - Palpatine, same date
    repo.create(Booking(date(2026, 12, 2), 6, False, 2))   # id 3 - Saruman, different date

    others = repo.find_other_requests_details(1)
    assert len(others) == 1
    assert others[0]['username'] == 'Sheev Palpatine'

def test_find_host_details(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    host = BookingRepository(db_connection).find_host_details(6)
    assert host['host_id'] == 3
    assert host['username'] == 'DrEvil'
    assert host['phone'] == '07513589922'
    assert host['location_name'] == 'Island Volcano Cavity Base'

def test_find_host_details_missing_returns_none(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    assert BookingRepository(db_connection).find_host_details(999) is None