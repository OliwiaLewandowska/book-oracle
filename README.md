# book-oracle
Oracle is a book recommendation web app that provides personalized book recommendations powered by collaborative and content-based filtering algorithms, embedded into a neural network. It leverages NLP techniques for better-tailored reading suggestions and effortless book discovery.

## Key Features
Get Your Five Perfect Books:<br> 
User logs on to the app an gets 5 book recommendations specifically for this user.

Get Book Based on Favourite Read:<br>
User inputs  favourite book and gets five 
recommendations of books that 
similar readers liked a lot

Get Book Based on Ideal Book Description:<br>
User shares brief description of preferred book 
and receives instant personalized recommendations

Get Book Based on Favourite Genre:<br>
User selects favourite book genre and 
can explore the most beloved books

## The Creators of Book Oracle
- Oliwia Lewandowska
- Janina Kleine
- Neha Shah
- Nina Sophie Pejsa

## Install Virtual Environment
In your terminal navigate to project folder and type: 
```bash
make setup
```

Alternatively you can install your virtual environment with:

```bash
pyenv local 3.11.3
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

## Add New Packages to requirements.txt file
In terminal
-make sure you are in the project folder
-pip install <your-package>
-pip freeze > requirements.txt
then add, commit and push requirements.txt file



## Description of Tables of Original Data
Source of data: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

The original data that was provided consisted of three tables: 
### Books.csv
| ISBN     | Book-Title | Book-Author | Year-Of-Publication| Publisher     | Image-URL-S | Image-URL-M  | Image-URL-L |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| Book ISBN     | Book Title |Book Author |Year of Publication| Publisher of the book | Small Image of the book, amazon link | Medium Size Image of the book, amazon link | Large Image of the book, amazon link |

### Ratings.csv
| User-ID      | ISBN |Book-Rating |
| ----------- | ----------- |----------- 
| Unique User ID     | Book ISBN      |Rating   |

### Users.csv   
| User-ID      | Location |Age |
| ----------- | ----------- |----------- 
| Unique User ID     | Location of User      |User Age   |

### worldcities.csv
| City  | City_ascii | lat     | lng      | Country | Iso2 | Iso3 | Admin_name | Capital | Population | Id         |
|-------|------------|---------|----------|---------|------|------|------------|---------|------------|------------|
| Tokyo | Tokyo      | 35.6897 | 139.6922 | Japan   | JP   | JPN  | Tōkyō      | primary | 37732000   | 1392685764 |



## Description of Table Created from Merged Tables


### small_kaggle_df.csv
This table was created from the above tables. It is the table used for training the model. This table contains only a subset of data:

61.k ratings of 571 books and 30k users.

| Book Title  | Book Author | Year of Publication     | Publisher      | Image URL in Size M | Common_Identifier | User ID | ISBN | Book Rating | Age | City         | Country | Description | Rating Count
|-------|------------|---------|----------|---------|------|------|------------|---------|------------|------------|------------|------------|------------|
| To Kill A Mockingbird | Harper Lee     | 1988| Little Brown Company | http://images.amazon.com/images/P/0446310786.01.MZZZZZZZ.jpg   | 38   | 85526  | 0060935464      | 9 | 36   | Victoria | Canada | The unforgettable novel of...|

The subset was created with the following code:
```bash
#Only Rating above 0
df = df[df['book_rating']>0]

#Only users from US or Canada
df = df[df['country'].str.contains("usa|canada")]
```

## Web App

Book Oracle runs in the Streamlit app. Find the documentation of this app here:<br>
https://docs.streamlit.io/