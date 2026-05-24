# Meta-Back-End-Developer-Capstone
assignment solution of the Back-End Developer Capstone by meta


# to run the test
command is  pipenv run python .\littlelemon\manage.py test Restaurant.tests


# DB Setting
'NAME': 'META',  
'USER': 'RAGHAV',  
'PASSWORD': 'RAGHAV',  
'HOST': '127.0.0.1',  
'PORT': '3306',  


# Meta Backend Capstone
This is a capstone project for the Meta Back-End Development course

# Commands

``` bash
python -m venv capstone
capstone\Scripts\activate
pip install django
# create a django project
django-admin startproject littlelemon
# run development server
cd littlelemon
python manage.py runserver
# create a django app 
python manage.py startapp restaurant
# install client
pip3 install mysqlclient
```

```sql
create database RAGHAV;
use RAGHAV;
CREATE USER 'RAGHAV'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON RAGHAV.* TO 'RAGHAV'@'localhost';
```

```bash
python3 manage.py migrate 
python3 manage.py makemigrations
python manage.py createsuperuser
#user:super
#email: super@gmail.com
#password: 123
pip3 install djangorestframework
```

GET in 
http://localhost:8000/api/menu/1

```json
{
    "id": 1,
    "title": "Menu 1",
    "price": "3",
    "inventory": 4
}
```
GET in 
http://localhost:8000/api/menu

- Get all menus

POST http://localhost:8000/api/menu/

BODY
```json
{
    "title": "m2",
    "price": "13.00",
    "inventory": 30
}
```
RESULT
```json
{
    "id": 2,
    "title": "m2",
    "price": "13.00",
    "inventory": 30
}
```


GET in 
http://localhost:8000/api/booking/tables

```json
[
    {
        "id": 1,
        "name": "Booking 1",
        "number_of_guests": 6,
        "booking_date": "2023-06-06T17:41:53Z"
    }
]
```
POST http://localhost:8000/api/api-token-auth/
```json
{
    "token": "a9d223579062329a541eb8eb8206c52c8b15c974"
}
```

Add authorization to the endpoints, so you have to send a header in the request with the Authorization title: Token [VALUE]

```bash
pip install djoser
```

navigate to http://127.0.0.1:8000/auth/token/login/ to get the token  
```
user: "super  
password: "123"
```

use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header

## Testing
```bash
python manage.py test
```


To execute the available unittests, please open the Visual Studio terminal and enter the following command: python manage.py test tests/.
Please ensure that you have activated the virtual environment and navigated into the 'littlelemon' directory prior to running the unit-tests command.

Utilize this path to verify that the web application is serving static HTML content, inclusive of images and styling.
/restaurant

For testing, you can make use of the following API endpoints with Insomnia or Postman clients.
Alternatively, feel free to explore them through your browser of choice.

DJOSER endpoint, for instance, to perform a POST request and register a new user.
/auth/users/

To log in and obtain an authentication token.
/api-token-auth/

To log in using the DJOSER endpoint.
/auth/token/login

Menu items
I am provideding the curl here only change the token rest will automatically taken care
----------------------------------------------
curl --location 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b'

[]

------------------------------------------------
Adding menu item

curl --location 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \
--form 'Title="sugar cane"' \
--form 'Price="10.90"' \
--form 'Inventory="20"'

{
    "ID": 1,
    "Title": "sugar cane",
    "Price": "10.90",
    "Inventory": 20
}

--------------------------------------------
Now listing it

curl --location --request GET 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \


[
    {
        "ID": 1,
        "Title": "sugar cane",
        "Price": "10.90",
        "Inventory": 20
    }
]

---------------------------------
now searching for wrong id
curl --location --request GET 'http://127.0.0.1:8000/restaurant/menu/3' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \

{
    "detail": "No Menu matches the given query."
}


Table reservations
/api/booking/tables/
/api/booking/tables/{bookingId}

curl --location 'http://127.0.0.1:8000/restaurant/booking/tables/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \
--form 'Name="Dr Raghav Atreya"' \
--form 'No_of_guests="10"' \
--form 'BookingDate="2026-05-24T02:28:00.000+05:30"'

{
    "ID": 1,
    "Name": "Dr Raghav Atreya",
    "No_of_guests": 10,
    "BookingDate": "2026-05-23T20:58:00Z"
}


curl --location --request GET 'http://127.0.0.1:8000/restaurant/booking/tables/1/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \
--form 'Name="Dr Raghav Atreya"' \
--form 'No_of_guests="10"' \
--form 'BookingDate="2026-05-24T02:28:00.000+05:30"'

{
    "ID": 1,
    "Name": "Dr Raghav Atreya",
    "No_of_guests": 10,
    "BookingDate": "2026-05-23T20:58:00Z"
}

curl --location --request GET 'http://127.0.0.1:8000/restaurant/booking/tables/10/' \
--header 'Authorization: Token 2a6bbdb35db98ba05bfe4f5d6c1589f6c67e8b6b' \
--form 'Name="Dr Raghav Atreya"' \
--form 'No_of_guests="10"' \
--form 'BookingDate="2026-05-24T02:28:00.000+05:30"'

{
    "detail": "No Booking matches the given query."
}

