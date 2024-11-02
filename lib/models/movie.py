from models.__init__ import CURSOR, CONN
from models.movieshop import MovieShop

class Movie:

    all = {}

    def __init__(self, title, release_year, genre, movieshop_id, id = None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.movieshop_id = movieshop_id

    def __repr__(self):
        return (
            f"<Movie {self.id} : Title = '{self.title}', Release year = {self.release_year}, "
            f"genre = '{self.genre}', Movie shop id = {self.movieshop_id}>"
        )
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (isinstance(title, str) and title) or (isinstance(title, int) and title != 0):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string or a non-zero integer")

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        if isinstance(release_year, int):
            self._release_year = release_year
        else:
            raise ValueError(
                "Release Year must be an integer"
            )

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")
        
    @property
    def movieshop_id(self):
        return self._movieshop_id

    @movieshop_id.setter
    def movieshop_id(self, movieshop_id):
        if type(movieshop_id) is int and MovieShop.find_by_id(movieshop_id):
            self._movieshop_id = movieshop_id
        else:
            raise ValueError(
                "movieshop_id must reference a movie shop in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT, 
            release_year INTEGER,
            genre TEXT,
            movieshop_id INTEGER,
            FOREIGN KEY (movieshop_id) REFERENCES movieshops(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO movies (title, release_year, genre, movieshop_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.release_year, self.genre, self.movieshop_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE movies
            SET title = ?, release_year = ?, genre = ?, movieshop_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.release_year, self.genre, self.movieshop_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movies
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, title, release_year, genre, movieshop_id):
        movie = cls(title, release_year, genre, movieshop_id)
        movie.save()
        return movie

    @classmethod
    def instance_from_db(cls, row):

        # Check the dictionary for  existing instance using the row's primary key
        movie = cls.all.get(row[0])
        if movie:
            # ensure attributes match row values in case local instance was modified
            movie.title = row[1]
            movie.release_year = row[2]
            movie.genre = row[3]
            movie.movieshop_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            movie = cls(row[1], row[2], row[3], row[4])
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movies
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movies
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM movies
            WHERE title = ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_release_year(cls, release_year):
        sql = """
            SELECT *
            FROM movies
            WHERE release_year = ?
        """

        row = CURSOR.execute(sql, (release_year,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_genre(cls, genre):
        sql = """
            SELECT *
            FROM movies
            WHERE genre = ?
        """

        rows = CURSOR.execute(sql, (genre,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]