# Django CRM Application

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [API Endpoints](#api-endpoints)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

Welcome to the Django CRM Application! This project is designed to manage customer relationships, providing functionalities such as customer registration, authentication, viewing customer records, and CSV file operations. This project showcases my backend development skills using Django, demonstrating proficiency in creating robust and scalable web applications.

## Features

- User Registration and Authentication
- Add, View, and Manage Customers
- Import and Export Customer Data via CSV
- User-friendly Interface with Authentication Protected Routes

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.8+
- Django 3.2+
- Git

## Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/joelezz/Django-CRM.git
   cd Django-CRM
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000` to see the application in action.

## Configuration

### Environment Variables

Create a `.env` file in the root directory of the project to store environment variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Ensure you replace `your_secret_key` with a secret key for your Django application.

## Usage

### User Registration and Login

1. **Register:**

   Navigate to `http://127.0.0.1:8000/register` to create a new user account.

2. **Login:**

   Navigate to `http://127.0.0.1:8000/my-login` to log in with your credentials.

### Managing Customers

1. **View Customers:**

   Navigate to `http://127.0.0.1:8000/customers` to view a list of all customers.

2. **Add Customer:**

   Navigate to `http://127.0.0.1:8000/add_customer` to add a new customer.

3. **View Customer Record:**

   Click on a customer ID in the list to view the customer's detailed record.

### Import and Export CSV

1. **Import Customers:**

   Navigate to `http://127.0.0.1:8000/upload_csv` to upload a CSV file containing customer data.

2. **Export Customers:**

   Navigate to `http://127.0.0.1:8000/export_customers_csv` to download a CSV file with all customer data.

## Project Structure

```plaintext
Django-CRM/
├── crm/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── myapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   ├── customers.html
│   ├── add_customer.html
│   ├── record.html
├── static/
│   ├── css/
│   ├── js/
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
```

## API Endpoints

- **User Registration:** `POST /register`
- **User Login:** `POST /my-login`
- **View Customers:** `GET /customers`
- **Add Customer:** `POST /add_customer`
- **View Customer Record:** `GET /record/<int:id>`
- **Upload CSV:** `POST /upload_csv`
- **Export CSV:** `GET /export_customers_csv`

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. **Fork the Project**
2. **Create your Feature Branch (`git checkout -b feature/AmazingFeature`)**
3. **Commit your Changes (`git commit -m 'Add some AmazingFeature'`)**
4. **Push to the Branch (`git push origin feature/AmazingFeature`)**
5. **Open a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
