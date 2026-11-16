# Movie Rating Analyzer

## Project Overview

The **Movie Rating Analyzer** is a Python 3 application that reads movie
information from a CSV file and analyzes the ratings. It calculates the
overall average rating, identifies the highest- and lowest-rated movies,
calculates average ratings for each genre, and presents the results
through charts.

The project is designed to demonstrate fundamental Python programming,
CSV file handling, data validation, data analysis, and data
visualization.

## Problem Statement

Movie ratings stored in spreadsheet or CSV files can be difficult to
compare manually. This project provides a simple way to process movie
records, summarize their ratings, compare genres, and visualize the
results.

## Objectives

-   Read movie records from `movies.csv`.
-   Validate movie names, genres, and ratings.
-   Accept ratings only within the range of **0 to 10**.
-   Calculate the overall average rating.
-   Find the top-rated and lowest-rated movies.
-   Calculate the average rating for each genre.
-   Identify the genre with the highest average rating.
-   Display the analysis using a bar chart and a histogram.

## Technologies and Libraries

-   **Python 3** --- application logic and program execution.
-   **Pandas** --- reading the CSV file, storing records in a DataFrame,
    calculating statistics, and grouping records by genre.
-   **Matplotlib** --- displaying charts.
-   **OS** --- checking whether the CSV file exists.
-   **Math** --- checking that ratings are finite numeric values.

## Input File Format

The program reads a file named `movies.csv`. It must contain these
column headers:

  Movie          Genre       Rating
  -------------- --------- --------
  Inception      SciFi          8.8
  Titanic        Romance        7.9
  Interstellar   SciFi          8.6

`Movie` and `Genre` must not be blank. `Rating` must be a valid number
from 0 to 10, inclusive.

## Main Features

1.  **CSV loading:** Reads movie data from `movies.csv`.
2.  **Data validation:** Skips records with missing movie names or
    genres, non-numeric or non-finite ratings, and ratings outside the
    permitted range.
3.  **Overall summary:** Calculates the average rating and displays the
    top-rated and lowest-rated movies.
4.  **Genre-wise analysis:** Groups records by genre, calculates each
    genre's average rating, and identifies the best genre.
5.  **Data visualization:** Displays a genre-wise average rating bar
    chart and a movie rating distribution histogram.
6.  **Interactive menu:** Lets the user choose which analysis to run.

## Program Workflow

1.  Check whether `movies.csv` exists and attempt to read it.
2.  Confirm that the required columns (`Movie`, `Genre`, and `Rating`)
    are present.
3.  Validate each record and keep only valid movie entries.
4.  Display the menu and process the user's selection.
5.  Calculate and display the requested statistics or charts.
6.  Continue until the user selects Exit.

## Menu Options

  -----------------------------------------------------------------------
  Option                              Operation
  ----------------------------------- -----------------------------------
  1                                   Summary --- overall average,
                                      top-rated movie, and lowest-rated
                                      movie

  2                                   Genre-wise Average --- average
                                      rating for each genre and the best
                                      genre

  3                                   Display Charts --- genre-wise bar
                                      chart and rating-distribution
                                      histogram

  4                                   Exit the application
  -----------------------------------------------------------------------

## Main Functions

  -----------------------------------------------------------------------
  Function                            Responsibility
  ----------------------------------- -----------------------------------
  `load_movies(filename)`             Reads the CSV file, validates
                                      records, and returns valid movie
                                      data

  `display_summary(data)`             Displays the overall average,
                                      top-rated movie, and lowest-rated
                                      movie

  `genre_wise_average(data)`          Calculates and displays genre
                                      averages and the best genre

  `plot_genre_chart(genre_average)`   Displays a bar chart of genre-wise
                                      average ratings

  `display_charts(data)`              Displays the genre-wise bar chart
                                      and rating histogram

  `main()`                            Runs the interactive menu and calls
                                      the selected operation
  -----------------------------------------------------------------------

## Validation and Error Handling

The program handles common input and file problems:

-   Reports an error if `movies.csv` is missing or cannot be read.
-   Checks that all required column headers are present.
-   Skips records with a blank movie name or genre.
-   Skips ratings that cannot be converted to numbers.
-   Rejects non-finite ratings and ratings below 0 or above 10.
-   Reports skipped records and the number of valid rows when invalid
    records are found.
-   Displays a message when no valid movie records are available.

## Assignment Test Cases

The project is intended to handle the four scenarios specified in the
assignment:

1.  **Normal input:** Calculates the expected average and identifies the
    top- and lowest-rated movies.
2.  **Boundary / minimum input:** Correctly analyzes a CSV containing
    one valid movie with a rating of 10; that movie is both the top- and
    lowest-rated movie.
3.  **Invalid input:** Skips an out-of-range rating such as `11` and a
    non-numeric rating such as `abc`, then reports the number of valid
    rows.
4.  **Different valid scenario:** Calculates separate genre averages,
    identifies the best genre, and displays the genre-wise bar chart.

## Expected Result

After valid data is loaded, the application can show:

-   Overall average movie rating (formatted to two decimal places).
-   Name and rating of the top-rated movie.
-   Name and rating of the lowest-rated movie.
-   Average rating for each genre.
-   Best-performing genre.
-   A bar chart of genre-wise average ratings.
-   A histogram showing the distribution of movie ratings.

## Conclusion

The **Movie Rating Analyzer** provides a straightforward way to analyze
movie ratings using Python. It combines CSV file handling, data
validation, statistical calculations, genre-based grouping, and
graphical visualization. The project demonstrates practical use of
Python functions, loops, conditional statements, exception handling,
Pandas, and Matplotlib to turn raw movie records into clear and useful
information.

## Test case :- 1
![alt text](<Screenshot 2026-11-14 191710-1.png>)

## Test case :- 2
![alt text](<Screenshot 2026-11-14 191932.png>)

## Test case :- 3
![alt text](<Screenshot 2026-11-14 200340.png>)

## Test case :- 4
![alt text](<Screenshot 2026-11-14 192034.png>)