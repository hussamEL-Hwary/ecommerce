# E-Commerce Backend

This project implements a robust backend solution for an e-commerce system using Django and Django REST Framework (DRF). 
It includes API endpoints for managing products, sales, and purchases, with OAuth2 authentication, 
inventory management, and notifications for low stock levels using Celery.

## Table of Contents

- [Objective](#objective)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Scheduled Tasks](#scheduled-tasks)
- [Testing](#testing)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

## Objective

The goal of this project is to design and implement a backend solution for managing product sales and purchases, including features like:
- CRUD operations for products.
- Sales and purchase orders management.
- Inventory updates after sales and purchases.
- OAuth2 authentication for securing the API.
- Notifications for low stock levels.

## Features

- **Product Management**: Create, read, update, and delete products with unique SKUs.
- **Sales Orders**: API endpoints for creating sales orders that update inventory.
- **Purchase Orders**: API endpoints for creating purchase orders to restock inventory.
- **Inventory Management**: Automated inventory updates on sales and purchases.
- **Low Stock Notifications**: Scheduled task to notify when stock levels are below a threshold.
- **OAuth2 Authentication**: Secure API endpoints using OAuth2.
- **API Documentation**: Swagger UI for exploring API endpoints.

## Technology Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: Django OAuth Toolkit (OAuth2)
- **Database**: PostgreSQL
- **Task Queue**: Celery with Redis
- **Deployment**: Docker, Docker Compose
- **API Documentation**: Swagger (drf-yasg)

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.9 or higher if running locally without Docker.

### Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
```

### Environment Variables
Create a `.env` file in the root directory with the following environment variables:

```
DEBUG=False
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=postgres
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
OAUTH2_CLIENT_ID=your_client_id
OAUTH2_CLIENT_SECRET=your_client_secret
```

### Database Setup
Ensure the PostgreSQL database is set up and ready. 
1. Run Migrations:
``` bash
python manage.py migrate
```

2. Create Superuser:
``` bash
python manage.py createsuperuser
```

### Running the Application

1. Start Services:
```bash
python manage.py runserver
```

2. Access the Application:
* Admin: http://localhost:8000/admin/
* Swagger API Docs: http://localhost:8000/api/docs/swagger/

### API Documentation
API documentation is available via Swagger UI:

Visit http://localhost:8000/api/docs/swagger/ to explore the available endpoints.


### Authentication
The project uses OAuth2 for authentication. Set up the OAuth2 application in the Django admin under OAuth2 Applications.

1. Create an OAuth2 Application:

http://localhost:8000/o/applications/
Click on the link to create a new application and fill the form with the following data:
```bash
Name: just a name of your choice
Client Type: confidential
Authorization Grant Type: Resource owner password-based
```

2. Obtain Access Token:

Use the /o/token/ endpoint to obtain an access token by providing the client ID, client secret, username, and password./n
Open your shell:
```shell
curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
```

Visit [the documentation](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html) for more details


### Scheduled Tasks
The application uses Celery with Redis to handle background tasks.

Start Celery:
```bash
celery -A ecommerce worker -B --scheduler django -l info
```

A Celery task is scheduled to run daily at 10 AM to check for low stock levels and create notifications.



### Deployment
For production deployment:

``` TODO: Building a complete CI/CD pipleline```

1. SSH to EC2 machine
2. pull the code from GitHub
3. Ensure all environment variables are correctly set for the production environment.
4. Build Docker Image ```docker build -f docker/django/Dockerfile -t web .```
5. Up the docker compose ```docker compose -f deployment/docker-compose.backend.yml up -d```
