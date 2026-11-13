from playwright.sync_api import Page, expect
from flask import session
from lib.Location_repository import LocationRepository

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

def test_get_signup(web_client):
    response = web_client.get("/signup")
    assert response.status_code == 200

def test_signup_success_redirects(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "unique-user",
        "email": "user@example.com",
        "phone": "07891234567",
        "password": "mypassword",
        "password_confirm": "mypassword"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"
    
def test_signup_fail_400_password_match(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "unique-user",
        "email": "user@example.com",
        "phone": "07891234567",
        "password": "mypassword",
        "password_confirm": "wrongpassword"
    })
    assert response.status_code == 400

def test_signup_fail_400_empty_username(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "unique-user",
        "email": "user@example.com",
        "phone": "07891234567",
        "password": "mypassword",
        "password_confirm": "wrongpassword"
    })
    assert response.status_code == 400

def test_signup_fail_400_empty_username(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "",
        "email": "user@example.com",
        "phone": "07891234567",
        "password": "mypassword",
        "password_confirm": "mypassword"
    })
    assert response.status_code == 400

def test_signup_fail_400_empty_email(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "unique-user",
        "email": "",
        "phone": "07891234567",
        "password": "mypassword",
        "password_confirm": "mypassword"
    })
    assert response.status_code == 400

def test_signup_fail_400_empty_phone(web_client, db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post("/signup", data={
        "username": "unique-user",
        "email": "user@example.com",
        "phone": "",
        "password": "mypassword",
        "password_confirm": "mypassword"
    })
    assert response.status_code == 400

##### LOGIN PAGE ######

def test_get_login(web_client):
    response = web_client.get("/login")
    assert response.status_code == 200

def test_post_login_success(web_client, db_connection):
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post('/login', data={
        'email': 'tu1@gmail.com',
        'password': 'password1'
    })
    assert response.status_code == 302
    assert response.location == '/locations'

def test_post_login_unsuccessful(web_client, db_connection):
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post('/login', data={
            'email': 'nesh@gmail.com',
            'password': 'nesh1'
        })
    assert response.status_code == 302
    assert response.location == ("https://www.youtube.com/watch?v=9RF45wxvf_kautoplay=1")

def test_logout_success(web_client, db_connection):
    db_connection.seed("seeds/baobnb_test.sql")
    response = web_client.post('/login', data={
            'email': 'tu1@gmail.com',
            'password': 'password1'
    })
    response = web_client.get("/logout")
    assert response.status_code == 302
    assert response.location == "/login"
    assert "user_id" not in session
    assert "username" not in session

def test_get_add_location_200(web_client, db_connection):
    response = web_client.get("/locations/new")
    assert response.status_code == 200

def test_add_location_redirects_adds_to_db(web_client, db_connection):
        db_connection.seed("seeds/baobnb_test.sql")

        with web_client.session_transaction() as sess:
            sess["user_id"] = 1
        response = web_client.post("/locations/new", data ={
            "name": "Room1",
            "user_id": 1,
            "city": "nowhere",
            "description": "a room with a view",
            "price_per_night": "200",
            "image_1_url": "image1.com",
            "image_2_url": "image2.com",
            "image_3_url": "image3.com",
        })
        assert response.status_code == 302
        assert response.location == "/locations"

        repo = LocationRepository(db_connection)
        locations = repo.all()
        assert any(l.name == "Room1" and l.price_per_night == 200 for l in locations)
