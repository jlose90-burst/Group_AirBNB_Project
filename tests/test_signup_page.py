from playwright.sync_api import Page, expect

def test_success_signup_form_submission_redirects_to_login(page: Page, db_connection, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.get_by_placeholder("Username").fill('testuser')
    page.get_by_placeholder("Email Address").fill('test@email.com')
    page.get_by_placeholder("Phone Number").fill('012345678912')
    page.get_by_placeholder("Password", exact=True).fill('password123')
    page.get_by_placeholder("Password Confirmation").fill('password123')
    page.get_by_role("button", name="Sign up").click()
    
    expect(page).to_have_url(f"http://{test_web_address}/login")

def test_failed_signup_if_username_already_exists(page: Page, db_connection, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.get_by_placeholder("Username").fill('testuser')
    page.get_by_placeholder("Email Address").fill('test@email.com')
    page.get_by_placeholder("Phone Number").fill('012345678912')
    page.get_by_placeholder("Password", exact=True).fill('password123')
    page.get_by_placeholder("Password Confirmation").fill('password123')
    page.get_by_role("button", name="Sign up").click()

    expect(page).to_have_url(f"http://{test_web_address}/signup")
    expect(page.locator("text=Username already exists")).to_be_visible()

def test_failed_signup_if_email_already_exists(page: Page, db_connection, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.get_by_placeholder("Username").fill('Thanos')
    page.get_by_placeholder("Email Address").fill('test@email.com')
    page.get_by_placeholder("Phone Number").fill('012345678912')
    page.get_by_placeholder("Password", exact=True).fill('password123')
    page.get_by_placeholder("Password Confirmation").fill('password123')
    page.get_by_role("button", name="Sign up").click()

    expect(page).to_have_url(f"http://{test_web_address}/signup")
    expect(page.locator("text=Email already exists")).to_be_visible()