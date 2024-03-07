Django
- follows MVT design pattern

===========================================
Model
- data from the database
- delivered as ORM
- located in <models.py>

View
- data + template
- located in <views.py>

Template
- the file where we describe how result is presented
- located in <templates> folder

===========================================

to navigate around different pages in website
- <urls.py>
- django checks urls.py ===> calls the view that matches the URL
- checks for relevant models, sends the model data to template folder
- template returns <HTML + Django tags>

===========================================
python -m venv env24                  // set up a virtual environment
    creates subfolders --- include, bin, lib
source env24/bin/activate               // activate the virtual environment
    command prompt is changed to (env24)$
python -m pip install Django            // installs Django

django-admin startproject my_tennis_club            // start the project firsttime
cd my_tennis_club   
python manage.py runserver

# start an app
python manage.py startapp members11
===========================================