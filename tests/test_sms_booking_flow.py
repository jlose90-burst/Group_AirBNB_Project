from datetime import date
from playwright.sync_api import Page, expect
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.magic_link import create_code

def test_host_link_from_booking_request_logs_host_in(page: Page, test_web_address, db_connection):
    db_connection.seed("seeds/baobnb.sql")

    # DrDoom logs in and books DrEvil's lair
    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("drdoom@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password4")
    page.get_by_role("button", name="Log In").click()
    page.goto(f"http://{test_web_address}/locations/6")
    page.locator("#dates").select_option(index=1)
    page.get_by_role("button", name="Book").click()

    # A magic link was created for DrEvil, tied to the new booking
    rows = db_connection.execute('SELECT code, user_id, booking_id FROM magic_links')
    assert rows[0]['user_id'] == 3
    assert rows[0]['booking_id'] == 1

    # Log out, then use the link like the host tapping the SMS
    page.context.clear_cookies()
    page.goto(f"http://{test_web_address}/r/{rows[0]['code']}")

    expect(page).to_have_url(f"http://{test_web_address}/requests")
    expect(page.get_by_text("DrDoom")).to_be_visible()
    expect(page.get_by_text("Pending")).to_be_visible()

def test_confirmed_booking_link_opens_chat(page: Page, test_web_address, db_connection):
    db_connection.seed("seeds/baobnb.sql")
    booking_id = BookingRepository(db_connection).create(Booking(date(2026, 12, 1), 6, True, 4))
    code = create_code(db_connection, 4, booking_id)

    page.goto(f"http://{test_web_address}/r/{code}")

    expect(page).to_have_url(f"http://{test_web_address}/bookings/{booking_id}/chat")