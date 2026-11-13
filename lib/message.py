class Message:

    def __init__(self, booking_id, sender_id, content, timestamp=None, id=None, sender_username=None):
        self.id = id
        self.booking_id = booking_id
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp
        self.sender_username = sender_username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Message({self.id}, {self.booking_id}, {self.sender_id}, {self.content}, {self.timestamp})"