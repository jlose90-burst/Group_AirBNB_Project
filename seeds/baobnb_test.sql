DROP TABLE IF EXISTS magic_links CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP TABLE IF EXISTS locations CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- DROP SEQUENCE IF EXISTS booking_id_seq
-- DROP SEQUENCE IF EXISTS location_id_seq
-- DROP SEQUENCE IF EXISTS user_id_seq;



-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE users (
id SERIAL PRIMARY KEY,
username text,
password text,
email text,
phone text );


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS location_id_seq;
CREATE TABLE locations (
id SERIAL PRIMARY KEY,
name text,
description text,
price_per_night int,
city text,
image_1_url text,
image_2_url text,
image_3_url text, 
user_id int,
CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(id)
ON DELETE cascade


);


CREATE SEQUENCE IF NOT EXISTS booking_id_seq;
CREATE TABLE bookings (
id SERIAL PRIMARY KEY,
date date,
location_id int,
CONSTRAINT fk_location
FOREIGN KEY(location_id)
REFERENCES locations(id)
ON DELETE cascade,
confirmed bool,
booker_id int,
CONSTRAINT fk_booker
FOREIGN KEY(booker_id)
REFERENCES users(id)
ON DELETE cascade

);

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
id SERIAL PRIMARY KEY,
booking_id INT NOT NULL REFERENCES bookings(id) ON DELETE CASCADE,
sender_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
content TEXT NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE magic_links (
    code TEXT PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    booking_id INTEGER REFERENCES bookings(id) ON DELETE CASCADE,
    expires_at TIMESTAMP NOT NULL
);

INSERT INTO users (username, password, email, phone) VALUES ('test_user1','password1','tu1@gmail.com','07513589988');
INSERT INTO users (username, password, email, phone) VALUES ('test_user2','password2','tu2@gmail.com','07513589989');
INSERT INTO users (username, password, email, phone) VALUES ('test_user3','password3','tu3@gmail.com','07513589980');
INSERT INTO users (username, password, email, phone) VALUES ('test_user4','password4','tu4@gmail.com','07513389989');


-- Finally, we add any records that are needed for the tests to run
INSERT INTO locations (name,user_id,description,price_per_night,city) VALUES ('Death Star Overlook Quarters',1 ,'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200,'Deep Space, Alderaan Sector');
INSERT INTO locations (name,user_id,description,price_per_night,city) VALUES ('Endor Shield Generator Bunker',1 ,'Secluded forest bunker with raw industrial charm. Escape the rat race beneath giant redwood canopies in this subterranean, reinforced-durasteel hideaway. Features blast-proof blast doors, dedicated reactor cooling ambiance, and heavy repulsorlift parking on-site. Walkable to pristine forest trails. Note: Local bipedal fauna (Ewoks) can be vocal at dusk; do not leave rations outside.', 150,'Sanctuary Moon of Endor');
INSERT INTO locations (name,user_id,description,price_per_night,city) VALUES ('Isengard Tower of Orthanc',2,'Striking historical black-stone spire with courtyard. Stay in an ancient, indestructible stone fortress steeped in wizarding heritage. Features expansive stone balconies overlooking deep iron foundries and timber-cleared grounds. High ceilings, sweeping mountain vistas, and ambient clanking from subterranean artisan pits below. Catering available upon request (salted pork included).',180,'Ring of Isengard, Nan Curunír');
INSERT INTO locations (name,user_id,description,price_per_night,city) VALUES ('Island Volcano Cavity Base',3,'Chic retro-modern retreat carved into living magma. Unwind in a hollowed-out caldera boasting mid-century lounge decor, an iconic illuminated skull entrance, and indoor monorails. Relax poolside beside our indoor lagoon (complete with laser-guided aquatic wildlife). Includes spinning executive swivel chairs and freeze-thaw chamber access. Zip-line exits only',200,'Uncharted Pacific Atoll');



INSERT INTO bookings (date, location_id, confirmed, booker_id) VALUES ('2026-01-10',1,True,1);
INSERT INTO bookings (date, location_id, confirmed, booker_id) VALUES ('2026-01-11',2,True,2);
INSERT INTO bookings (date, location_id, confirmed, booker_id) VALUES ('2026-01-12',3,True,3);
INSERT INTO bookings (date, location_id, confirmed, booker_id) VALUES ('2026-01-10',2,True,3);
INSERT INTO bookings (date, location_id, confirmed, booker_id) VALUES ('2026-01-10',1,False,4);









