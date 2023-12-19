import streamlit as st
import pickle
import numpy as np
#from utils.model_functions import get_book_recommendations

# from streamlit_marquee import streamlit_marquee
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv("data/small_kaggle_df.csv")
#Create a pivot dataset for item-based collaborative filtering
movie_features_df = df.pivot_table(index='book_title',columns='user_id',values='book_rating').fillna(0)

popular_books = ""

# Function to show Top 5 Books
def recommend_top_rated_books():
    global df
    sorted_df = df.sort_values(by="book_rating", ascending=False)
    top_rated_books = sorted_df.head(5)
    result_df = top_rated_books[
        [
            "image_url_m",
            "book_title",
            "book_author",
            "book_rating",
            "year_of_publication",
        ]
    ]
    return result_df

# Display List of all books from dataframe for user selection in sidebar dropdown. Also allows autosuggest
book_list = df["book_title"].unique()

# Modify - get all genre from df column
genre_list = ["science", "spritual", "comedy", "romance", "crime"]

#####  Streamlit App Sidebar Design

user_input = st.sidebar.text_input("Enter User ID")

# Header 1: Top 5 popular books (from baseline model)
st.sidebar.title("Popular Reads")
selected_genre = st.sidebar.selectbox(
    "Type or select Genre from the dropdown", genre_list
)
if st.sidebar.button("Show"):
    #popular_books = get_book_recommendations(user_input, df, loaded_model, n=5)
    st.write("Top 5 Popular Books")
st.write(popular_books)

# Header 2 : Personalized Recommendations based on your Reads: (ANN model)
st.sidebar.title("Tailored to Your Tastes")
if st.sidebar.button("Display"):
    popular_books = recommend_top_rated_books()


# Header 3: Book Title Based (CFIB Model)

#Load the KNN model

with open("knn_itembased.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

#Select a book from the dropdown
st.sidebar.title("Read a book similar to:")
selected_book = st.sidebar.selectbox(
    "Type or select a book from the dropdown", book_list
)

def recommend_similar_books(selected_book):

    global df
    query_index = np.where(movie_features_df.index == selected_book)[0][0]

    #Find the 5 most similar books based on the title
    distances, indices = loaded_model.kneighbors(movie_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)

    #create a list with the top 5 movie titles
    book_list = []
    for i in range(0, len(distances.flatten())):
        if i == 0:
            pass
        else:
            book_list.append(movie_features_df.index[indices.flatten()[i]])

    #subset a df with the top 5 movie titles
    df_subset = df[df['book_title'].isin(book_list)].drop_duplicates(subset=['book_title'], keep='first')
    top_rated_books = df_subset.head(5)
    result_df = top_rated_books[
        [
            "image_url_m",
            "book_title",
            "book_author",
            "book_rating",
            "year_of_publication",
        ]
    ]
    return result_df

if st.sidebar.button("Recommend Me"):
    popular_books = recommend_similar_books(selected_book)

# Header 4: Describe your perfect book for next read (NLP Model)
st.sidebar.title("Describe your Perfect Book")
describe = st.sidebar.text_area("Enter keywords for your next read", height=3)
#if st.sidebar.button("Recommend"):
#    popular_books = recommend_popular_books(selected_book)


# Streamlit app Output Design
st.title("Book Recommendation App")
st.subheader("Reader's Oasis: Uncover the Top Rated Books")
num_columns = 5  # number of columns in the grid

# Split the recommendations into rows and columns
rows, remainder = divmod(len(popular_books), num_columns)
if remainder > 0:
    rows += 1

# Iterate through the rows and columns to create the grid
for i in range(rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        index = i * num_columns + j
        if index < len(popular_books):
            cols[j].image(
                popular_books.iloc[index]["image_url_m"],
                use_column_width=True,
                width=50,
            )
            cols[j].write(f"**Title:** {popular_books.iloc[index]['book_title']}")
            cols[j].write(f"**Author:** {popular_books.iloc[index]['book_author']}")
            cols[j].write(f"**Avg Rating:** {popular_books.iloc[index]['book_rating']}")
            cols[j].write("---")


st.markdown(
    """
---
Capestone Project Made for **- Book Recommendation System** by [Oliwia, Nina, Neha, Janina]
"""
)