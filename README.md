![Logo](/project_cinema_home.png)

# API for project-cinema
This is the repo for the project_cinema back-end powered by django and django rest-framework
including other packages that can be found in the requirements.txt file. Together with the [frontend
application](https://github.com/geraldsanga/project-cinema-frontend) written in Vue js This back-end makes the full project_cinema. Endpoints include
* _auth/registration/_ for user registration
* _auth/login/_ for user authentication
* _core/_ for the core application that holds a number of other endpoints as listed in /core/api/urls.py

## Configuration
You will need [postgres](https://www.postgresql.org/) with [postgis](https://postgis.net/) with all it's dependencies GDAL to name one
for this application to work. Create a database with the name _project_cinema_ with the user postgres.

## The frontend app
Click this 👉 [link](https://github.com/geraldsanga/project-cinema-frontend) to follow installation guides for the frontend application written in Vue.js

##Installation
* clone 🔽 the project
  
* cd ▶️ into the BASE_DIR with
  ```cd project_cinema```
* Install ⚙️ packages with pip
```pip install -r requirements.txt```
  
* make migrations 📑 
``` python manage.py makemigrations  and python manage.py migrate```
  
* create a superuser 👨‍🏫 with
``` python manage.py createsuperuser```
  
* for sanity 🚥 chake run 
```python manage.py collectstatic```

## Start the development server ⚡
``python manage.py runserver``

Now you can go to [localhost:8000](https://127.0.0.1:8000) and enjoy the world of movies
