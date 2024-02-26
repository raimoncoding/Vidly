<img src="videotape.jpg" alt="Decorative Cassette Tape" width="200"/>

# Vidly Project Documentation

## Project Overview

Vidly is a Django-based web application designed for browsing and renting movies and props. Developed with Python 3.10, it aims to provide a comprehensive platform for movie enthusiasts and prop collectors. The application features an admin page for content management, enabling easy updates to movie and prop listings, and a user-friendly front page that allows customers to explore the catalog efficiently. SQLite is utilized as the database system, ensuring fast and reliable data storage and retrieval.

## Setup and Installation

## Cloning the Repository

To clone the repository and start working on the project locally, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:

`git clone https://github.com/raimoncoding/Vidly.git`

This command will create a local copy of the repository on your machine.


### Initial Setup

1. **Python 3.10 Installation**: Ensure Python 3.10 is installed to take advantage of the latest features and maintain compatibility with the project requirements.


2. **Virtual Environment**:
   - Create a virtual environment to isolate project dependencies.
   - Use `pipenv` for managing the virtual environment and dependencies.

### Django Setup

1. **Install Django**: Leverage Django's capabilities for web development by installing it within the virtual environment.
2. **Dependencies**: Install necessary dependencies, such as `whitenoise` for static file management and `tastypie` for REST API functionality, as per the project's `Pipfile`.

### Project Configuration

**Database Setup**: Use Django's ORM to define models and execute migrations, setting up SQLite as the project database.

1. **Download the Database File**: Download the `db.sqlite3` file from the provided web address.
 `https://sqlitebrowser.org/dl/`

3. **Running Migrations**: To make sure your database schema is up to date, run:

`python manage.py makemigrations`
`python manage.py migrate`

4. **Admin and User Interface**: Configure the Django admin for content management and customize the front page for a user-friendly browsing experience.

## Development Workflow

### Environment Preparation

- Install `pipenv` to handle virtual environments and dependencies.
- macOS/Linux: `pip3 install --user pipenv`
- Windows: `pip install --user pipenv`
- Ensure `pipenv` is added to the system `PATH`.

### Project Setup

- Navigate to the project directory and run `pipenv install` to set up the virtual environment and install dependencies.
- Activate the virtual environment with `pipenv shell`.
- Install Django and other required libraries as specified in the `Pipfile`.

### Running the Project

- Start the Django development server with `python manage.py runserver`.
- Access the project at `http://127.0.0.1:8000/`.

## API and Admin Interface

### API Endpoints

- **Movies and Props**: Accessible at `/api/movies/` and `/api/props/` for retrieving information in JSON format.

### Django Admin

- **Superuser Creation**: Essential for managing content through the Django admin interface.
- **Content Management**: Administer movies, props, genres, and availability directly through the web interface.

## Security and Maintenance

### Secret Key Management

- **Importance**: The `SECRET_KEY` is crucial for maintaining the security of Django projects.
- **Generation**: Use Django's `get_random_secret_key()` or a custom Python script to generate a secure secret key.

### Generating a New Secret Key

#### Method 1: Using Django's `get_random_secret_key()`

1. Open a terminal or command prompt.
2. Activate your project's virtual environment.
3. Enter the Django shell by running:
    ```
    python manage.py shell
    ```
4. In the Django shell, generate a new secret key:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
5. Copy the generated key.
6. Replace the `SECRET_KEY` in `settings.py` with the new key:
    ```python
    SECRET_KEY = 'newly_generated_secret_key_here'
    ```

#### Method 2: Using Python Directly

1. Open a terminal or command prompt.
2. Run Python by typing `python` and hitting Enter.
3. Generate a secret key:
    ```python
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    print(get_random_string(50, chars))
    ```
4. Copy the generated key and replace the `SECRET_KEY` in your `settings.py`:
    ```python
    SECRET_KEY = 'paste_your_generated_key_here'
    ```


### Admin Security

- Create a superuser with `python manage.py createsuperuser`.
- Always access the admin interface securely, especially in production environments.

## Conclusion

Vidly exemplifies the application of Django and Python in web development, offering a practical learning experience in building and managing a web application. From setup to deployment, the project provides insights into modern web development practices, database management, and application security, making it a valuable resource for students and aspiring developers.
