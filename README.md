# Backend for the Library Managment System

## Setup
### Dependencies
- Python 3.6 + pip (usually bundled with python)
- Mysql

### Python Environment
- Install virtualenv to be able to work with an isolated environment (similar to rbenv or NVM but for python).
`pip install virtualenv`
- Setup a new environment inside the project root. This will setup a shim for your python executable and isolate the libraries.
```virtualenv -p <path/to/your/python3> .venv```
- Source the virtual environment. `source .venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`


### Configuration Steps
- Create an environment and install requirements as per mention above
- Create one Superuser
```python manage.py createsuperuser```
- Change database username and password.
- Apply migrations
```python manage.py migrate```
- Finally, run server
```python manage.py runserver```


### Project Details
Create a Library management system that allows the following features for a admin and multiple users -

	- The Admin should be able to add/remove users
    - The Admin/non-admin users able to Login using email and password.
    - The Admin should be able to add/remove a book.
    - The Admin should be able to update a book details.
    - The Admin can give a specific access to the non-admin users using Django admin.


Models : 

- Book
- Custom User Model (to handle email)

Views:

    UserSignupAPIView
        Sign-up
    LoginAPIView
        Log-in
    BookViewSet
        CRUD
        Search

### End-points / Postman collection
- https://www.getpostman.com/collections/d7fd9346708ebc767e9c
    