from datetime import date
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.magic_link import create_code, use_code

def test_create_code_returns_six_characters(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    assert len(create_code(db_connection, 1)) == 6

def test_valid_code_returns_user_id(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    code = create_code(db_connection, 1)
    assert use_code(db_connection, code)['user_id'] == 1

def test_code_without_booking_has_no_booking_id(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    code = create_code(db_connection, 1)
    assert use_code(db_connection, code)['booking_id'] is None

def test_code_stores_booking_id(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    booking_id = BookingRepository(db_connection).create(Booking(date(2026, 12, 1), 6, False, 4))
    code = create_code(db_connection, 4, booking_id)
    assert use_code(db_connection, code)['booking_id'] == booking_id

def test_wrong_code_returns_none(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    create_code(db_connection, 1)
    assert use_code(db_connection, "nope12") is None

def test_expired_code_returns_none(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    code = create_code(db_connection, 1, hours=-1)
    assert use_code(db_connection, code) is None

def test_deleting_booking_deletes_its_links(db_connection):
    db_connection.seed("seeds/baobnb.sql")
    repo = BookingRepository(db_connection)
    booking_id = repo.create(Booking(date(2026, 12, 1), 6, False, 4))
    code = create_code(db_connection, 4, booking_id)
    repo.delete(booking_id)
    assert use_code(db_connection, code) is None