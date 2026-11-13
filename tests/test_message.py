from datetime import datetime
from lib.message import Message


def test_message_constructs():
    time = datetime(2026, 11, 12, 12, 0)
    message = Message(booking_id=1, sender_id=2, content="Hello host!", timestamp=time, id=10, sender_username="spalps")

    assert message.id == 10
    assert message.booking_id == 1
    assert message.sender_id == 2
    assert message.content == "Hello host!"
    assert message.timestamp == time
    assert message.sender_username == "spalps"


def test_messages_are_equal():
    m1 = Message(booking_id=1, sender_id=2, content="Hi", id=1)
    m2 = Message(booking_id=1, sender_id=2, content="Hi", id=1)
    assert m1 == m2