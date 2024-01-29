# 🎸 Band Web - Django Web Application

## Overview

Welcome to **Band Web**, a Django-based web application designed to showcase information about music bands and their albums. This project is an accomplishment that highlights proficiency in web development, incorporating Django, Python, HTML, CSS, and database management.

## Brief Description

**Band Web** is a Django-based web application that serves as a platform for showcasing information about music bands and their albums. With features such as a robust band model, user authentication, and a user-friendly interface, the project demonstrates proficiency in  web development. The application utilizes Django, Python, HTML, and CSS, providing a seamless user experience for exploring and managing music-related data.

## Features

- **Band Model:** Represents music bands with attributes such as name, genre, and description.
- **Album Model:** Represents music albums with attributes including title, release date, and a foreign key reference to the Band model.
- **User Authentication:** Allows users to register, log in, and view personalized information. Utilizes Django's built-in authentication forms and custom user creation forms.
- **Class-Based Views:** Utilizes Django's class-based views for dynamic and efficient presentation of band lists and detailed band information.
- **Database Management:** Configured with SQLite to ensure efficient data storage and retrieval.
- **Web Security:** Adheres to Django's best practices for web security, including password validation.
- **User-Friendly Templates:** HTML templates created with Django's template engine for a visually appealing and user-friendly interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tshamala-pathy/band_web.git
    ```

2. Navigate to the project directory:

    ```bash
    cd band_web
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Create a superuser for accessing the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

2. Follow the prompts to set up a superuser account.

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

4. Access the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials.

5. Use the admin panel to manage bands and albums.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
