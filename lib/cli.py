from helpers import(
    exit_program,
    list_movieshops,
    find_movieshop_by_name,
    find_movieshop_by_id,
    create_movieshop,
    update_movieshop,
    delete_movieshop,
    list_movies,
    find_movie_by_title,
    find_movie_by_genre,
    find_movie_by_id,
    create_movie,
    update_movie,
    delete_movie,
    list_movieshop_movies
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_movieshops()
        elif choice == "2":
            find_movieshop_by_name()
        elif choice == "3":
            find_movieshop_by_id()
        elif choice == "4":
            create_movieshop()
        elif choice == "5":
            update_movieshop()
        elif choice == "6":
            delete_movieshop()
        elif choice == "7":
            list_movies()
        elif choice == "8":
            find_movie_by_title()
        elif choice == "9":
            find_movie_by_genre()
        elif choice == "10":
            find_movie_by_id()
        elif choice == "11":
            create_movie()
        elif choice == "12":
            update_movie()
        elif choice == "13":
            delete_movie()
        elif choice == "14":
            list_movieshop_movies()
        else:
            print("Invalid choice")

def menu():
    print("Welcome to Movie Shop Manager! Please select an option:")
    print("0. Exit the program")
    print("1. List all movie shops")
    print("2. Find movie shop by name")
    print("3. Find movie shop by id")
    print("4. Create movie shop")
    print("5. Update movie shop")
    print("6. Delete movie shop")
    print("7. List all movies")
    print("8. Find movie by title")
    print("9. Find movie(s) by genre")
    print("10. Find movie by ID")
    print("11. Create movie")
    print("12. Update movie")
    print("13. Delete movie")
    print("14. List all movies in a movie shop")


if __name__ == "__main__":
    main()