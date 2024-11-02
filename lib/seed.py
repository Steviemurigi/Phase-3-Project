#!/usr/bin/env python3

from models.movie import Movie
from models.movieshop import MovieShop

def seed_database():
    Movie.drop_table()
    MovieShop.drop_table()
    Movie.create_table()
    MovieShop.create_table()

    cinemagic = MovieShop.create("Cinemagic", "Delta towers, 5th street, shop C2")
    flicks = MovieShop.create("Flicks", "Corner store, 7th avenue")
    Movie.create("Dune: Part Two", 2024, "Action Epic", cinemagic.id)
    Movie.create("Anyone But You", 2023, "Romance", cinemagic.id)
    Movie.create("StrangeLand", 1998, "Horror", cinemagic.id)
    Movie.create("Coming to America", 1988, "Comedy", cinemagic.id)
    Movie.create("Legion", 2010, "Sci-fi", cinemagic.id)
    Movie.create("The Bucket List", 2007, "Comedy", flicks.id)
    Movie.create("The Dark Knight", 2008, "Action Epic", flicks.id)
    Movie.create("Manhunter", 1986, "Thriller", flicks.id)
    Movie.create("The Forgotten", 2004, "Horror", flicks.id)
    Movie.create("Call me by Your Name", 2017, "Romance", flicks.id)
     
seed_database()
print("Seeded database")