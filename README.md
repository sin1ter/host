
# Project Title

A brief description of what this project does 


# Welcome to Movie Management System API 👋

![Version](https://img.shields.io/badge/version-v1-blue.svg?cacheSeconds=2592000)


## Features

- **User Management:**
    - User can signup with email, username and password.
    - User can login with username and password or email and password.
    - Used **JWT authentication** for authentication security.

- **Movie Management:**
  - User add movie records.
  - Only User who created the movie can update, and remove movie records.
  - Ensure unique movie through unique ID.
  - Retrieve detailed information about each movie such as movie title, description, length, genre, created_by, ratings and language.
  - User can rate any movie range to 1 to 5 and can change their own ratings.
  - User can report any movie they seem to be inappropriate. 

- **Admin Features**
  - Admin can see the list of reports which were reported by the users and admin can how many reports were approved and rejected.
  - Admin can approve and reject the movie report. 
  
## Run Locally

Clone the project

```bash
  git clone https://github.com/sin1ter/Movie-Management-System-API.git
```

Go to the project directory

```bash
  cd Movie_Management_System
```

Install dependencies

# For Windows
```bash 
   python -m venv env

   env\Scripts\activate
```

 # For macOS/Linux
 ```bash
   python3 -m venv env
   
   source env/bin/activate
   ```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```
## API Reference


####  Movie Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **POST** | `/api/movie-create/` | To create a new employee record |
| **GET** | `/api/movies/` | To retrieve all movies |
| **GET** | `/api/movie/:id/` | To retrieve details of a single movies |
| **PUT** | `/api/movie/:id/` | To update the details of a single movie |
| **PATCH** | `/api/movie/:id/` | To update a detail of a single movie |
| **DELETE** | `/api/movie/:id/` | To delete a single movie |

#### Rating Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `/api/id/rating/` | To get ratings of particular movie |
| **POST** | `/api/id/rating-create/` | To create a rating for particular movie |
| **GET** | `/api/rating/id/` | To retrieve rating of a single movie |
| **PUT** | `/api/rating/id/` | To update the rating of a single movie who created the movie rating |
| **DELETE** | `/api/rating/id/` | To delete the rating of a single movie who created the movie rating |


#### Report Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `/api/id/report` | To get all the report of a movie |
| **POST** | `/api/id/report-create/` | To create a report for a particular movie |
| **GET** | `/api/report/id/` | To retrieve the report of a specific movie who created the report|
| **PUT** | `/api/report/id/` |To update the report of a specific movie who created the report|
| **DELETE** | `/api/report/id/` | To delete the report of a specific movie who created the report |

#### Admin's Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `/api/admin-report/` | To retrieve all the reports that were reported by the users |
| **PUT** | `/api/report-approve/id/` | To approve the reports of the user |
| **PUT** | `/api/report-reject/id/` | To reject the reports of the user |
| **GET** | `/api/report-status/` | To retrieve all the reports staus such as how many approved and rejected |
## Author

👤 **Symon**

- Github: [@sin1ter](https://github.com/sin1ter)# host
