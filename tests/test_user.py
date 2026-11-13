from lib.User import User

def test_user_constructs():
    user = User('test_user1','password1','tu1@gmail.com','07513589988',1)
    assert user.id == 1
    assert user.email == 'tu1@gmail.com'
    assert user.username == 'test_user1'
    assert user.phone == '07513589988'
    assert user.password == 'password1'

def test_user_formats():
    user = User('test_user1','password1','tu1@gmail.com','07513589988',1)
    assert str(user) == "User(1, test_user1, password1, tu1@gmail.com, 07513589988)"

def test_users_are_equal():
    user = User('test_user1','password1','tu1@gmail.com','07513589988',1)
    user2 = User('test_user1','password1','tu1@gmail.com','07513589988',1)
    assert user == user2