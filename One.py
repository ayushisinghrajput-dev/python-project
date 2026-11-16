import os
import math
import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movies.csv")
COLUMNS = ["Movie", "Genre", "Rating"]


def load_movies(filename):
    """Load CSV data and validate movie records."""

    if not os.path.isfile(filename):
        print("Error: movies.csv file not found.")
        return pd.DataFrame(columns=COLUMNS)

    try:
        data = pd.read_csv(
            filename,
            dtype=str,
            keep_default_na=False,
            encoding="utf-8-sig"
        )

    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        return pd.DataFrame(columns=COLUMNS)

    except (pd.errors.ParserError, OSError, UnicodeError) as error:
        print(f"Error reading CSV file: {error}")
        return pd.DataFrame(columns=COLUMNS)

    data.columns = [str(col).strip() for col in data.columns]

    if not all(col in data.columns for col in COLUMNS):
        print("Error: CSV must contain Movie, Genre, Rating columns.")
        return pd.DataFrame(columns=COLUMNS)

    valid_movies = []
    skipped_count = 0

    for row_number, (_, row) in enumerate(data.iterrows(), start=1):

        movie = str(row["Movie"]).strip()
        genre = str(row["Genre"]).strip()
        rating_text = str(row["Rating"]).strip()

        if not movie:
            print(f"Row {row_number} skipped: Movie name is missing.")
            skipped_count += 1
            continue

        if not genre:
            print(f"Row {row_number} skipped: Genre is missing.")
            skipped_count += 1
            continue

        try:
            rating = float(rating_text)

            if not math.isfinite(rating):
                raise ValueError

        except (ValueError, TypeError):
            print(
                f"Row {row_number} skipped: "
                f"invalid Rating '{rating_text}'."
            )
            skipped_count += 1
            continue

        if rating < 0 or rating > 10:
            print(
                f"Row {row_number} skipped: Rating "
                f"{rating_text} must be between 0 and 10."
            )
            skipped_count += 1
            continue

        valid_movies.append({
            "Movie": movie,
            "Genre": genre,
            "Rating": rating
        })

    result = pd.DataFrame(valid_movies, columns=COLUMNS)

    if skipped_count > 0:
        print(f"Valid rows: {len(result)}")

    return result


def display_summary(data):
    """Display overall movie rating statistics."""

    if data.empty:
        print("No valid movie records available.")
        return

    average = data["Rating"].mean()
    maximum = data["Rating"].max()
    minimum = data["Rating"].min()

    top_movie = data[data["Rating"] == maximum].iloc[0]
    lowest_movie = data[data["Rating"] == minimum].iloc[0]

    print(f"Average rating: {average:.2f}")
    print(
        f"Top rated: {top_movie['Movie']} "
        f"({top_movie['Rating']:g})"
    )
    print(
        f"Lowest: {lowest_movie['Movie']} "
        f"({lowest_movie['Rating']:g})"
    )


def plot_genre_chart(genre_average):
    """Display genre-wise average rating bar chart."""

    plt.figure(figsize=(9, 5))
    genre_average.plot(kind="bar")

    plt.title("Genre-wise Average Rating")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.ylim(0, 10)
    plt.xticks(rotation=45)
    plt.tight_layout()

    print("Bar chart 'Genre-wise Average Rating' displayed")
    plt.show()


def genre_wise_average(data):
    """Calculate genre-wise averages and best genre."""

    if data.empty:
        print("No valid movie records available.")
        return

    genre_average = (
        data.groupby("Genre", sort=False)["Rating"].mean()
    )

    for genre, average in genre_average.items():
        print(f"{genre}: {average:.2f}")

    best_genre = genre_average.idxmax()
    print(f"Best genre: {best_genre}")

    plot_genre_chart(genre_average)


def display_charts(data):
    """Display bar chart and histogram."""

    if data.empty:
        print("No valid movie records available.")
        return

    genre_average = (
        data.groupby("Genre", sort=False)["Rating"].mean()
    )

    # Bar chart
    plt.figure(figsize=(9, 5))
    genre_average.plot(kind="bar")

    plt.title("Genre-wise Average Rating")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.ylim(0, 10)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Histogram
    plt.figure(figsize=(9, 5))
    plt.hist(
        data["Rating"],
        bins=10,
        range=(0, 10),
        edgecolor="black"
    )

    plt.title("Movie Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.xlim(0, 10)
    plt.tight_layout()

    print("Both charts are displayed.")
    plt.show()


def main():
    """Main menu of Movie Rating Analyzer."""

    data = load_movies(CSV_FILE)

    while True:
        print("\n===== MOVIE RATING ANALYZER =====")
        print("1. Summary")
        print("2. Genre-wise Average")
        print("3. Display Charts")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_summary(data)

        elif choice == "2":
            genre_wise_average(data)

        elif choice == "3":
            display_charts(data)

        elif choice == "4":
            print("Thank you for using Movie Rating Analyzer.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()