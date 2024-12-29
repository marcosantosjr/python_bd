import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("movies_dataset.csv")

# Basic information
print(df.head())
print(df.info())

# Highest-rated movie
highest_rated = df[df["Rating"] == df["Rating"].max()]
print("Highest Rated Movie:\n", highest_rated)

# Average rating by genre
average_rating = df.groupby("Genre")["Rating"].mean()
print("Average Rating by Genre:\n", average_rating)

# Top 10 highest-grossing movies
top_movies = df.sort_values("Revenue (Millions)", ascending=False).head(10)
print("Top 10 Highest Grossing Movies:\n", top_movies)

# Average revenue by genre
avg_revenue = df.groupby("Genre")["Revenue (Millions)"].mean()
print("Average Revenue by Genre:\n", avg_revenue)


# Bar chart of average ratings by genre
avg_rating = df.groupby("Genre")["Rating"].mean().sort_values()
avg_rating.plot(kind="bar", title="Average Ratings by Genre")
plt.show()

# Scatter plot: Revenue vs Rating
sns.scatterplot(data=df, x="Rating", y="Revenue (Millions)", hue="Genre")
plt.title("Revenue vs Rating")
plt.show()

# Histogram of ratings
df["Rating"].plot(kind="hist", bins=10, title="Distribution of Ratings")
plt.show()

avg_rating_by_year = df.groupby("Year")["Rating"].mean()
avg_rating_by_year.plot(title="Average Rating Over Years")
plt.show()

top_movies_by_genre = df.groupby("Genre").apply(
    lambda x: x.nlargest(5, "Rating")
)
print(top_movies_by_genre)

correlation = df[["Rating", "Revenue (Millions)"]].corr()
print("Correlation:\n", correlation)
