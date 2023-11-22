# book-oracle
Your personalised Book Prophet powered by cutting-edge ML technology.

## Install Virtual Environment
In your terminal navigate to project folder and type: 
```bash
make setup
```

Alternatively you can install your virtual environment 

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