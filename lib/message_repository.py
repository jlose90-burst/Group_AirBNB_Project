from lib.message import Message

class MessageRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_by_booking(self, booking_id):
        rows = self._connection.execute(
            """
            SELECT messages.id, messages.booking_id, messages.sender_id, messages.content, messages.timestamp, users.username AS sender_username
            FROM messages
            JOIN users ON users.id = messages.sender_id
            WHERE messages.booking_id = %s
            ORDER BY messages.timestamp ASC, messages.id ASC
            """,
            [booking_id]
        )

        messages = []
        for row in rows:
            item = Message(
                booking_id=row['booking_id'],
                sender_id=row['sender_id'],
                content =row['content'],
                timestamp=row['timestamp'],
                id=row['id'],
                sender_username=row['sender_username']
            )
            messages.append(item)
        return messages

    def create(self, message):
        self._connection.execute(
            """
            INSERT INTO messages (booking_id, sender_id, content)
            Values (%s, %s, %s)
            """,
            [message.booking_id, message.sender_id, message.content]
        )
        return None