import smtplib
from email.message import EmailMessage
class Email:
    def __init__(self,connection):
        self._connection = connection

    def new_user_email(self,email,username):
        test_email = str(email)
        msg = EmailMessage()
        msg.set_content(f"Hi {username}, Welcome to lair BNB")
        msg['Subject'] = "Welcome!"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = test_email
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)

    def create_new_location_email(self,user_id,location_name):
        owner = self._connection.execute('SELECT email, username FROM users where id = %s',[user_id])[0]
        msg = EmailMessage()
        msg.set_content(f"Hi {owner['username']}, Your Location {location_name} is now live on LAIRBNB!")
        msg['Subject'] = "Your New Location is Live!"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = owner['email']
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)
    
    # def update_location(self,):
    #     msg = EmailMessage()
    #     msg.set_content(f"Hi {owner_name}, Your Location {location} has been updated!")
    #     msg['Subject'] = "Update Succesfull!"
    #     msg['From'] = 'LAIRBNB@gmail.com'
    #     msg['To'] = owner_email
    #     with smtplib.SMTP('localhost',1025) as s:
    #         s.send_message(msg)



    def new_booking_request_recieved(self, location_id, date, link=None):
        owner = self._connection.execute('SELECT email, username FROM users where id = (SELECT user_id FROM locations WHERE id =%s)',[location_id])[0]
        location = self._connection.execute('SELECT name FROM locations WHERE id =%s',[location_id])[0]
        msg = EmailMessage()
        msg.set_content(f"Hi {owner['username']}, You have received a new booking request at {location['name']} on {date} ")
        msg['Subject'] = "New Booking Request Received!"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = owner['email']
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)

    def confirm_a_request(self,):
        msg = EmailMessage()
        msg.set_content(f"Hi {owner_name}, You have confirmed a booking at {location_name} on {date}")
        msg['Subject'] = "You have Confirmed a Booking!"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = owner_email
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)

    def new_booking_request_sent(self,location_id, booker_id, date):
        booker = self._connection.execute('SELECT email, username FROM users where id = %s',[booker_id])[0]
        location = self._connection.execute('SELECT name FROM locations WHERE id =%s',[location_id])[0]
        msg = EmailMessage()
        msg.set_content(f"Hi {booker['username']}, You have succesfully sent a new booking request at {location['name']} on {date} ")
        msg['Subject'] = "New Booking Request Sent!"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = booker['email']
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)

    def your_booking_has_been_confirmed(self, booking_id, link=None):
        booker = self._connection.execute('SELECT email, username FROM users where id = (SELECT booker_id FROM bookings WHERE id =%s)',[booking_id])[0]
        location = self._connection.execute('SELECT name FROM locations WHERE id =(SELECT location_id FROM bookings WHERE id =%s)',[booking_id])[0]
        msg = EmailMessage()
        msg.set_content(f"Hi {booker['username']}, Your Booking at {location['name']} has now been confirmed!!")
        msg['Subject'] = f"Pack your bags you are off to {location['name']}! "
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = booker['email']
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)

    def your_booking_has_been_denied(self,booker_name,location_name,date,):
        user = self._connection.execute('SELECT email FROM users where username = %s',[booker_name])[0]
        msg = EmailMessage()
        msg.set_content(f"Hi {booker_name}, sorry, {location_name} is no longer available on {date}")
        msg['Subject'] = "Sorry your booking was unsuccesful this time"
        msg['From'] = 'LAIRBNB@gmail.com'
        msg['To'] = user['email']
        with smtplib.SMTP('localhost',1025) as s:
            s.send_message(msg)