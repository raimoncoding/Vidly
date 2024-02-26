# Vidly
Vidly, a Django-based student project with Python 3.10, offers a platform for browsing and renting movies and props. It features an admin page for content management and a customer-friendly front page for easy navigation. Uses SQLite for efficient data management.

# Vidly Project

## Overview

Vidly is a student project developed using Django with Python 3.10, aimed at providing a comprehensive platform for movie and prop rental services. This application features a robust admin page for administrators to manage content and a user-friendly front page for customers to browse movies, props, genres, and check availability. The project utilizes SQLite as its database, offering a lightweight, yet efficient solution for data management.

## Setup Process

### Environment Setup

- **Python 3.10 Installation**: The project is built on Python 3.10 to leverage the latest language features and ensure compatibility.
- **Virtual Environment**: A virtual environment was created to manage project dependencies separately from the system-wide Python installation, maintaining a clean development space.

### Django and Dependencies

- **Django Framework**: Utilizing the Django framework for its robust web development capabilities, Vidly benefits from Django's scalability and extensive library support.
- **Dependency Management**: Critical dependencies, such as `whitenoise` for static file handling and `tastypie` for RESTful API integration, were installed and configured to enhance the application's functionality.

### Configuration and Development

- **Project Configuration**: Initial setup using Django's `startproject` and `startapp` commands laid the groundwork for the application's development.
- **Database Migrations**: Leveraging Django's ORM and migration system, database models were defined and managed effectively to support the application's data structure. SQLite was chosen for its simplicity and ease of integration with Django.

## Project Setup

This section guides you through setting up your development environment for the Vidly project. It covers installing `pipenv`, setting up a virtual environment, activating it, and installing Django along with other necessary libraries.

### Installing `pipenv`

First, you need to install `pipenv`, a tool that creates and manages virtual environments and handles project dependencies.

- **macOS and Linux**:
    ```
    pip3 install --user pipenv
    ```
- **Windows**:
    ```
    pip install --user pipenv
    ```

Ensure that the path to the user base's binary directory is on your `PATH` environment variable. You might need to add `export PATH="$PATH:$(python -m site --user-base)/bin"` to your `.bashrc` or `.bash_profile` for macOS/Linux, or adjust the PATH variable in the System Environment Variables on Windows.

### Setting Up the Virtual Environment

Navigate to the project's root directory and run:
```
pipenv install
```

This command creates a virtual environment for the project and installs the dependencies defined in the `Pipfile`.

### Activating the Virtual Environment

To activate the virtual environment, use:
```
pipenv shell
```

This command spawns a shell within the virtual environment. Any Python or pip commands will now use the versions in the virtual environment instead of the global ones.

### Installing Django and Required Libraries

With the virtual environment active, you can install Django and any other necessary libraries. While specific library versions may vary, you can generally install Django with:
```
pipenv install django
```


To install other required libraries, including `whitenoise` for static file management, refer to the `Pipfile` in the project's root directory for a list of dependencies. For example, to install `whitenoise`:
```
pipenv install whitenoise
```


Repeat this process for any other libraries listed in the `Pipfile`.

### Starting the Project

After installing Django and other dependencies, you can start the Django development server with:
```
python manage.py runserver
```


Visit `http://127.0.0.1:8000/` in your web browser to view the project.

## API Endpoints

The project provides RESTful API endpoints for accessing movies and props data. These endpoints can be used to retrieve JSON-formatted information about the movies and props available in the application.

### Movies API

To see a list of movies, visit the following URL:
- http://127.0.0.1:8000/api/movies/

### Props API

To see a list of props, visit the following URL:
- http://127.0.0.1:8000/api/props/

These endpoints are designed for easy integration with frontend applications or for use by third-party services.

Please note: The URLs provided are for accessing the API in a local development environment. Replace `127.0.0.1:8000` with the actual domain or IP address where your project is hosted in a production environment.


### Admin Webpage

The Django Admin interface is a powerful built-in tool that allows administrators to manage the content of the website. Before accessing the admin interface, a superuser account must be created, and specific password validations can be enforced for added security.

- **User Authentication**: The admin interface is protected by secure authentication mechanisms. To access the management dashboard, users must log in with a superuser account. This account has full access to create, read, update, and delete operations within the admin interface.


- **Password Requirements**: For added security, Django allows you to enforce password validation rules for user accounts, including superuser accounts. These rules can be defined in your project's `settings.py` file using the `AUTH_PASSWORD_VALIDATORS` setting. An example configuration might look like this:

### Generating a Secret Key

The `SECRET_KEY` in Django is vital for security. Follow these steps to generate and set a new secret key:

1. Open a terminal and run Python interactive shell:
    ```bash
    python
    ```

2. Use the following commands to generate a new secret key:
    ```python
    import secrets
    print(secrets.token_urlsafe())
    ```

3. Copy the generated key and replace the `SECRET_KEY` in your `settings.py`:
    ```python
    SECRET_KEY = 'paste_your_generated_key_here'
    ```

Ensure this key is kept confidential to maintain your application's security.

### Admin Access

To manage your application's data through the Django admin, create a superuser account:

```bash
python manage.py createsuperuser
Follow the prompts to set up the superuser credentials. Access the admin interface at http://127.0.0.1:8000/admin/ using these credentials.

Remember to set DEBUG to False in production settings and use strong, unique passwords for all administrator accounts.


- **Content Management**: Within the admin interface, administrators can effortlessly manage the content of movies, props, genres, and their availability. The intuitive interface supports operations such as adding new entries, editing existing ones, and deleting entries that are no longer needed.

Remember, accessing the admin interface in a production environment should always be done over a secure connection (HTTPS) to protect sensitive information.


### Customer Front Page

- **Movie and Prop Catalog**: Customers can explore a detailed catalog of movies and props, complete with descriptions, images, genres, and availability information.
- **Search and Filtering**: Advanced search and filtering capabilities enable customers to easily find content that matches their interests.

## Generating a Django Secret Key

The `SECRET_KEY` in a Django project plays a crucial role in security and cryptography. It's used to provide cryptographic signing, and its value is used to salt hashes for various security mechanisms, including CSRF tokens and session IDs. Therefore, it's vital to keep this key secret and unique per project, especially in production environments.

### Why the SECRET_KEY is Important

- **Cryptography**: The `SECRET_KEY` is used throughout Django's security features, such as signing session cookies, CSRF tokens, and passwords.
- **Security**: A unique and unpredictable `SECRET_KEY` makes various attacks, such as guessing session cookies or CSRF tokens, much harder.

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
4. Copy the generated key.
5. Update `settings.py` with the new `SECRET_KEY`.

### Important Notes

- Never expose your `SECRET_KEY` in public repositories or to unauthorized users.
- For production, consider setting the `SECRET_KEY` through an environment variable to avoid including it directly in your source code.


## Conclusion

As a student project, Vidly serves as a practical demonstration of applying modern web development techniques in a real-world application. This project showcases the potential of Django and Python in creating feature-rich web applications, while also serving as an invaluable learning tool for web development students. The choice of SQLite for database management underscores the project's commitment to simplicity and efficiency, making it an ideal learning platform for those new to web development.

