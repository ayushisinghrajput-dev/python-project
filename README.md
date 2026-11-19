1. Repository name: movie-rating-analyzer

Project type: Data Analysis and Visualization

Language: Python

Description: A Python application that analyzes movie ratings using Pandas and Matplotlib, calculates average ratings, identifies top and lowest-rated movies, and visualizes genre-wise rating statistics.

Suggested GitHub topics

python pandas matplotlib data-analysis movie-rating data-visualization csv

2. Complete repository structure
This is the recommended folder structure for your project:
movie-rating-analyzer/
│
├── movies.csv
│
├── One.py
│
├── README.md
│
├── .gitignore
│
└── screenshots/
    ├── summary.png
    ├── genre_average.png


3. Repository file contents
A. movies.csv
This file stores the movie dataset.

Create a file named movies.csv and add the following sample data:
Movie,Genre,Rating
Inception,Sci-Fi,8.8
Interstellar,Sci-Fi,8.7
The Dark Knight,Action,9.0
Titanic,Romance,7.9
Avatar,Sci-Fi,7.8
Avengers,Action,8.0
The Notebook,Romance,7.8
Joker,Drama,8.4
Forrest Gump,Drama,8.8
Gladiator,Action,8.5


## Purpose:
- Stores movie names.
- Stores movie genres.
- Stores movie ratings between 0 and 10.
- Provides input data for the analyzer.
B. movie_analyzer.py
This is your main Python source file.

Paste your complete Python code (the code you provided above) into this file.

It contains the following main functions:
Function	Responsibility
load_movies()	Loads and validates CSV records.
display_summary()	Calculates average, highest and lowest ratings.
plot_genre_chart()	Generates a genre-wise bar chart.
genre_wise_average()	Calculates average rating for each genre.
display_charts()	Displays a bar chart and histogram.
main()	Controls the application menu.

# Movie Rating Analyzer

## Project Overview

Movie Rating Analyzer is a Python-based data analysis and visualization application. It analyzes movie information stored in a CSV file and provides useful insights about movie ratings and genres.

The application uses Pandas for data processing and Matplotlib for graphical representation.

## Objectives

- Analyze movie ratings from a CSV dataset.
- Calculate the average movie rating.
- Identify the highest-rated and lowest-rated movies.
- Calculate genre-wise average ratings.
- Identify the best-performing movie genre.
- Display graphical representations of movie ratings.
- Validate input data and handle invalid records.

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV (Comma-Separated Values)

## Project Structure

