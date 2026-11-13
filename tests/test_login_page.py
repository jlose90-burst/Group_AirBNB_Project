from playwright.sync_api import Page, expect

def test_successful_login_form_submission_redirects_to_locations(page: Page, db_connection, test_web_address): 
    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("tu1@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password1")
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url(f"http://{test_web_address}/locations")

def test_unsuccessful_login_form_submission_redirects_to_locations(page: Page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.get_by_placeholder("Email Address").fill("nesh@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("nesh1")
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url("https://www.youtube.com/watch?v=9RF45wxvf_k")