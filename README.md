
### Make migrations for all apps
python manage.py makemigrations authentication <br>
python manage.py makemigrations patients <br>
python manage.py makemigrations doctors <br>
python manage.py makemigrations mappings <br>

### Apply migrations
python manage.py migrate

### Create a superuser for admin access
python manage.py createsuperuser

### Run the server
python manage.py runserver <br>

### setting up postman
create new collection(example: "Healthcare API"
## Authentication APIs
### User Registration
#### 1) Create a new request:
method: POST <br>
url: http://localhost:8000/api/auth/register/ <br>
body(example JSON file):
```
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "default123",
  "password2": "default123",
  "first_name": "Test",
  "last_name": "User"
}
```

### User Login
#### 1) create a new request:
method: POST <br>
url: http://localhost:8000/api/auth/login/ <br>
body(using aforementioned example): <br>
```
{
  "username": "testuser",
  "password": "default123"
}
```
#### 2) send the request and receive access token and a refresh
###  Set Up Authorization
In "Healthcare API", in variable tab set "variable name" = token and initial value = current value = access token. and in "Authorization" tab select "Bearer Token" and set Token = {{token}}

### Patient Management APIs
#### ADD patient
Method: POST <br>
url: http://localhost:8000/api/patients/ <br>
body: (example case) <br>
```
{
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1985-05-15",
  "gender": "M",
  "phone_number": "1234567890",
  "email": "john.doe@example.com",
  "address": "123 Main St, City, Country",
  "medical_history": "No known medical conditions"
}
```
#### Get patient details:
method: GET <br>
url: http://localhost:8000/api/patients/ <br>
and interested in perticular patient then use this url: http://localhost:8000/api/patients/{id}/ , where ID are in sequential order
#### Update Patient
method: PUT <br>
url: http://localhost:8000/api/patients/{id}/ , update patient with id = {id} <br>
body: (updated entries of above patient details):
```
{
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1985-05-15",
  "gender": "M",
  "phone_number": "9876543210",
  "email": "john.updated@example.com",
  "address": "456 New St, City, Country",
  "medical_history": "Updated medical history"
}
```

#### Delete Patient:
method: DELETE <br>
url: http://localhost:8000/api/patients/{id}/ (delete patient with id = {id}) <br>

### Doctor Management APIs
#### ADD a doctor
method: POST <br>
url: http://localhost:8000/api/doctors/ <br>
body: (example case):
```
{
  "first_name": "Jane",
  "last_name": "Smith",
  "specialization": "Cardiology",
  "license_number": "MED12345",
  "phone_number": "9876543210",
  "email": "jane.smith@hospital.com",
  "address": "789 Hospital Ave, City, Country"
}
```
#### NOTE: other management methods of doctor are same as patient

### Patient-Doctor Mapping APIs
#### Create Mapping
Method: POST <br>
url: http://localhost:8000/api/mappings/ <br>
body: (example case):
```
{
  "patient": 1,
  "doctor": 1,
  "notes": "Regular check-up appointments"
}
```
#### Get All Mappings
Method: GET <br>
url: http://localhost:8000/api/mappings/

#### Get mapping for patient:
method: GET <br>
url: http://localhost:8000/api/mappings/patient/{id}/ , getting mapping for patient with id = {id}

#### Delete mapping
method: DELETE <br>
url: http://localhost:8000/api/mappings/{id of mapping}/ , deleting the mapping with id = {id of mapping}



