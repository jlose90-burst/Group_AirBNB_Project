from playwright.sync_api import Page, expect

def test_create_new_booking(page:Page, db_connection,test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("tu1@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password1")
    page.get_by_role("button", name="Log In").click()
    page.locator("a",has_text="Death Star Overlook Quarters").click()

    page.locator("#dates").select_option("2026-12-10")
    page.get_by_role("button",name="book").click()
    

    expect(page).to_have_url(f"http://{test_web_address}/requests")
def test_book_on_same_day(page:Page, db_connection, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("tu2@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password2")
    page.get_by_role("button", name="Log In").click()
    page.locator("a",has_text="Death Star Overlook Quarters").click()

    page.locator("#dates").select_option("2026-12-11")
    page.get_by_role("button",name="book").click()

def test_deny_booking(page:Page, db_connection,test_web_address):
    

    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("tu1@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password1")
    page.get_by_role("button", name="Log In").click()

    page.locator("a",has_text="My requests").click()
    page.get_by_role("button",name="Deny").first.click()
    expect(page).to_have_url(f"http://{test_web_address}/requests")


def test_accept_booking(page:Page, db_connection,test_web_address):
    

    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("tu1@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password1")
    page.get_by_role("button", name="Log In").click()

    page.locator("a",has_text="My requests").click()
    page.get_by_role("button",name="Confirm").first.click()
    expect(page).to_have_url(f"http://{test_web_address}/requests")

