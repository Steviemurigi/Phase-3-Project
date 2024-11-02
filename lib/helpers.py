from models.movie import Movie
from models.movieshop import MovieShop

def exit_program():
    print("Goodbye!")
    exit()

def list_movieshops():
    movieshops = MovieShop.get_all()
    for movieshop in movieshops:
        print(movieshop)

def find_movieshop_by_name():
    name = input("Enter the movie shop's name: ")
    movieshop = MovieShop.find_by_name(name)
    print(movieshop) if movieshop else print(
        f'{name} not found')
    
def find_movieshop_by_id():
    id_ = input("Enter the movie shop's id: ")
    movieshop = MovieShop.find_by_id(id_)
    print(movieshop) if movieshop else print (f'Movie shop with id {id_} not found')

def create_movieshop():
    name = input("Enter the movie shop's name: ")
    location = input ("Enter the movie shop's location: ")
    try:
        movieshop= MovieShop.create(name, location)
        print(f'Succesfully created {movieshop}')
    except Exception as exc:
        print("Error creating movieshop: ", exc)

def update_movieshop():
    id_ = input("Enter the movie shop's id: ")
    if movieshop := MovieShop.find_by_id(id_):
        try:
            name = input("Enter the movie shop's new name: ")
            movieshop.name = name
            location = input("Enter the movie shop's new location: ")
            movieshop.location = location
            movieshop.update()
            print(f'Success: {movieshop}')
        except Exception as exc:
            print("Error updating movie shop: ", exc)
    else:
        print(f'Movie shop {id_} not found')

def delete_movieshop():
    id_ = input("Enter the movie shop's id: ")
    if movieshop := MovieShop.find_by_id(id_):
        movieshop.delete()
        print(f'Movie shop {id_} deleted')
    else:
        print(f'Movie shop {id_} not found')

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(movie)

def find_movie_by_title():
    title = input("Enter the movie's title: ")
    movie = Movie.find_by_title(title)
    print(movie) if movie else print(
        f'{title} not found')
    
def find_movie_by_genre():
    genre = input("Enter your preferred movie's genre: ")
    movies = Movie.find_by_genre(genre)
    if movies:
        print(f"Movies in genre '{genre}':")
        for movie in movies:
            print(movie)
    else:
        print(f'{genre} movies not found')
    
def find_movie_by_id():
    id_= input("Enter the movie's id: ")
    movie = Movie.find_by_id(id_)
    print(movie) if movie else print(
        f'Movie {id_} not found')
    
def create_movie():
    title = input("Enter the movie's title: ")
    release_year_input = input("Enter the movie's release year: ")
    genre = input("Enter the movie's genre: ")
    movieshop_id_input = input("Enter the movie shop's id: ")
    try:
        release_year = int(release_year_input)
        movieshop_id = int(movieshop_id_input)
        movie = Movie.create(title, release_year, genre, movieshop_id)
        print(f'Success: {movie}')
    except Exception as exc:
        print("Error creating new movie: ", exc)

def update_movie():
    id_ = input("Enter the movie's id: ")
    if movie := Movie.find_by_id(id_):
        title = input("Enter the movie's new title: ")
        movie.title = title
        
        release_year_input = input("Enter the movie's correct release year: ")
        genre = input("Enter the movie's updated genre: ")
        movie.genre = genre
        
        try:
            movie.release_year = int(release_year_input)  # Convert release year to integer
            movie.update()  # Move this inside the try block
            print(f'Success: {movie}')
        except ValueError:
            print("Invalid input. Please enter a valid integer for the release year.")
        except Exception as exc:
            print("Error updating movie: ", exc)
    else:
        print(f'Movie {id_} not found')


def delete_movie():
    id_ = input("Enter the movie's id: ")
    if movie := Movie.find_by_id(id_):
        movie.delete()
        print(f'Movie {id_} successfully deleted')
    else:
        print(f'Movie {id_} not found')

def list_movieshop_movies():
    movieshop_id_input = input("Enter the movie shop's ID: ")
    try:
        movieshop_id = int(movieshop_id_input)
        movieshop = MovieShop.find_by_id(movieshop_id)
        
        if movieshop:
            movies = movieshop.movies()

            if movies:
                print(f"Movies in Movie Shop ID {movieshop_id}:")
                for movie in movies:
                    print(f"  Title: {movie.title}, Release Year: {movie.release_year}, Genre: {movie.genre}")
            else:
                print(f"No movies found in Movie Shop ID {movieshop_id}.")
        else:
            print(f"Movie shop with ID {movieshop_id} does not exist.")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the movie shop ID.")


    


