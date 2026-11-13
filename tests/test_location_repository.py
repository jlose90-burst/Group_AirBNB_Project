from lib.Location_repository  import LocationRepository
from lib.Location import Location



def test_all(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = LocationRepository(db_connection)
    locations = repository.all()
    assert locations == [
        Location('Death Star Overlook Quarters', 1, 'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200, 'Deep Space, Alderaan Sector', None, None, None, 1),
        Location ('Endor Shield Generator Bunker', 1, 'Secluded forest bunker with raw industrial charm. Escape the rat race beneath giant redwood canopies in this subterranean, reinforced-durasteel hideaway. Features blast-proof blast doors, dedicated reactor cooling ambiance, and heavy repulsorlift parking on-site. Walkable to pristine forest trails. Note: Local bipedal fauna (Ewoks) can be vocal at dusk; do not leave rations outside.', 150, 'Sanctuary Moon of Endor', None, None, None, 2),
        Location('Isengard Tower of Orthanc', 2, 'Striking historical black-stone spire with courtyard. Stay in an ancient, indestructible stone fortress steeped in wizarding heritage. Features expansive stone balconies overlooking deep iron foundries and timber-cleared grounds. High ceilings, sweeping mountain vistas, and ambient clanking from subterranean artisan pits below. Catering available upon request (salted pork included).', 180, 'Ring of Isengard, Nan Curunír', None, None, None, 3),
        Location ('Island Volcano Cavity Base', 3, 'Chic retro-modern retreat carved into living magma. Unwind in a hollowed-out caldera boasting mid-century lounge decor, an iconic illuminated skull entrance, and indoor monorails. Relax poolside beside our indoor lagoon (complete with laser-guided aquatic wildlife). Includes spinning executive swivel chairs and freeze-thaw chamber access. Zip-line exits only', 200, 'Uncharted Pacific Atoll', None, None, None, 4)

    ]
    

def test_find(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = LocationRepository(db_connection)
    found = repository.find(1) 
    assert found == Location('Death Star Overlook Quarters', 1, 'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200, 'Deep Space, Alderaan Sector',None,None,None, 1)


def test_find_by_user(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = LocationRepository(db_connection)
    found = repository.find_by_user(1) 
    assert found == [Location('Death Star Overlook Quarters', 1, 'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200, 'Deep Space, Alderaan Sector',None,None,None, 1), Location('Endor Shield Generator Bunker',1 ,'Secluded forest bunker with raw industrial charm. Escape the rat race beneath giant redwood canopies in this subterranean, reinforced-durasteel hideaway. Features blast-proof blast doors, dedicated reactor cooling ambiance, and heavy repulsorlift parking on-site. Walkable to pristine forest trails. Note: Local bipedal fauna (Ewoks) can be vocal at dusk; do not leave rations outside.', 150,'Sanctuary Moon of Endor',None,None,None,2)]




def test_create(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repository = LocationRepository(db_connection)
    repository.create(Location('test',4,'description',50,'city', 'url1', 'url2', 'url3'))


    result = repository.all()
    assert result == [
        Location('Death Star Overlook Quarters', 1, 'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200, 'Deep Space, Alderaan Sector',None, None, None, 1),
        Location ('Endor Shield Generator Bunker', 1, 'Secluded forest bunker with raw industrial charm. Escape the rat race beneath giant redwood canopies in this subterranean, reinforced-durasteel hideaway. Features blast-proof blast doors, dedicated reactor cooling ambiance, and heavy repulsorlift parking on-site. Walkable to pristine forest trails. Note: Local bipedal fauna (Ewoks) can be vocal at dusk; do not leave rations outside.', 150, 'Sanctuary Moon of Endor',None, None, None, 2),
        Location('Isengard Tower of Orthanc', 2, 'Striking historical black-stone spire with courtyard. Stay in an ancient, indestructible stone fortress steeped in wizarding heritage. Features expansive stone balconies overlooking deep iron foundries and timber-cleared grounds. High ceilings, sweeping mountain vistas, and ambient clanking from subterranean artisan pits below. Catering available upon request (salted pork included).', 180, 'Ring of Isengard, Nan Curunír',None, None, None, 3),
        Location ('Island Volcano Cavity Base', 3, 'Chic retro-modern retreat carved into living magma. Unwind in a hollowed-out caldera boasting mid-century lounge decor, an iconic illuminated skull entrance, and indoor monorails. Relax poolside beside our indoor lagoon (complete with laser-guided aquatic wildlife). Includes spinning executive swivel chairs and freeze-thaw chamber access. Zip-line exits only', 200, 'Uncharted Pacific Atoll',None, None, None, 4),
        Location('test',4,'description',50,'city', 'url1', 'url2', 'url3', 5)

    ]

def test_update(db_connection):
    db_connection.test_mode = True
    db_connection.seed("seeds/baobnb_test.sql")
    repo = LocationRepository(db_connection)
    updated_location = Location(
        "Volcano Fortress",
        1,
        "Newly renovated magma moat",
        250,
        "Mount Doom",
        "https://example.com/new1.png",
        "https://example.com/new2.png",
        "https://example.com/new3.png",
        1,
    )
    repo.update(updated_location)
    result = repo.find(1)
    assert result == updated_location