## Overview
This project is about managing and tracking keyboards. The API allows you to create, read, update, and delete keyboard data. The data includes the makers, the keyboard name and the type of switches.

## Features
- create read and delete keyboard data
- create read update and delete maker data
- create read and delete switch data
- create a user for oauth2 authentication

## API Endpoints
- `/merken` GET: get all the makers
- `/merken/{id}` GET: get a specific maker
- `/merken` POST: create a new maker
- `/merken/{id}` PUT: update a maker
- `/merken/{id}` DELETE: delete a maker
- `/keyboards` GET: get all the keyboards
- `/keyboards/{id}` GET: get a specific keyboard
- `/keyboards` POST: create a new keyboard
- `/keyboards/{id}` DELETE: delete a keyboard
- `/switches` GET: get all the switches
- `/switches/{id}` GET: get a specific switch
- `/switches` POST: create a new switch
- `/switches/{id}` DELETE: delete a switch
- `/users` GET: get all the users
- `/users/{id}` GET: get a specific user
- `/users` POST: create a new user
- `/users/{id}` DELETE: delete a user
- `/users/me` GET: get the current user 


## Screenshots
- 


## Task list
- [x] 1 API in een GitHub repository
- [x] Beschrijving van het gekozen thema, je API en link naar hosted API op GitHub README.md
- [x] Volledige OpenAPI docs screenshot(s) op GitHub README.md (linkapi/docs (alle mapjes screenshoten)
- [x] Minstens 2 GET endpoints en 1 DELETE endpoint 
- [x] Minstens 1 POST endpoint met class(es)
- [x] Maximaal gebruik van validaties. Gebruik van response model wanneer aangewezen. (kijk naar parameter validaties in cursus)
- [x] Logisch gebruik van path parameters, query parameters en body
- [x] Gebruik van SQLite als database for persistentie
- [x] Docker container voor de API, welke automatisch door GitHub Actions opgebouwd wordt
- [x] Deployment van de API container op Okteto Cloud via Docker Compose

