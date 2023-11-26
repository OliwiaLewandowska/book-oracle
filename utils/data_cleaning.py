from langdetect import detect
import pandas as pd
import json

# Books DATA CLEANING - Janina Kleine

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'Unknown'

def clean_books(df):
    """
    Perform various data cleaning operations on the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be cleaned.

    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    # Snakecase column names
    df.columns = df.columns.str.replace("-", "_").str.lower()

    #Make the above for-loop more efficient

    for column in ['book_title', 'book_author']:
        df[column] = df[column].str.replace('Ã?Â?', 'ß').str.replace('Ã?Â¼', 'ü').str.replace('Ã¼', 'ü').str.replace('Ã?Â¤', 'ä').str.replace('Ã?Â¶', 'ö').str.replace('Ã?Â©', 'é').str.replace('Ã?Â¨', 'è').str.replace('Ã?Â', 'à').str.replace('àº', 'ú').str.replace('àª', 'ê').str.replace('à§', 'ç').str.replace('à¯', 'ï').str.replace('à«', 'ë').str.replace('à®', 'î').str.replace('à±', 'ñ').str.replace('à¢', 'â').str.replace('à¡', 'á').str.replace('à³', 'ó').str.replace('à´', 'ō').str.replace('à»', 'ū').str.replace('&Amp;', '&').str.replace('ã¡', 'á').str.replace('Ã?', 'ö').str.replace('ã¶', 'ö')

    # Capitalize the first letter of each word in specified columns
    df[['book_title', 'book_author']] = df[['book_title', 'book_author']].apply(lambda x: x.str.title())

    # Imputation of missing publisher values
    df.loc[(df['isbn'] == '1931696993') | (df['isbn'] == '193169656X'), 'publisher'] = "NovelBooks"

    # Drop rows with missing values in 'book_author'
    df.dropna(subset=['book_author'], how='all', inplace=True)

    # Create a unique identifier for each row
    df['identifier'] = range(1, len(df) + 1)

    # Create a common identifier for duplicates, unique for each group
    df['common_identifier'] = df.groupby(['book_title', 'book_author'])['identifier'].transform('first')

    #Create a dictionarty with common identifier and corresponding ISBNs
    common_identifier_dict = df.groupby('common_identifier')['isbn'].unique().to_dict()

    isbn_identifier_dict = {}
    for key, value in common_identifier_dict.items():
        for isbn in value:
            isbn_identifier_dict[isbn] = key

    # Drop duplicates based on 'common_identifier' and keep the first occurence
    df = df.drop_duplicates(subset = 'common_identifier', keep = 'first')

    # Language detection
    #df['language'] = df['book_title'].apply(detect_language)

    # Only keep English books and reset index
    #df = df[df['language'] == 'en'].reset_index(drop=True)

    # Drop columns 'image_url_s' and 'image_url_l'
    df.drop(columns=['image_url_l', 'image_url_s', 'identifier'], axis=1, inplace=True)

    #Drop ISBN since it's ambiguous
    df.drop('isbn', axis=1, inplace=True)

    #Print column names with their data types
    print("Columns and their data types:")
    print(df.dtypes)

    return df, isbn_identifier_dict

## Ratings DATA CLEANING - Neha Shah

def clean_ratings(df):
    
    # Rename columns
    column_name_mapping = {
    'User-ID': 'user_id',
    'Book-Rating': 'book_rating',
    'ISBN': 'isbn'
}

    # Use the rename method to rename the columns
    df.rename(columns=column_name_mapping, inplace=True)
    #Print column names with their data types
    print("Columns and their data types:")
    print(df.dtypes)
    print("")

    # Check for and display duplicate rows
    duplicate_rows = df[df.duplicated(keep=False)]
    print("Number of duplicated rows:{0}".format(len(duplicate_rows)))

    # Check for and display rows with missing values
    missing_values = df[df.isna().any(axis=1)]
    print("\nNumber of rows with missing values:{0}".format(len(missing_values)))

    return df


## Users DATA CLEANING - Nina Pejsa

def clean_users(df):

    #Import mapping table for missing values in country and create a new dataframe
    worldcities_df = pd.read_csv('data/worldcities.csv')

    # clean columns lables
    df.columns = df.columns.str.replace('-','_') #snakecase
    df.columns = df.columns.str.lower() #lowercase
    
    # clean data types
    df['age'].fillna(0, inplace=True) #fill missing age values with 0
    df['location'] = df['location'].astype('str') #change location type to str
    df['age'] = df['age'].astype(int) #change age type to int
    
    # clean age
    df = df.drop(df[df['age'] > 100].index) # remove age outlier >100 
   
    # clean location and split into three columns: country, state, city
    df[['city', 'state', 'country']] = df['location'].str.split(', ', n=2, expand=True) # #split the values of location into three different columns: city, state, country
    df = df.drop('location', axis=1) # remove column 'location' as it is replaced by the three newly created columns: city, state, country
    df['country'] = df['country'].str.replace(',', '') # remove commas from country
    df['city'] = df['city'].str.replace(',', '') # remove commas from city
    df['country'] = df['country'].replace('n/a', '') # empying 'n/a' values

    #remove leading and trailing whitespaces
    df['country'] = df['country'].str.strip()
    df['city'] = df['city'].str.strip()
    
    # clean country: Using a mapping table to fill in missing values and the drop remaining missing values
    city_country_mapping = dict(zip(worldcities_df['city'], worldcities_df['country'])) # Create a dictionary mapping cities to countries
    mapping_dict = {key.lower(): value.lower() for key, value in city_country_mapping.items()}   # Change Dictionary to lower case to ensure case insensitive mapping
    df['country'] = df['country'].fillna(df['city'].map(mapping_dict)) # Mapping of city and country to fill missing values in country
    df = df.dropna(subset=['country']) # drop remaining missing country values
    countrylength_1 = df[df['country'].str.len() == 1] # check for countries with just one character
    df.drop(countrylength_1.index, inplace=True) #drop country with values of one character

    #create dictionary to map country abbreviations
    country_abbr_dict = {'uk': 'united kingdom', 'us': 'usa', 'de': 'germany', 'united states of america':'usa', 'united states':'usa', 'united state':'usa', 'in':'india', 'pa':'panama', 'nh':'netherlands', 'u.':'usa', 'kz':'kazakhstan', 'nl':'netherlands', 'id':'indonesia','pr':'dominican republic', 'gb':'united kingdom','az':'azerbaijan','ua':'ukraine', 'england united kingdom':'united kingdom' }
    #map country abbreviations
    df['country'] = df['country'].replace(country_abbr_dict)#map country abbreviations

    countrylength_2 = df[df['country'].str.len() == 2] # check for values
    df.drop(countrylength_2.index, inplace=True) #drop country with values of one character
    
    # clean state
    df = df.drop('state', axis=1) #Remove state column
   
    # clean city 
    df['city'] = df['city'].replace('\d', '', regex=True) # remove numbers from city names
    df = df.drop(df[df['city'].str.len() == 1].index) # remove values that are only one character long
    df = df.drop(df[df['city'].str.len() == 2].index) #remove values that are only two character long 

    #Map city abbreviations
    city_abbr_dict = {'nyc':'new york', 'new york city': 'new york' }
    df['city'] = df['city'].replace(city_abbr_dict)#map city abbreviations

    #remove values that are only three character long except "nyc"
    df = df.drop(df[(df['city'].str.len() == 3) & (df['city'] != 'nyc')].index)
    df.drop(df[df['city'] == 'n/a'].index, inplace=True)

    #Print column names with their data types
    print("Columns and their data types:")
    print(df.dtypes)

    return df 

