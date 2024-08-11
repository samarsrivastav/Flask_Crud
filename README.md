# Flask CRUD Application with MongoDB

## Steps to run the application in local machine 


## Prerequisites

- Docker: Install Docker from its official website

## Setup and Running

### 1. Clone the Repository
 - go to any directory and open terminal there
 - use the code:
    ``` git clone https://github.com/samarsrivastav/Flask_Crud ```
    ``` cd Flask_Crud ```

### 2. Build the docker file
- The above project is cloned and you are inside the project
- use the below code to build the docker image
    ``` docker-compose build ```

### 3. Start the docker container
``` docker-compose up ```

### 4. Testing of the Crud application
 -  POST Request to Add a User
    To add a user, send a POST request to http://localhost:8080/user with your JSON body:
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