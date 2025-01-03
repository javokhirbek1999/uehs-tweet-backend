
# AEHSTweet Backend API Documentation

## Overview

<b>AEHSTweet</b> is a <i>Progressive Web App (PWA)</i> built using <b>React.js</b> that allows users to post tweets, interact with tweets, and view posts from other users. The app supports offline functionality and provides a smooth user experience for both mobile and desktop users.

This is the documentation for Backend.

## App Features
- User registration and login
- Post and view tweets
- Post tweets images by either uploading or capturing from device camera
- Speech to Text feature using device Microphone
- Offline functionality via Service Worker (SW)
- App can be installed on both Desktop and Mobile devices
- Keep tracks of the current user location in the cache
- Clean and responsive design

## <a href="https://aehs-tweet-client.onrender.com/">Live Demo</a>
## <a href='https://github.com/javokhirbek1999/aehs-tweet-client' target='_blank'>Frontend repository</a>

## API Endpoints

### User Registration and Authentication

- `POST /auth/register/`
  - Registers a new user.
  - **Request Body**: 
    ```json
    {
      "username": "string",
      "password": "string",
      "email": "string"
    }
    ```
  
- `POST /auth/login/`
  - Login and obtain a JWT token pair.
  - **Request Body**: 
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

- `POST /auth/login/refresh/`
  - Refresh the JWT token pair.

### Tweets API

- `GET /tweets/`
  - Get a list of all tweets.
  
- `POST /tweets/`
  - Create a new tweet.
  - **Request Body**:
    ```json
    {
      "content": "string",
      "image": "url (optional)"
    }
    ```

## Authentication

The authentication system uses JWT tokens. To get started, make sure to register a user and log in to obtain a token.

**Example login request**:

```bash
curl -X POST http://localhost:8000/auth/login/ -d '{"username": "testuser", "password": "testpassword"}' -H "Content-Type: application/json"
```

**Example tweet creation request**:

```bash
curl -X POST http://localhost:8000/tweets/ -d '{"content": "Hello, world!", "image": upload image file}' -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json"
```

## Running the Backend

To run the AEHSTweet backend locally:

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

The backend should now be running at `http://localhost:8000`.

## Development

To contribute to the backend:

1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b feature-name
    ```

3. Make your changes, then commit and push:
    ```bash
    git add .
    git commit -m "Your commit message"
    git push origin feature-name
    ```

4. Create a pull request.
