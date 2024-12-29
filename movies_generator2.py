import json
import random
import string

# Predefined list of genres
genres = ["Sci-Fi", "Drama", "Crime", "Action", "Thriller", "Animation", "Adventure", "Comedy", "Fantasy"]

# Function to generate a random movie title
def generate_title():
    words = ["The", "Rise", "Fall", "Legacy", "Quest", "Chronicles", "Saga", "Shadows", "Light", "Empire"]
    return f"{random.choice(words)} of {random.choice(words)}"

# Function to generate a random movie entry
def generate_movie():
    title = generate_title()
    genre = random.choice(genres)
    rating = round(random.uniform(6.0, 9.5), 1)  # Random rating between 6.0 and 9.5
    return {"title": title, "genre": genre, "rating": rating}

# Function to generate and save a JSON file
def generate_json_file(filename="movies.json", num_movies=100):
    unique_titles = set()  # To ensure unique titles
    movies = []

    while len(movies) < num_movies:
        movie = generate_movie()
        if movie["title"] not in unique_titles:  # Avoid duplicate titles
            unique_titles.add(movie["title"])
            movies.append(movie)

    with open(filename, "w") as file:
        json.dump(movies, file, indent=4)
    print(f"{num_movies} movies saved to {filename}")

# Generate the file
generate_json_file("movies.json", 100)
