import streamlit as st
import pickle
import pandas as pd

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://cdn.mos.cms.futurecdn.net/rDJegQJaCyGaYysj2g5XWY.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #FF0000;
        color: Black;
        border: none;
        padding: 0.5em 1em;
        font-size: 16px;
        border-radius: 8px;
    }

    div.stButton > button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def recommend (movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'What movie would you like us to recommend to you?',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)