class User:
    def __init__(self, username,password,email,phone,id=None): 
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.password}, {self.email}, {self.phone})"