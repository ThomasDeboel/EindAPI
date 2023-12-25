## Overview
This project is about managing and tracking video games and the platforms on which they were purchased. The API allows you to create, read, update, and delete game and platform data.

## Features
- Create a new game or platform
- Retrieve a list of all games or platforms
- Retrieve details of a specific game or platform
- Delete a game or platform

## API Endpoints
- `POST /platforms/`: Create a new platform
- `GET /platforms/`: Retrieve a list of all platforms
- `GET /platforms/{platform_id}`: Retrieve details of a specific platform
- `POST /platforms/{platform_id}/games/`: Create a new game for a specific platform
- `GET /games/`: Retrieve a list of all games for a specific platform
- `DELETE /platforms/{platform_id}/games/{game_id}`: Delete a specific game for a specific platform


## Screenshots
- `POST /platforms/`: Create a new platform
![Screenshot 1: Post /platforms/ ](./Screens/post_create_platform_1.png)

- `GET /platforms/`: Retrieve a list of all platforms
![Screenshot 2: Get /platforms/ ](./Screens/get_platforms.png)
- 
- `GET /platforms/{platform_id}`: Retrieve details of a specific platform
![Screenshot 3: Get /platforms/{platform_id}](./Screens/get_platforms_id_1.png)

- `POST /platforms/{platform_id}/games/`: Create a new game for a specific platform
![Screenshot 4: Post /platforms/{platform_id}/games/](./Screens/post_create_game_1.png)

- `GET /games/`: Retrieve a list of all games for a specific platform
![Screenshot 5: Get /games/](./Screens/get_games.png)

- `DELETE /platforms/{platform_id}/games/{game_id}`: Delete a specific game for a specific platform
![Screenshot 6: Delete /platforms/{platform_id}/games/{game_id}](./Screens/delete_game_1.png)

- Full Fast API Docs on Okteto
![Screenshot 7: Full page screenshot](./Screens/FastApiOkt.png)

- Small extra home page on Okteto
![Screenshot 8: screenshot of home page of my api](./Screens/homeOkt.png)

- Okteto environment 
![Screenshot 9: screenshot of okteto page](./Screens/Okteto.png)


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

