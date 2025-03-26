import pandas as pd
import streamlit as st
import requests

import pickle

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9487be0771d995d947b360d136cef377&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances =similarity[index]
    movies_list = (sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1]))[1:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id= movies.iloc[i[0]]["id"]
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))  # Correct, passing movie_id
    return recommended_movies, recommended_movies_poster


st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names,posters=recommend(selected_movie)
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




