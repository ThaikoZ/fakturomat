# Invoicing Application

The Invoicing Application allows for easy handling of invoices through the Django admin panel. It is a tool designed for managing clients, products, and issuing invoices.

## Description

The application is built with Django, providing a convenient way to manage data in the admin panel. The backend handles business logic, such as generating and managing invoices, clients, and products.

## Features

### 1. Invoice Management

- **Issuing Invoices**: Ability to create new invoices through the Django admin panel.
- **Deleting Invoices**: Ability to delete existing invoices directly from the panel.
- **Downloading Invoices**: Option to download invoices in PDF format.

### 2. Client Management

- **Adding Clients**: Ability to add new clients to the database via the admin panel.
- **Editing Client Data**: Ability to update existing client data.
- **Deleting Clients**: Option to remove clients from the database.

### 3. Product Management

- **Adding Products**: Ability to add new products to the database via the admin panel.
- **Editing Product Data**: Ability to update existing product data.
- **Deleting Products**: Option to remove products from the database.

### 4. Templates Management
Templates allow to issue an invoice directly from templates panel.

- **Adding Templates**: Ability to add new templates to the database via the admin panel.
- **Editing Templates Data**: Ability to update existing product data.
- **Deleting Templates**: Option to remove products from the database.

## Installation and Running

### Requirements

- Python 3.x
- Django

### Instructions

1. **Download the repository**:

   ```bash
   git clone https://github.com/ThaikoZ/fakturomat
   cd fakturomat
   ```

2. **Install dependencies**:

   ```bash
   pip install pipenv
   pipenv install
   ```

3. **Run the Django server**:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser  
   python manage.py runserver
   ```

4. **Access the admin panel**:

   - Log in to the Django admin panel available at `http://localhost:8000/admin/`.

## Notes

- Ensure the Django server is running to have full access to invoicing management features.
- This project was created as part of a Software Engineering course requirement.
- Add authentication and login if you need additional security for accessing invoicing functions.
