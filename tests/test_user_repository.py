from lib.User_repository import UserRepository
from lib.User import User



def test_all(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User('test_user1','password1','tu1@gmail.com','07513589988', 1),
        User('test_user2','password2','tu2@gmail.com','07513589989', 2),
        User('test_user3','password3','tu3@gmail.com','07513589980', 3),
        User('test_user4','password4','tu4@gmail.com','07513389989', 4)
    ]

def test_find(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = UserRepository(db_connection)
    found = repository.find(1) 
    assert found == User('test_user1','password1','tu1@gmail.com','07513589988', 1)


def test_find_by_user(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = UserRepository(db_connection)
    found = repository.find_by_username("test_user1") 
    assert found == User('test_user1','password1','tu1@gmail.com','07513589988', 1)

def test_find_by_email(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = UserRepository(db_connection)
    found = repository.find_by_email("tu1@gmail.com") 
    assert found == User('test_user1','password1','tu1@gmail.com','07513589988', 1)

def test_create(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = UserRepository(db_connection)
    repository.create(User('test_user5','password5','tu5@gmail.com','07123478451'))
    result = repository.all()
    assert result == [
        User('test_user1','password1','tu1@gmail.com','07513589988',1),
        User('test_user2','password2','tu2@gmail.com','07513589989',2),
        User('test_user3','password3','tu3@gmail.com','07513589980',3),
        User('test_user4','password4','tu4@gmail.com','07513389989',4),
        User('test_user5','password5','tu5@gmail.com','07123478451',5)
        ]


