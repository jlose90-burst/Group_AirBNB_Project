from lib.Location import Location


class LocationRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM locations ORDER BY id ASC"
        )
        locations = []
        for row in rows:
            item = Location(
                row["name"],
                row["user_id"],
                row["description"],
                row["price_per_night"],
                row["city"],
                row["image_1_url"],
                row["image_2_url"],
                row["image_3_url"],
                row["id"],
            )
            locations.append(item)
        return locations

    def find(self, location_id):
        rows = self._connection.execute(
            "SELECT * FROM locations WHERE id = %s", [location_id]
        )
        if not rows:
            return None
        row = rows[0]
        return Location(
            row["name"],
            row["user_id"],
            row["description"],
            row["price_per_night"],
            row["city"],
            row["image_1_url"],
            row["image_2_url"],
            row["image_3_url"],
            row["id"],
        )

    def find_by_user(self, user_id):
        locations = []
        rows = self._connection.execute(
            "SELECT * FROM locations WHERE user_id = %s ORDER BY id ASC",
            [user_id],
        )
        for row in rows:
            item = Location(
                row["name"],
                row["user_id"],
                row["description"],
                row["price_per_night"],
                row["city"],
                row["image_1_url"],
                row["image_2_url"],
                row["image_3_url"],
                row["id"],
            )
            locations.append(item)
        return locations

    def create(self, location):
        self._connection.execute(
            """
            INSERT INTO locations (name, user_id, description, price_per_night, city, image_1_url, image_2_url, image_3_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            [
                location.name,
                location.user_id,
                location.description,
                location.price_per_night,
                location.city,
                location.image_1_url,
                location.image_2_url,
                location.image_3_url,
            ],
        )
        return None

    def update(self, location):
        self._connection.execute(
            """
            UPDATE locations
            SET name = %s,
                description = %s,
                price_per_night = %s,
                city = %s,
                image_1_url = %s,
                image_2_url = %s,
                image_3_url = %s
            WHERE id = %s
            """,
            [
                location.name,
                location.description,
                location.price_per_night,
                location.city,
                location.image_1_url,
                location.image_2_url,
                location.image_3_url,
                location.id
            ],
        )
        return None