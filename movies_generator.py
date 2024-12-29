import pandas as pd
import numpy as np

# Generate fake movie data
data = {
    "Movie": [f"Movie_{i}" for i in range(1, 1001)],
    "Genre": np.random.choice(["Action", "Comedy", "Drama", "Horror", "Sci-Fi"], 1000),
    "Rating": np.random.uniform(1, 10, 1000).round(1),
    "Year": np.random.randint(1990, 2023, 1000),
    "Revenue (Millions)": np.random.uniform(10, 500, 1000).round(2),
}

movies_df = pd.DataFrame(data)
movies_df.to_csv("movies_dataset.csv", index=False)