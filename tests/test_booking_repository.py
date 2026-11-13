from lib.booking_repository  import BookingRepository
from lib.booking import Booking
from datetime import date, timedelta




def test_all(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()
    assert bookings == [
    Booking(date(2026,1,10), 1, True, 1, 1),
    Booking(date(2026,1,11), 2, True, 2, 2),
    Booking(date(2026,1,12), 3, True, 3, 3),
    Booking(date(2026,1,10), 2, True, 3, 4),
    Booking(date(2026,1,10), 1, False, 4, 5)
    ]




def test_find(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    found = repository.find(1) 
    assert found == Booking(date(2026,1,10),1,True,1,1)

def test_available_dates(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    today = date.today()
    tomorrow = today + timedelta(days=1)
    found = repository.get_available_dates(1,2)
    assert found == [today, tomorrow]

def test_available_dates_doesnt_show_booked(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    today = date.today()
    tomorrow = today + timedelta(days=1)
    found = repository.get_available_dates(1,2)
    repository.create(Booking(today,4,True,2))
    found = repository.get_available_dates(4,2)
    assert found == [tomorrow]

def test_unavailable_dates(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    found = repository.get_unavailable_dates(1) 
    assert found == [date(2026,1,10)]


def test_find_by_host(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repo = BookingRepository(db_connection)
    result = repo.find_by_host(1)
    assert result == [
        Booking(date(2026,1,10), 1, True, 1, 1),
        Booking(date(2026,1,11), 2, True, 2, 2),
        Booking(date(2026,1,10), 2, True, 3, 4),
        Booking(date(2026,1,10), 1, False, 4, 5),
        ]
    
    


def test_create(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = BookingRepository(db_connection)
    repository.create(Booking(date(2026,1,10),4,True,2))
    assert repository.find(6) == Booking(date(2026,1,10),4,True,2,6)


def test_update(db_connection):
    db_connection.test_mode = True
    db_connection.seed('seeds/baobnb_test.sql')
    repo = BookingRepository(db_connection)
    repo.update(1,'confirmed',False)
    
    assert repo.find(1) == Booking(date(2026,1,10),1,False,1,1)



# MAKE SURE TO ADD UPDATE METHOD IN TEST_BOOKING

# ALSO ADD FIND WITH USERS OR FINF WITH LOCATION

