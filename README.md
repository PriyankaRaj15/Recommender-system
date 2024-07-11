**Movie Recommender System**

This repository contains a Movie Recommender System built using Python, Pandas, NumPy, NLTK, and scikit-learn. The system uses content-based filtering to recommend movies based on their genres, keywords, cast, crew, and overview.

**Overview**
The Movie Recommender System fetches data from the TMDB API and uses it to create a dataset of movies. It preprocesses this data to extract relevant features such as genres, keywords, cast members, and directors. These features are then combined into a single "tags" column, which is vectorized using CountVectorizer for text processing. Cosine similarity is computed between movies based on these vectors to determine similarity scores.

**Project Structure**
app.py: A Streamlit web application that allows users to input a movie title and get recommendations based on the content-based filtering algorithm.
movie_recommender.py: Python script that builds and trains the recommender system, saving the model and data as pickle files (movie_dict.pkl and similarity.pkl).
tmdb_5000_movies.csv and tmdb_5000_credits.csv: Dataset files used for movie information.

**Setup**

To run the Movie Recommender System locally:

Clone this repository.
Install the required dependencies:
pip install -r requirements.txt
Run the Streamlit app:
streamlit run app.py
Select a movie from the dropdown list and click "Recommend" to see similar movie suggestions.

**Files**

tmdb_5000_movies.csv and tmdb_5000_credits.csv: Original datasets containing movie information.
app.py: Streamlit web application for interactive movie recommendations.
movie_recommender.py: Script to preprocess data, build the recommender system, and save the necessary files.
movie_dict.pkl and similarity.pkl: Pickle files storing processed movie data and similarity matrix respectively.

**Credits**
This project utilizes data from TMDB (The Movie Database) via their API.
Streamlit is used for creating the interactive web application.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
