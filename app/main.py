
from utils import read_data, head, body

import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter
# from streamlit_lottie import st_lottie

st.set_page_config(
    page_title='Movie Recommender',
    # page_icon='assets/icon.png'
)

# def load_lottifile(filename):
#     with open(filename) as f:
#         return json.load(f)
        
# lottie_movie = load_lottifile('assets/movie.json')


head()

with open(r'app/data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'app/titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)


#Applying the KNN algorithms on to the point
def knn(test_point, k):
    target = [0 for item in movie_titles]
    model = KNearestNeighbours(data, target, test_point, k=k)
    model.fit()
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    table = list()
    for i in model.indices:
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table

#All the genres from which a user can select
if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    
    movies = [title[0] for title in movie_titles]
    
    # #Designing of the header and main section of the application.
    # with st.container():
    #  left_column, right_column = st.columns(2)
    #  with left_column:
    #         st.write("")
    #         st.title('MOVIE RECOMMENDER ENGINE') 
    #  with right_column:
    #         st_lottie(lottie_coding, height=300,width=400, key="coding")
        
    
    #Selection basis of recommendation.

    apps = ['*--Select--*', 'Movie based', 'Genres based']   
    app_options = st.selectbox('Method Of Recommendation:', apps)


    
    #If Movie Based Recommendation is being selected this condtion will get executed.
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select a movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select a movie')
        else:
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n)
            st.write("")
            st.write("")
            st. markdown("<h1 style='text-align: center;'> RECOMMENDED MOVIES ???? </h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            for movie, link in table:
                st.success(movie)
                st.markdown(f"???? IMDB LINK --- [{movie}]({link})")

        
    #If Genre Based Recommendation is being selected this condtion will get executed.
    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            st.write("")
            st.write("")
            st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> RECOMMENDED MOVIES ???? </h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            for movie, link in table:
                # Displays movie title with link to imdb
                st.success(movie)
                st.markdown(f"???? IMDB LINK --- [{movie}]({link})")

        else:
                st.write(" _Can Select Multiple Genres_ ")
                        

    else:
        st.write('Select option')

    # st_lottie(animation_data=lottie_movie, speed=1, height=400,loop = True, key='Yeee')