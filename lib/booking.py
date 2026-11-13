class Booking:
    def __init__(self,date,location_id,confirmed=False, booker_id=None,id=None):
        self.id = id
        self.date = date
        self.location_id = location_id
        self.booker_id = booker_id
        self.confirmed = confirmed
        
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.date}, {self.location_id}, {self.confirmed}, {self.booker_id}, {self.id})"