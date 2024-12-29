import json

# Load JSON data from a file
def load_movies(filename="movies.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Save JSON data to a file
def save_movies(data, filename="movies.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_movie(movies):
    title = input("Enter the movie title: ")
    genre = input("Enter the genre: ")
    rating = float(input("Enter the rating (0-10): "))
    movies.append({"title": title, "genre": genre, "rating": rating})
    print(f"Movie '{title}' added successfully!")

def search_movies(movies):
    criteria = input("Search by 'title' or 'genre': ").lower()
    keyword = input("Enter your search keyword: ").lower()

    results = [
        movie for movie in movies
        if keyword in movie[criteria].lower()
    ]

    if results:
        print("Search results:")
        for movie in results:
            print(f"- {movie['title']} ({movie['genre']}), Rating: {movie['rating']}")
    else:
        print("No movies found matching your criteria.")

    def display_movies(movies):
        if movies:
            print("Movie Database:")
            for movie in movies:
                print(f"- {movie['title']} ({movie['genre']}), Rating: {movie['rating']}")
        else:
            print("No movies in the database.")

def display_movies(movies):
    if movies:
        print("Movie Database:")
        for movie in movies:
            print(f"- {movie['title']} ({movie['genre']}), Rating: {movie['rating']}")
    else:
        print("No movies in the database.")

def main():
    movies = load_movies()

    while True:
        print("\nMovie Database Manager")
        print("1. Add a movie")
        print("2. Search for movies")
        print("3. Display all movies")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie(movies)
            save_movies(movies)
        elif choice == "2":
            search_movies(movies)
        elif choice == "3":
            display_movies(movies)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

