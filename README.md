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

pipenv install

This command creates a virtual environment for the project and installs the dependencies defined in the `Pipfile`.

### Activating the Virtual Environment

To activate the virtual environment, use:

pipenv shell

This command spawns a shell within the virtual environment. Any Python or pip commands will now use the versions in the virtual environment instead of the global ones.

### Installing Django and Required Libraries

With the virtual environment active, you can install Django and any other necessary libraries. While specific library versions may vary, you can generally install Django with:

pipenv install django

To install other required libraries, including `whitenoise` for static file management, refer to the `Pipfile` in the project's root directory for a list of dependencies. For example, to install `whitenoise`:

pipenv install whitenoise

Repeat this process for any other libraries listed in the `Pipfile`.

### Starting the Project

After installing Django and other dependencies, you can start the Django development server with:

python manage.py runserver

Visit `http://127.0.0.1:8000/` in your web browser to view the project.

### Admin Webpage

- **User Authentication**: Secure authentication mechanisms allow administrators to log in and access the management dashboard.
- **Content Management**: The admin page provides comprehensive tools for managing movies, props, genres, and availability, all through an intuitive interface.

### Customer Front Page

- **Movie and Prop Catalog**: Customers can explore a detailed catalog of movies and props, complete with descriptions, images, genres, and availability information.
- **Search and Filtering**: Advanced search and filtering capabilities enable customers to easily find content that matches their interests.

## Conclusion

As a student project, Vidly serves as a practical demonstration of applying modern web development techniques in a real-world application. This project showcases the potential of Django and Python in creating feature-rich web applications, while also serving as an invaluable learning tool for web development students. The choice of SQLite for database management underscores the project's commitment to simplicity and efficiency, making it an ideal learning platform for those new to web development.

