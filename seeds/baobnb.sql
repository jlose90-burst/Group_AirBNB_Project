DROP TABLE IF EXISTS magic_links;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS users;


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

CREATE TABLE magic_links (
    code TEXT PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    booking_id INTEGER REFERENCES bookings(id) ON DELETE CASCADE,
    expires_at TIMESTAMP NOT NULL
);

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
id SERIAL PRIMARY KEY,
booking_id INT NOT NULL REFERENCES bookings(id) ON DELETE CASCADE,
sender_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
content TEXT NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password, email, phone) VALUES ('Sheev Palpatine','password1','spalps@gmail.com','07513589988');
INSERT INTO users (username, password, email, phone) VALUES ('Sarumanthewh!te','password2','sarum4n@gmail.com','07513589988');
INSERT INTO users (username, password, email, phone) VALUES ('DrEvil','password3','drevil@gmail.com','07513589922');
INSERT INTO users (username, password, email, phone) VALUES ('DrDoom','password4','drdoom@gmail.com','07513589444');


INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Death Star Overlook Quarters',1 ,'Panoramic celestial views & ultimate power. Relax in our minimalist, high-vaulted officer suite directly facing the prime superlaser focusing dish. Floor-to-ceiling blast glass offers unmatched vistas of impending planetary doom. Monorail transit to central turbo-lifts, 24/7 complimentary stormtrooper patrol, and private comlink desk. Strictly no non-registered droids; keep exhaust ports clear.', 200,'Deep Space, Alderaan Sector', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Endor Shield Generator Bunker',1 ,'Secluded forest bunker with raw industrial charm. Escape the rat race beneath giant redwood canopies in this subterranean, reinforced-durasteel hideaway. Features blast-proof blast doors, dedicated reactor cooling ambiance, and heavy repulsorlift parking on-site. Walkable to pristine forest trails. Note: Local bipedal fauna (Ewoks) can be vocal at dusk; do not leave rations outside.', 150,'Sanctuary Moon of Endor', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Exegol Sith Citadel',1,'Gothic monolith retreat for dark contemplation. Hidden deep beyond the hyperspace navigation anomalies, this towering obsidian temple boasts inverted basalt ceilings, brooding atmospheric fog, and low ambient chanting. Includes access to private chemical vat laboratories and high-voltage lightning terraces. Navigation beacon required for check-in; steep rocky descent.',180,'Unknown Regions, Exegol', 'None', 'None', 'None');

INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Isengard Tower of Orthanc',2,'Striking historical black-stone spire with courtyard. Stay in an ancient, indestructible stone fortress steeped in wizarding heritage. Features expansive stone balconies overlooking deep iron foundries and timber-cleared grounds. High ceilings, sweeping mountain vistas, and ambient clanking from subterranean artisan pits below. Catering available upon request (salted pork included).',180,'Ring of Isengard, Nan Curunír', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Palantír Observation Chamber',2,'High-altitude observatory with 360° panoptic vision. Perched at the apex of Orthanc, this circular penthouse suite comes with high-speed eagle access and an authentic seeing-stone focal point. Peer across Middle-earth from the comfort of a plush velvet recliner. Ultra-quiet; perfect for remote scheming. Warning: Do not attempt ocular contact with flaming eyes without host approval', 400, 'Orthanc Spire Peak, Isengard', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Island Volcano Cavity Base',3,'Chic retro-modern retreat carved into living magma. Unwind in a hollowed-out caldera boasting mid-century lounge decor, an iconic illuminated skull entrance, and indoor monorails. Relax poolside beside our indoor lagoon (complete with laser-guided aquatic wildlife). Includes spinning executive swivel chairs and freeze-thaw chamber access. Zip-line exits only',200,'Uncharted Pacific Atoll', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Lunar Laser Station',3,'Zero-G orbital pod with literal world-class views. Float away from terrestrial drama in our vacuum-sealed, crater-edge outpost. Highlights include a custom brass-trimmed laser command deck pointing directly at Washington D.C., cryogenic sleeping pods, and dehydrated space ice cream on arrival. Please wear magnetic slippers in shared corridors',320,'Sea of Tranquility, Earths Moon', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Submarine Sub-Aquatic Lair',3,'Sleek nautical bunker for sub-surface cruising. Escape maritime radar in a stealth-rated, chrome-hulled submersible hideaway. Features wraparound observation ports into deep oceanic trenches, pressurized ambient lighting, and wet-dock access for personal minisubs. Motion sickness medication provided; no open flames on level B.',420,'Caribbean Sea Trench', 'None', 'None', 'None');
INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Fortress Castle of Doom',4,'Regal European castle with automated bespoke service. Experience royal Latverian hospitality in this imposing Gothic fortress overlooking cobblestone town squares. Features antique tapestries, vaulted throne halls, and 24-hour concierge service handled exclusively by polite, titanium-plated Doombots. Guests must observe the curfew broadcast from the state clock tower',200,'Doomstadt, Latveria', 'None', 'None', 'None');

INSERT INTO locations (name,user_id,description,price_per_night,city,image_1_url,image_2_url,image_3_url) VALUES ('Orbital Latverian Embassy Platform', 4,'Exclusive diplomatic loft with sovereign extraterritoriality. Hover comfortably in low Earth orbit inside a luxury diplomatic station protected by high-energy force fields. Features state-of-the-art anti-gravity lounges, private docking bays, and immunity from all local Earth law enforcement. Diplomatic visa issued automatically upon booking confirmation.',1000,'Low Earth Orbit, International Airspace', 'None', 'None', 'None');


