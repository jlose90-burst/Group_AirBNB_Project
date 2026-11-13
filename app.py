import os
import smtplib
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.Location_repository import LocationRepository
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.User import User
from lib.User_repository import UserRepository
from email.message import EmailMessage
from lib.emails import Email
from lib.Location import Location
from lib.magic_link import create_code, use_code
from lib.sms_service import send_sms
from lib.message_repository import MessageRepository
from lib.message import Message


# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret")
BASE_URL = os.environ.get("BASE_URL", "http://localhost:5001")

def current_user_id():
    return session.get("user_id")

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index

@app.route('/', methods=['GET'])
def homepage():
    return redirect("/login")

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/login")

@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def save_user():
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone","").strip()
    password = request.form.get("password","")
    password_confirm = request.form.get("password_confirm","")

    if not (username and email and phone and password.strip()):
        return render_template("signup.html", error="All fields are required"), 400
    if password != password_confirm:
        return render_template("signup.html", error="Passwords do not match"), 400

    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    if user_repo.find_by_username(username):
       
        return render_template("signup.html", error="Username already exists"), 400

    if user_repo.find_by_email(email):
        return render_template("signup.html", error="Email already exists"), 400

    new_user = User(username, password, email, phone)
    user_repo.create(new_user)

    test_email = str(email)
    email = Email(connection)
    email.new_user_email(test_email,username)

    return redirect("/login")

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    connection.connect()
    userrepository = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']
    
    user = userrepository.find_by_email(email)

    if user and user.password == password:
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect('/locations')
    else:
        return redirect('https://www.youtube.com/watch?v=9RF45wxvf_kautoplay=1')
    
@app.route('/locations', methods=['GET'])
def get_locations():
    connection = get_flask_database_connection(app)
    connection.connect()
    locationrepository = LocationRepository(connection)
    locations = locationrepository.all()
    
    return render_template('locations.html', locations=locations)


@app.route('/locations/<int:location_id>', methods=['GET'])
def get_book_location(location_id):
    connection = get_flask_database_connection(app)
    connection.connect()
    locationrepository = LocationRepository(connection)
    location = locationrepository.find(location_id)
    bookrepo = BookingRepository(connection)
    availdates = bookrepo.get_available_dates(location_id)

    return render_template('book_location.html', location=location, available_dates = availdates)

@app.route('/locations/<int:location_id>', methods=['POST'])
def book_location(location_id):
    connection = get_flask_database_connection(app)
    bookingrepository = BookingRepository(connection)
    chosen_date = request.form["dates"]
    booker_id = current_user_id()
    booking = Booking(chosen_date, location_id, False, booker_id)
    booking_id = bookingrepository.create(booking)

    email = Email(connection)
    email.new_booking_request_sent(location_id, booker_id, chosen_date)

    host = bookingrepository.find_host_details(location_id)
    if host:
        link = f"{BASE_URL}/r/{create_code(connection, host['host_id'], booking_id)}"
        email.new_booking_request_recieved(location_id, chosen_date, link)
        send_sms(host['phone'],
                 f"Hi {host['username']}, you have a new booking request for "
                 f"{host['location_name']} on {chosen_date}. Review it: {link}")

    return redirect('/requests')

@app.route('/requests', methods=['GET'])
def get_requests():
    connection = get_flask_database_connection(app)
    bookingrepository = BookingRepository(connection)
    user_id = current_user_id()
    my_requests = bookingrepository.find_requests_by_booker(user_id)
    requests_for_my_locations = bookingrepository.find_requests_for_host(user_id)
    return render_template('request.html',
                           my_requests=my_requests,
                           requests_for_my_locations=requests_for_my_locations)

@app.route('/bookings/<int:booking_id>/confirm', methods=['POST'])
def confirm_booking(booking_id):
    connection = get_flask_database_connection(app)
    bookingrepository = BookingRepository(connection)

    booking = bookingrepository.find_booking_details(booking_id)
    rejected = bookingrepository.find_other_requests_details(booking_id)

    bookingrepository.update(booking_id, 'confirmed', True)
    bookingrepository.reject_other_requests(booking_id)

    if booking:
        link = f"{BASE_URL}/r/{create_code(connection, booking['guest_id'], booking_id)}"
        Email(connection).your_booking_has_been_confirmed(booking_id, link)
        send_sms(booking['phone'],
                 f"Hi {booking['username']}, your stay at {booking['location_name']} "
                 f"on {booking['date'].strftime('%d %b %Y')} is confirmed! View it: {link}")

    for other in rejected:
        send_sms(other['phone'],
                 f"Hi {other['username']}, sorry, {other['location_name']} is no longer "
                 f"available on {other['date'].strftime('%d %b %Y')}.")

    return redirect('/requests')

