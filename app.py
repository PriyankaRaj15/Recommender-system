import pandas as pd
import streamlit as st

st.title('Movie Recommender System')
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get( "https://api.themoviedb.org/3/movie/{}?api_key=282947ccafec03f1009cb5437f9c720b&language=en-US".format(
        movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        # movie_id = movies.iloc[i[0]].movie_id
        movie_id = movies.iloc[i[0]].id  # Update this line based on the correct column name

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    #recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movies_poster


# Load movie data and similarity matrix
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movies_name = st.selectbox(
    "Choose a movie",
    movies['title'].values)

#st.write("You selected:", option)
if st.button('Recommend'):
    names, posters = recommend(selected_movies_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
