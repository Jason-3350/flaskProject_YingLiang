## Assessment with BDD Tests in Python with Flask and Sqlite3
Movie popularity survey and movie selection based on certain options

Find an overview of the popularity of open source library movies. The format of the file is CSV. The APP's first design is to show data in three ways on the website. The first way is to show film ratings, which can be learned through viewing the ratings and selecting the movies. The second way is to collect the same movie genre in the CSV file, and you can use the movie genre to see what specific movies there are. The second is to read the film's plot. You can continue to understand the particular information in the film for the plot you are interested in.

Create four tables in the database to track the movie's success, form, and plot, as well as a link table to connect the data from the first three tables at once.

## Set up the Repository
Git clone this repository into local pc.
Please keep in mind that individual commands can vary depending on the operating system, window, or mac.

We need to start by setting up our development environment by executing these commands in the terminal, that's open in the diretory were we've cloned this repo.

        pyenv local 3.7.0 # this sets the local version of python to 3.7.0
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

## Setting up the Assessment of flask project
Run the setup_db.py file to create the tables, and read the data from CSV files and write into tables.

Load the application settings into your terminal and start the server with 

        export FLASK_APP=app.py 
        export FLASK_ENV=development
        python3 -m flask run 
		