@app.route('/bookings/<int:booking_id>/deny', methods=['POST'])
def deny_booking(booking_id):
    connection = get_flask_database_connection(app)
    bookingrepository = BookingRepository(connection)

    booking = bookingrepository.find_booking_details(booking_id)
    bookingrepository.delete(booking_id)

    if booking:
        send_sms(booking['phone'],
                 f"Hi {booking['username']}, sorry, your request for {booking['location_name']} "
                 f"on {booking['date'].strftime('%d %b %Y')} was declined.")
        email = Email(connection)
        email.your_booking_has_been_denied(booking['username'],booking['location_name'],booking['date'])

    return redirect('/requests')

@app.route('/locations/new', methods=['GET'])
def get_add_location():
    return render_template("list_location.html")

@app.route('/locations/new', methods=['POST'])
def add_location():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login') 
    
    name = request.form.get("name", "").strip()
    city = request.form.get("city", "").strip()
    description = request.form.get("description", "").strip()
    raw_price = request.form.get("price_per_night", "").strip()
    price_per_night = int(raw_price) if raw_price.isdigit() else None

    url1 = request.form.get('image_1_url', "").strip() or None
    url2 = request.form.get('image_2_url', "").strip() or None
    url3 = request.form.get('image_3_url', "").strip() or None
    
    connection = get_flask_database_connection(app)
    location_repo = LocationRepository(connection)
    location = Location(
        name=name,
        user_id=user_id,
        description=description,
        price_per_night=price_per_night,
        city=city,
        image_1_url=url1,
        image_2_url=url2,
        image_3_url=url3
    )

    try:
        location_repo.create(location)
        email = Email(connection)
        email.create_new_location_email(user_id,name)
    except ValueError:
        return render_template("list_location.html", error="Invalid location details provided.")

    return redirect("/locations")

@app.route('/r/<code>')
def magic_login(code):
    connection = get_flask_database_connection(app)
    link = use_code(connection, code)
    if link is None:
        return redirect('/login')
    session['user_id'] = link['user_id']
    if link['booking_id']:
        booking = BookingRepository(connection).find(link['booking_id'])
        if booking.confirmed:
            return redirect(f"/bookings/{booking.id}/chat")
    return redirect('/requests')

@app.route('/bookings/<int:booking_id>/chat', methods=['GET', 'POST'])
def booking_chat(booking_id):
    user_id = current_user_id()
    connection = get_flask_database_connection(app)

    booking_repo = BookingRepository(connection)
    location_repo = LocationRepository(connection)
    message_repo = MessageRepository(connection)

    booking = booking_repo.find(booking_id)
    if not booking or not booking.confirmed:
        return redirect("/requests")

    location = location_repo.find(booking.location_id)
    if not location or user_id not in (booking.booker_id, location.user_id):
        return redirect("/requests")

    if request.method == 'POST':
        content = request.form.get('content', "").strip()
        if content:
            new_message = Message(booking_id=booking.id, sender_id=user_id, content=content)
            message_repo.create(new_message)
        return redirect(f'/bookings/{booking.id}/chat')

    messages = message_repo.find_by_booking(booking.id)
    return render_template(
        'chat.html',
        booking=booking,
        location=location,
        messages=messages,
        current_user_id=user_id
    )

@app.route('/locations/<int:location_id>/edit', methods=['GET'])
def get_edit_location(location_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect('/login')
    connection = get_flask_database_connection(app)
    connection.connect()
    locationrepository = LocationRepository(connection)
    location = locationrepository.find(location_id)

    if not location or location.user_id != user_id:
        return redirect('/locations')

    return render_template('edit_location.html', location=location)

@app.route('/locations/<int:location_id>/edit', methods=['POST'])
def post_edit_location(location_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect('/login')
    connection = get_flask_database_connection(app)
    connection.connect()
    locationrepository = LocationRepository(connection)
    existing = locationrepository.find(location_id)

    if not existing or existing.user_id != user_id:
        return redirect('/locations')

    updated_location = Location(
        request.form.get('name') or existing.name,
        existing.user_id,
        request.form.get('description') or existing.description,
        request.form.get('price_per_night') or existing.price_per_night,
        request.form.get('city') or existing.city,
        request.form.get('image_1_url') or existing.image_1_url,
        request.form.get('image_2_url') or existing.image_2_url,
        request.form.get('image_3_url') or existing.image_3_url,
        location_id,
    )
    locationrepository.update(updated_location)

    return redirect(f'/locations/{location_id}')

@app.route('/my-locations', methods=['GET'])
def get_my_locations():
    user_id = current_user_id()
    if not user_id:
        return redirect('/login')

    connection = get_flask_database_connection(app)
    location_repo = LocationRepository(connection)
    my_locations = location_repo.find_by_user(user_id)

    return render_template('my_locations.html', locations=my_locations)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
