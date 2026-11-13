from lib.Location import Location

def test_location_constructs():
    batcave = Location('Batcave',3,'Spacious and full of bats','£150','Gotham',None, None, None,1)
    assert batcave.id == 1
    assert batcave.name == 'Batcave'
    assert batcave.description == 'Spacious and full of bats'
    assert batcave.price_per_night == '£150'
    assert batcave.city == 'Gotham' 
    assert batcave.user_id == 3
    

def test_location_formats():
    batcave = Location('Batcave',3,'Spacious and full of bats','£150','Gotham', None,None,None, 1)
    assert str(batcave) == "Location(Batcave, 3, Spacious and full of bats, £150, Gotham, None, None, None, 1)"



def test_locations_are_equal():
    location = Location('Batcave',3,'Spacious and full of bats','£150','Gotham', None,None,None, 1)
    location2 = Location('Batcave',3,'Spacious and full of bats','£150','Gotham', None,None,None, 1)
    assert location == location2
