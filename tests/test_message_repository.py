from lib.database_connection import DatabaseConnection
from lib.message_repository import MessageRepository
from lib.message import Message


def test_create_and_find_messages_by_booking(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")

    repo = MessageRepository(db_connection)

    repo.create(Message(1, 1, "Hi, what time is check-in?"))
    repo.create(Message(1, 2, "Anytime after 3 PM!"))

    messages = repo.find_by_booking(1)

    assert len(messages) == 2
    assert messages[0].content == "Hi, what time is check-in?"
    assert messages[0].sender_id == 1
    assert messages[1].content == "Anytime after 3 PM!"
    assert messages[1].sender_id == 2