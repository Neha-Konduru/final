## Project Documentation

### Motivation for the Project:
This project aims to provide an API for managing actors and movies in a casting agency. It allows authorized users to perform CRUD operations on actors and movies based on their roles.

### Hosted API URL:
The API is hosted at [https://final-1-gjn9.onrender.com/].

### Project Dependencies:
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- Auth0 (for authentication)

### Local Development Setup:
1. Clone the repository from [repository_url].
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Set up the Auth0 configuration:
   - Create a new Auth0 account and configure a new API.
   - Obtain the domain, client ID, and client secret.
   - Update the auth.auth module with your Auth0 credentials.
5. Set up the database:
   - Run `python manage.py db init` to initialize the migrations directory.
   - Run `python manage.py db migrate` to generate the initial migration.
   - Run `python manage.py db upgrade` to apply the migration and create the database tables.
6. Start the development server with `python app.py`.
7. Access the API endpoints locally using the provided URL.

### Authentication Setup:
To set up authentication, follow these steps:
1. Create an account on Auth0 and configure a new API.
2. Obtain the domain, client ID, and client secret.
3. Update the auth.auth module with your Auth0 credentials.
4. Define the required roles (Casting Assistant, Casting Director, Executive Producer) in Auth0.
5. Assign roles to users using the Auth0 dashboard.

# API Endpoints Documentation

## GET /actors
* Description: Retrieves a paginated list of actors.
* Required Permissions: Casting Assistant, Casting Director, Executive Producer
* Request Type: GET
### Response:
* 200 OK: Successful request with a list of actors.
* 404 Not Found: No actors found in the database.

## GET /movies
* Description: Retrieves a paginated list of movies.
* Required Permissions: Casting Assistant, Casting Director, Executive Producer
* Request Type: GET
### Response:
* 200 OK: Successful request with a list of movies.
* 404 Not Found: No movies found in the database.

## DELETE /actors/<int:actor_id>
* Description: Deletes the actor with the specified ID from the database.
* Required Permissions: Casting Director, Executive Producer
* Request Type: DELETE
* Request Parameters: actor_id (integer) - ID of the actor to delete.
### Response:
* 200 OK: Actor successfully deleted.
* 404 Not Found: Actor with the specified ID not found.

## DELETE /movies/<int:movie_id>
* Description: Deletes the movie with the specified ID from the database.
* Required Permissions: Executive Producer
* Request Type: DELETE
* Request Parameters: movie_id (integer) - ID of the movie to delete.
### Response:
* 200 OK: Movie successfully deleted.
* 404 Not Found: Movie with the specified ID not found.

## POST /movies
* Description: Adds a new movie to the database.
* Required Permissions: Executive Producer
* Request Type: POST
* Request Body:
{
    "title": "Movie Title",
    "release_date": "YYYY-MM-DD"
}

## POST /actors
* Description: Adds a new actor to the database.
* Required Permissions: Casting Director, Executive Producer
* Request Type: POST
* Request Body:
{
    "name": "Actor Name",
    "age": 30,
    "gender": "Male"
}

## PATCH /movies/<int:movie_id>
* Description: Updates the details of the movie with the specified ID.
* Required Permissions: Casting Director, Executive Producer
* Request Type: PATCH
* Request Parameters: movie_id (integer) - ID of the movie to update.
* Request Body: JSON object with the fields to update (e.g., title, release_date).
### Response:
* 200 OK: Movie details successfully updated.
* 404 Not Found: Movie with the specified ID not found.
* 422 Unprocessable Entity: Invalid data provided for update.

## PATCH /actors/<int:actor_id>
* Description: Updates the details of the actor with the specified ID.
* Required Permissions: Casting Director, Executive Producer
* Request Type: PATCH
* Request Parameters: actor_id (integer) - ID of the actor to update.
* Request Body: JSON object with the fields to update (e.g., name, age, gender).
### Response:
* 200 OK: Actor details successfully updated.
* 404 Not Found: Actor with the specified ID not found.
* 422 Unprocessable Entity: Invalid data provided for update.


### README File:
The README file should include the above project description and setup instructions, along with any additional details about the project structure, configuration files, and usage examples. It should also include information on how to run the provided test cases and contribute to the project.

