# book-oracle
Your personalised Book Prophet powered by cutting-edge ML technology.

<span style="color: red;">
add more description:</span>

<span style="color: red;">- how to use the app</span>

<span style="color: red;">- What is the value of app</span>

<span style="color: red;">- some key feature
</span>

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

## Status of Packages and Libraries
<span style="color: red;"> whether this package/library is deprecated, or not for general release, etc.</span>

## SQL Database
<span style="color: red;"> Not sure what to add here</span>

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


## Description of Table Created from Merged Tables
<span style="color: red;"> finish</span>

## Open API for Book Summary used for NLP
<span style="color: red;"> add link to API documenation</span>

## Web App
<span style="color: red;"> 
- Add description Which app is used: timelit?
- Add link to documentation of app 
</span>

## Random Info that needs to be deleted once the readme.md is finishe
<span style="color: red;"> Information how to design a proper readme.md file. 
https://google.github.io/styleguide/docguide/READMEs.html</span>
