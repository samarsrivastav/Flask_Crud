# Flask CRUD Application with MongoDB
## File Structure

- app/__init__.py: Initializes the Flask app and configures the application.
- app/api/users.py: Contains routes and logic for user CRUD operations.
- app/config.py: Configuration settings for the application.
- run.py: Entry point for running the Flask application.
- Dockerfile: Defines the Docker image for the application.
- docker-compose.yml: Defines services, including Flask and MongoDB, and their configurations.
- requirements.txt: Lists Python dependencies for the project.

  
## Steps to run the application in local machine 

## Prerequisites

- Docker: Install Docker from its official website

## Setup and Running

### 1. Clone the Repository
 - go to any directory and open terminal there
 - use the code:<br>
    ``` git clone https://github.com/samarsrivastav/Flask_Crud ``` <br>
    ``` cd Flask_Crud ```

### 2. Build the docker file
- The above project is cloned and you are inside the project
- use the below code to build the docker image<br>
    ``` docker-compose build ```

### 3. Start the docker container
``` docker-compose up ```

### 4. Testing of the Crud application
 -  POST Request to Add a User
    To add a user, send a POST request to http://localhost:8080/user with your JSON body: <br>
    example:
    {
        "name":"test-user",
        "email":"test-user@test",
        "password":"test@password"
    }

 -  GET Request to Retrieve Users (all the user)
    To retrieve all users, send a GET request to http://localhost:8080/user.

 -  GET Request to Retrieve a Specific User
    To retrieve a specific user by ID, send a GET request to http://localhost:8080/user/<id>, replacing <id> with the user's MongoDB ObjectId.

 - PUT Request to Update a User
    To update a user's information, send a PUT request to http://localhost:8080/user/<id> with the updated JSON body.
    
 - DELETE Request to Remove a User
    To delete a user, send a DELETE request to http://localhost:8080/user/<id>.
