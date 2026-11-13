from playwright.sync_api import Page, expect
from lib.magic_link import create_code

def test_magic_link_logs_user_in(page: Page, test_web_address, db_connection):
    db_connection.seed("seeds/baobnb.sql")
    code = create_code(db_connection, 1)
    page.goto(f"http://{test_web_address}/r/{code}")
    expect(page).to_have_url(f"http://{test_web_address}/requests")

def test_invalid_magic_link_redirects_to_login(page: Page, test_web_address, db_connection):
    db_connection.seed("seeds/baobnb.sql")
    page.goto(f"http://{test_web_address}/r/fake12")
    expect(page).to_have_url(f"http://{test_web_address}/login")

def test_expired_magic_link_redirects_to_login(page: Page, test_web_address, db_connection):
    db_connection.seed("seeds/baobnb.sql")
    code = create_code(db_connection, 1, hours=-1)
    page.goto(f"http://{test_web_address}/r/{code}")
    expect(page).to_have_url(f"http://{test_web_address}/login")