```text
movie-rating-analyzer/
├── movies.csv
├── One.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## Main Features

### 1. Movie Data Loading
Reads movie information from a CSV file and checks whether the required columns are available.

### 2. Data Validation
Checks missing movie names, missing genres, invalid ratings and ratings outside the permitted range of 0–10.

### 3. Movie Rating Summary
Displays:
- Average movie rating
- Highest-rated movie
- Lowest-rated movie

### 4. Genre-wise Average Rating
Calculates the average rating for each movie genre and identifies the best genre.

### 5. Data Visualization
Generates:
- Genre-wise average rating bar chart.
- Movie rating distribution histogram.

### 6. Menu-driven Interface
Provides four options:
1. Summary
2. Genre-wise Average
3. Display Charts
4. Exit

## Installation

First, install Python on your computer.

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Open the project folder in the terminal and execute:

```bash
python movie_analyzer.py
```

## Dataset Format

The CSV file must contain these columns:

| Movie | Genre | Rating |
|---|---|---|
| Inception | Sci-Fi | 8.8 |
| Titanic | Romance | 7.9 |
| Joker | Drama | 8.4 |

## Expected Output

The program provides movie rating statistics, genre-wise averages and graphical visualizations based on the dataset.

## Error Handling

The application handles:
- Missing CSV files.
- Empty CSV files.
- Invalid CSV formats.
- Missing movie names or genres.
- Invalid numerical ratings.
- Ratings outside the 0–10 range.
- Invalid menu choices.

## Future Enhancements

- Add a graphical user interface.
- Support searching for movies.
- Add movie recommendations.
- Connect to an online movie database API.
- Store and analyze larger movie datasets.

## Conclusion

Movie Rating Analyzer provides a simple and effective way to analyze movie ratings using Python. It combines data processing, validation, statistical calculations and visualization to generate meaningful insights from movie datasets.

Important improvements to your existing code
Your code is already structured well. However, I recommend three small improvements:

1. Remove duplicate chart logic: plot_genre_chart() and the bar chart section in display_charts() perform almost identical work. You can reuse the same plotting function.

2. Improve CSV row numbering: Your current row numbering starts at 1 after the header. If you want actual CSV line numbers, start enumeration at 2.

3. Handle missing or incorrectly formatted column names: Your program checks required columns but should also consider duplicate column names and normalize extra spaces.

Requirements:-

Python 3.9 or later recommended.
Internet connection for the initial installation of the Python packages.
Setup and run
1. Download or clone this repository
git clone https://github.com/ayushisinghrajput-dev/python.git
cd movie-rating-analyzer
If you downloaded the ZIP file, extract it and open a terminal in the extracted movie-rating-analyzer folder.
2. (Recommended) Create a virtual environment
Windows:
py -m venv .venv
.venv\Scripts\activate
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Run the application
Windows:
py One.py
macOS / Linux:
python3 One.py
You can also run python One.py if python points to your Python 3 installation.
Dataset format
Keep movies.csv in the same folder as One.py. The CSV file must have these column headers:
Movie
Genre
Rating
Inception
Sci-Fi
8.8
The Dark Knight
Action
9.0
Titanic
Romance
7.9
Ratings must be numeric values from 0 to 10, inclusive. You can replace the sample records with your own records while keeping the same three column headers.
Menu options
When the program starts, it displays:
===== MOVIE RATING ANALYZER =====
1. Summary
2. Genre-wise Average
3. Display Charts
4. Exit
1 — Summary: prints the overall average rating and the highest- and lowest-rated movies.
2 — Genre-wise Average: prints the average rating for each genre, identifies the best genre, and displays a bar chart.
3 — Display Charts: displays a genre-wise average bar chart and a rating-distribution histogram.
4 — Exit: closes the application.
Data validation and error handling
The application checks whether the CSV file exists, handles empty or unreadable CSV files, verifies that all required columns are present, and skips individual rows with missing movie names, missing genres, invalid ratings, or ratings outside the 0–10 range.
Limitations
The application uses the local CSV dataset; it does not fetch movie information from an online API.
It is a command-line application and does not include a web or desktop interface.
The charts appear in a Matplotlib window, so the environment used to run the program must support graphical display.
Future improvements
Add movie search and filtering.
Add a graphical user interface or web dashboard.
Import movie data from a movie database API.
Add more statistical reports and export options.
Store data in a database for larger datasets.
License
This project is provided for educational and learning purposes. Add a license file if you intend to distribute it under a specific open-source license.Requirements
Python 3.9 or later recommended.
Internet connection for the initial installation of the Python packages.
Setup and run
1. Download or clone this repository
git clone https://github.com/ayushisinghrajput-dev/python-project.git
cd movie-rating-analyzer
If you downloaded the ZIP file, extract it and open a terminal in the extracted movie-rating-analyzer folder.
2. (Recommended) Create a virtual environment
Windows:
py -m venv .venv
.venv\Scripts\activate
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Run the application
Windows:
py One.py
macOS / Linux:
python3 One.py
You can also run python One.py if python points to your Python 3 installation.
Dataset format
Keep movies.csv in the same folder as One.py. The CSV file must have these column headers:
Movie
Genre
Rating
Inception
Sci-Fi
8.8
The Dark Knight
Action
9.0
Titanic
Romance
7.9
Ratings must be numeric values from 0 to 10, inclusive. You can replace the sample records with your own records while keeping the same three column headers.
Menu options
When the program starts, it displays:
===== MOVIE RATING ANALYZER =====
1. Summary
2. Genre-wise Average
3. Display Charts
4. Exit
1 — Summary: prints the overall average rating and the highest- and lowest-rated movies.
2 — Genre-wise Average: prints the average rating for each genre, identifies the best genre, and displays a bar chart.
3 — Display Charts: displays a genre-wise average bar chart and a rating-distribution histogram.
4 — Exit: closes the application.
Data validation and error handling
The application checks whether the CSV file exists, handles empty or unreadable CSV files, verifies that all required columns are present, and skips individual rows with missing movie names, missing genres, invalid ratings, or ratings outside the 0–10 range.
Limitations
The application uses the local CSV dataset; it does not fetch movie information from an online API.
It is a command-line application and does not include a web or desktop interface.
The charts appear in a Matplotlib window, so the environment used to run the program must support graphical display.
Future improvements
Add movie search and filtering.
Add a graphical user interface or web dashboard.
Import movie data from a movie database API.
Add more statistical reports and export options.
Store data in a database for larger datasets.
License
This project is provided for educational and learning purposes. Add a license file if you intend to distribute it under a specific open-source license.

## Test Case :- 1
![alt text](<Screenshot 2026-11-14 191710.png>)

## Test Case :- 2
![alt text](<Screenshot 2026-11-14 191932-1.png>)

## Test Case :- 3
![alt text](<Screenshot 2026-11-14 200340-1.png>)

## Test Case :- 4
![alt text](<Screenshot 2026-11-14 192034-1.png>)