class Location:
    def __init__(self, name,user_id, description, price_per_night, city, image_1_url, image_2_url, image_3_url, id=None):
        
        self.name = name
        self.user_id = user_id
        self.description = description
        self.price_per_night = price_per_night
        self.city = city
        self.image_1_url = image_1_url
        self.image_2_url = image_2_url
        self.image_3_url = image_3_url
        self.id = id
        

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Location({self.name}, {self.user_id}, {self.description}, {self.price_per_night}, {self.city}, {self.image_1_url}, {self.image_2_url}, {self.image_3_url}, {self.id})"