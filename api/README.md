# Django Rest API

## Getting Started
Prerequisites
- python
- virtualenv

### Initial setup
Create a new virtual enviorment with virtualenv and activate
```
virtualenv venv
source venv/bin/activate
```
Install the required python libraries from requirements.txt
```
pip install -r requirements.txt
```

To make sure the database has the right tables from the models in the project, navigate to the `api` folder (same level as the `manage.py` file is located) and run these commands:
```
python manage.py makemigrations
python manage.py migrate
```

To run the project:
```
python manage.py runserver
```

### Import data
There is a script in the photos folder of the project that takes the photos.csv file from the files folder, this script will truncate the photos table in sqlite database and import data from the photos.csv file into the photos table.

```
python manage.py import_photos
```

Create a superuser and verify data got imported:
```
python manage.py createsuperuser
```
After creating a new admin user log into the admin page

```
python manage.py runserver
```
Open your browser and navigate to `http://localhost:8000/admin`
Use you credentials to login, click on the link labelled Photos and it will take you to the photos page which you'll see all the photos in the database.

## JWT Authentication
This project uses JWT Tokens for authentication. Here are the following endpoints to consider:
- Login (Auth Token): /api/token/
- Refresh Token: /api/token/refresh/
- Verify Token: /api/token/verify/

For more information here is the SimpleJWT library: [https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation]

## Photos API
Photos api you'll be able to view all the available photos, create a new one, view a single photo, update and delete. You'll have to logged in, in oreder to view the photos data. If you are using postman or another tool for testing the endpoints make sure after logging, you provide the Bearer Token in your Authorization Headers

Endpoints:
- /photos/
    - GET Request: View all of the data for the photos table
    - POST Request: Creates a new photos entry into the database
    - POST Request data:
    ```
    {
        "width": integer,
        "height": integer,
        "url": string,
        "photographer": string,
        "photographer_url": string,
        "photographer_id": number,
        "avg_color": string,
        "original": string,
        "large2x": string,
        "large": string,
        "medium": string,
        "small": string,
        "portrait": string,
        "landscape": string,
        "tiny": string,
        "alt": string
    }
    ```
- /photos/<int: photo_id>/
    - GET Request: View the photo with the specific id that is provided (photo_id)
    - PUT Request: Updates the a photo based on id (photo_id) with the data provided in the call
    - DELETE Request: Deletes the photo with the photo_id provided
