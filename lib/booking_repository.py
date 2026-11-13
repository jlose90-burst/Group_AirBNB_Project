from lib.booking import Booking
from lib.Location import Location
from datetime import timedelta, date

class BookingRepository:
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings ORDER BY id ASC")
        bookings = []
        for row in rows:
            item = Booking(row['date'],row['location_id'],row['confirmed'],row['booker_id'],row['id'])
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [booking_id])
        if not rows:
            return None
        row = rows[0]
        return Booking(row['date'],row['location_id'],row['confirmed'],row['booker_id'],row['id'])

    def find_by_booker(self, booker_id):
                bookings = []
                rows = self._connection.execute(
                    'SELECT * from bookings WHERE booker_id = %s ORDER BY date ASC', [booker_id])
                for row in rows:
                    item = Booking(row['date'],row['location_id'],row['confirmed'],row['booker_id'],row['id'])
                    bookings.append(item)
                return bookings

    def find_by_host(self, host_id):
            result = self._connection.execute(
                'SELECT bookings.id, bookings.date, bookings.location_id, bookings.confirmed, bookings.booker_id, locations.user_id as owner_id FROM bookings JOIN locations ON locations.id = bookings.location_id WHERE locations.user_id = %s',[host_id]
            )
            hosts_bookings = []
            for row in result:
                item = Booking(row['date'],row['location_id'],row['confirmed'],row['booker_id'],row['id'])
                hosts_bookings.append(item)

            return hosts_bookings

    def get_unavailable_dates(self, location_id):
            bookings = []
            rows = self._connection.execute(
                'SELECT * from bookings WHERE location_id = %s AND confirmed = True ORDER BY date ASC', [location_id])
            for row in rows:
                item = row['date']
                bookings.append(item)
            return bookings


    def get_available_dates(self,location_id,days_ahead=30):
        unavailable_dates = self.get_unavailable_dates(location_id)
        booked_dates = set(unavailable_dates)
        today = date.today()
        available_dates = []

        for i in range(days_ahead):
            current = today + timedelta(days=i)
            if (current not in booked_dates and current.isoformat() not in booked_dates):
                available_dates.append(current)
        return available_dates
        

    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (date, location_id, confirmed, booker_id) '
            'VALUES (%s, %s, %s, %s) RETURNING id',
            [booking.date, booking.location_id, booking.confirmed, booking.booker_id]
        )
        return rows[0]['id']
    

    def update (self,id, column_name, new_value):
        if column_name == 'confirmed':
            self._connection.execute('UPDATE bookings SET confirmed = %s WHERE id = %s',[new_value,id])
        return None
    
    def find_requests_by_booker(self, booker_id):
        return self._connection.execute('SELECT bookings.id, bookings.date, bookings.confirmed, locations.name AS location_name FROM bookings JOIN locations ON locations.id = bookings.location_id WHERE bookings.booker_id = %s ORDER BY bookings.date ASC', [booker_id])

    def find_requests_for_host(self, host_id):
        return self._connection.execute('SELECT bookings.id, bookings.date, bookings.confirmed, locations.name AS location_name, users.username AS guest_username FROM bookings JOIN locations ON locations.id = bookings.location_id JOIN users ON users.id = bookings.booker_id WHERE locations.user_id = %s ORDER BY bookings.date ASC', [host_id])

    def delete(self, booking_id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [booking_id])
        return None

    def reject_other_requests(self, booking_id):
        self._connection.execute('DELETE FROM bookings WHERE location_id = (SELECT location_id FROM bookings WHERE id =%s) AND date = (SELECT date FROM bookings WHERE id = %s) AND id !=%s',[booking_id,booking_id,booking_id])
        return None

    def find_booking_details(self, booking_id):
        rows = self._connection.execute(
            'SELECT bookings.id, bookings.date, users.id AS guest_id, users.username, users.phone, '
            'locations.name AS location_name '
            'FROM bookings '
            'JOIN users ON users.id = bookings.booker_id '
            'JOIN locations ON locations.id = bookings.location_id '
            'WHERE bookings.id = %s',
            [booking_id]
        )
        return rows[0] if rows else None

    def find_other_requests_details(self, booking_id):
        return self._connection.execute(
            'SELECT bookings.id, bookings.date, users.id AS guest_id, users.username, users.phone, '
            'locations.name AS location_name '
            'FROM bookings '
            'JOIN users ON users.id = bookings.booker_id '
            'JOIN locations ON locations.id = bookings.location_id '
            'WHERE bookings.location_id = (SELECT location_id FROM bookings WHERE id = %s) '
            'AND bookings.date = (SELECT date FROM bookings WHERE id = %s) '
            'AND bookings.id != %s',
            [booking_id, booking_id, booking_id]
        )
    def find_host_details(self, location_id):
        rows = self._connection.execute(
            'SELECT users.id AS host_id, users.username, users.phone, locations.name AS location_name '
            'FROM locations JOIN users ON users.id = locations.user_id '
            'WHERE locations.id = %s',
            [location_id]
        )
        return rows[0] if rows else None

