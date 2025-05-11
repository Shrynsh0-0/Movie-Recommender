import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://analyticsindiamag.com/wp-content/uploads/2019/05/apps.55787.9007199266246365.687a10a8-4c4a-4a47-8ec5-a95f70d8852d.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommender System")
st.write("Get movie recommendations based on your favorite movie.")

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

selected_movie_name = st.selectbox("Select a movie you like:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("### Recommended Movies:")
    for i, rec in enumerate(recommendations, start=1):
        st.write(f"{i}. {rec}")
