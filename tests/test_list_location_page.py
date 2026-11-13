from playwright.sync_api import Page, expect

def test_create_new_location_with_images(page: Page, test_web_address, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")

    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="email"]', "tu1@gmail.com")
    page.fill('input[name="password"]', "password1")
    page.click('button[type="submit"]')
    expect(page).to_have_url(f"http://{test_web_address}/locations")
    
    page.goto(f"http://{test_web_address}/locations/new")

    page.fill('input[name="name"]', "Secret Mountain Hideout")
    page.fill('input[name="city"]', "Swiss Alps")
    page.fill('textarea[name="description"]', "Heated lair with helipad access.")
    page.fill('input[name="price_per_night"]', "350")
    page.fill('input[name="image_1_url"]', "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/1200/675/007elementsprnewswire.jpg?ve=1&tl=1")
    page.fill('input[name="image_2_url"]', "https://i.dailymail.co.uk/i/newpix/2018/06/08/17/4D0D4D3100000578-5822101-Licence_to_thrill_007_Elements_will_be_opening_on_top_of_the_Gai-a-47_1528474463284.jpg")
    page.fill('input[name="image_3_url"]', "https://i.dailymail.co.uk/i/newpix/2018/06/08/17/4D0D492300000578-5822101-The_building_that_houses_the_experience_is_on_the_left_of_this_i-a-48_1528474495619.jpg")


    page.locator('.list_form button[type="submit"]').click()
    page.goto(f"http://{test_web_address}/locations/5")
    
    expect(page).to_have_url(f"http://{test_web_address}/locations/5")
    expect(page.locator("body")).to_contain_text("Secret Mountain Hideout")
def test_email_for_new_listing(page:Page):
    page.goto("http://localhost:8025/")
    page.wait_for_timeout(4000)
    expect(page.locator("body")).to_contain_text("Mailpit")

    