# Contact Management System - Full Stack (Flask + React)

This project is a full-stack web application built using Flask for the backend and ReactJS for the frontend. The application allows users to manage contacts by adding, updating, viewing, and deleting contact information. The backend uses Flask, Flask-SQLAlchemy, and JWT authentication, while the frontend is built with ReactJS.

## Features

### Backend Features (Flask)

- **User Authentication**:

  - User Registration: Users can create an account by providing a username, email, and password.
  - User Login: Users can log in using their credentials, and a JWT token is generated for accessing protected routes.

- **Contacts Management**:

  - CRUD Operations:

    - **Create Contact**: Users can create new contacts by entering a first name, last name, and email.
    - **Read Contacts**: Users can view all contacts stored in the database.
    - **Update Contact**: Users can update existing contact details.
    - **Delete Contact**: Users can delete contacts from the database.

- **Protected Routes**:

  - JWT authentication is used to protect routes that require login. Only users with valid JWT tokens can access the protected resources.

### Frontend Features (ReactJS)

- **Login and Registration**:

  - A user interface for user registration and login using forms.
  - Displays success or error messages after login and registration attempts.

- **Contact Management**:

  - Users can view, add, update, and delete contacts through a user-friendly interface.
  - Data is fetched from the Flask backend using API calls.

## Technologies Used

### Backend:

- **Flask**: A micro web framework for building the backend.
- **Flask-SQLAlchemy**: For ORM-based database handling.
- **Flask-JWT-Extended**: For JWT-based authentication.
- **Werkzeug**: For password hashing.
- **SQLite**: A lightweight SQL database for storing contact and user data.

### Frontend:

- **ReactJS**: JavaScript library for building the user interface.
- **Axios**: For making API requests to the backend.
- **Bootstrap**: For styling the frontend UI components.

## Installation

### Backend (Flask)

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   The database will be automatically created when the app runs. However, to ensure the database is created, you can run:

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```

5. **Run the Flask server**:

   ```bash
   python app.py
   ```

The backend should now be running on `http://127.0.0.1:5000/`.

### Frontend (ReactJS)

1. **Navigate to the frontend directory**:

   ```bash
   cd <frontend-folder>
   ```

2. **Install the required dependencies**:

   ```bash
   npm install
   ```

3. **Run the React development server**:

   ```bash
   npm start
   ```

The frontend should now be running on `http://localhost:3000/`.

## API Endpoints

### **User Authentication**

- **POST `/register`**: Register a new user.

  - **Request Body**:

    ```json
    {
      "username": "exampleUsername",
      "password": "examplePassword"
    }
    ```

- **POST `/login`**: Log in an existing user.

  - **Request Body**:

    ```json
    {
      "username": "exampleUsername",
      "password": "examplePassword"
    }
    ```

  - **Response**:

    ```json
    {
      "access_token": "your-jwt-token"
    }
    ```

### **Contacts Management**

- **GET `/contacts`**: Get a list of all contacts.

- **POST `/create_contact`**: Create a new contact.

  - **Request Body**:

    ```json
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com"
    }
    ```

- **PATCH `/update_contact/<int:user_id>`**: Update an existing contact.

  - **Request Body**:

    ```json
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "new.email@example.com"
    }
    ```

- **DELETE `/delete_contact/<int:user_id>`**: Delete a contact.

### Protected Route

- **GET `/secure`**: Access a protected resource (requires JWT token).

  - **Request Header**:

    ```bash
    Authorization: Bearer <JWT_TOKEN>
    ```

## Frontend Overview

### **Login Page**

- Users can enter their username and password.
- Upon successful login, the user is redirected to the contact management page.

### **Register Page**

- New users can register by providing a username, password, and email.
- After successful registration, users are redirected to the login page.

### **Contact Management Page**

- A list of contacts is displayed.
- Users can add, update, and delete contacts.
- The contacts are managed through API calls to the Flask backend.

## Dependencies

### Backend (Flask)

- **Flask**: The web framework.
- **Flask-SQLAlchemy**: ORM for database interaction.
- **Flask-JWT-Extended**: For token-based authentication.
- **Werkzeug**: For password hashing.
- **Flask-Cors**: To handle CORS issues between the frontend and backend.

### Frontend (React)

- **React**: The UI library.
- **React-Bootstrap**: For UI components.
- **Axios**: For making HTTP requests to the Flask backend.

## Troubleshooting

### CORS Errors

If you're encountering CORS issues, ensure the Flask backend has the appropriate CORS headers set by using the `flask_cors` extension.

### JWT Token Expiry

JWT tokens have an expiry time. If you're receiving an "unauthorized" error, ensure that the token hasn't expired. You can refresh it or log in again to get a new token.

## License

This project is open-source and available under the MIT License.
