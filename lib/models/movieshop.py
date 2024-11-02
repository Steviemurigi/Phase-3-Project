from models.__init__ import CURSOR, CONN

class MovieShop:

    all = {}

    def __init__(self, name, location, id = None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<MovieShop {self.id}: {self.name}, {self.location}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError(
                "Location must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movieshops (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movieshops;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO movieshops (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        movieshop = cls(name, location)
        movieshop.save()
        return movieshop

    def update(self):
        sql = """
            UPDATE movieshops
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movieshops
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):

        movieshop = cls.all.get(row[0])
        if movieshop:
            # ensure attributes match row values in case local instance was modified
            movieshop.name = row[1]
            movieshop.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            movieshop = cls(row[1], row[2])
            movieshop.id = row[0]
            cls.all[movieshop.id] = movieshop
        return movieshop

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movieshops
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movieshops
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM movieshops
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def movies(self):
        from models.movie import Movie
        sql = """
            SELECT * FROM movies
            WHERE movieshop_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Movie.instance_from_db(row) for row in rows
        ]