from datetime import date
from unittest.mock import patch
from lib.booking import Booking
from lib.booking_repository import BookingRepository

def login_as_drdoom(web_client):
    web_client.post('/login', data={'email': 'drdoom@gmail.com', 'password': 'password4'})

@patch('app.Email')
@patch('app.send_sms')
def test_host_texted_when_guest_requests(mock_sms, mock_email, web_client, db_connection, monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    db_connection.seed("seeds/baobnb.sql")
    login_as_drdoom(web_client)

    web_client.post('/locations/6', data={'dates': '2026-12-01'})

    phone, message = mock_sms.call_args[0]
    assert phone == '07513589922'
    assert 'Island Volcano Cavity Base' in message
    assert '/r/' in message

@patch('app.Email')
@patch('app.send_sms')
def test_host_email_and_sms_share_same_link(mock_sms, mock_email, web_client, db_connection, monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    db_connection.seed("seeds/baobnb.sql")
    login_as_drdoom(web_client)

    web_client.post('/locations/6', data={'dates': '2026-12-01'})

    email_link = mock_email.return_value.new_booking_request_recieved.call_args[0][2]
    sms_message = mock_sms.call_args[0][1]
    assert email_link in sms_message

@patch('app.Email')
@patch('app.send_sms')
def test_booking_request_link_is_tied_to_booking(mock_sms, mock_email, web_client, db_connection, monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    db_connection.seed("seeds/baobnb.sql")
    login_as_drdoom(web_client)

    web_client.post('/locations/6', data={'dates': '2026-12-01'})

    rows = db_connection.execute('SELECT user_id, booking_id FROM magic_links')
    assert len(rows) == 1
    assert rows[0]['user_id'] == 3
    assert rows[0]['booking_id'] == 1

@patch('app.Email')
@patch('app.send_sms')
def test_guest_texted_and_emailed_when_confirmed(mock_sms, mock_email, web_client, db_connection, monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    db_connection.seed("seeds/baobnb.sql")
    repo = BookingRepository(db_connection)
    repo.create(Booking(date(2026, 12, 1), 6, False, 4))   # DrDoom
    repo.create(Booking(date(2026, 12, 1), 6, False, 1))   # Palpatine, same date

    web_client.post('/bookings/1/confirm')

    assert mock_sms.call_count == 2
    confirmed_phone, confirmed_msg = mock_sms.call_args_list[0][0]
    assert confirmed_phone == '07513589444'
    assert 'confirmed' in confirmed_msg
    rejected_phone, rejected_msg = mock_sms.call_args_list[1][0]
    assert rejected_phone == '07513589988'
    assert 'no longer available' in rejected_msg

    booking_id, link = mock_email.return_value.your_booking_has_been_confirmed.call_args[0]
    assert booking_id == 1
    assert link in confirmed_msg

@patch('app.Email')
@patch('app.send_sms')
def test_guest_texted_when_denied(mock_sms, mock_email, web_client, db_connection, monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    db_connection.seed("seeds/baobnb.sql")
    BookingRepository(db_connection).create(Booking(date(2026, 12, 1), 6, False, 4))

    web_client.post('/bookings/1/deny')

    phone, message = mock_sms.call_args[0]
    assert phone == '07513589444'
    assert 'declined' in message