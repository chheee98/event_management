# Event Management System

## Requirements

### 1. User Authentication

- Implement user registration and login functionality.
- Differentiate between regular users and event organizers.

### 2. Event Management

- Allow event organizers to create, update, and delete events.
- Each event should have the following attributes: title, description, date and time, location, and capacity.

### 3. Event Registration

- Allow regular users to register for events.
- Prevent users from registering for an event that has reached its capacity.

### 4. Event Listing

- Provide a page where users can view all upcoming events.
- Provide an event detail page that includes information on which users have registered.
- Include a search feature to filter events by title, date, or location.

## Technical Requirements

- Python 3.8+
- Django 5.0.7

## Setup

1. **Clone the repository**

   - git clone https://github.com/chheee98/event_management.git
   - cd event_management

2. **Create and activate a virtual environment**

   - python3 -m venv .venv
   - source .venv/bin/activate

3. **Install dependencies**

   - pip install -r requirements.txt

4. **Apply migrations**

   - python manage.py migrate

5. **Create a superuser**

   - python manage.py createsuperuser

6. **Run the development server**
   - python manage.py runserver

## Testing

To test API endpoints, please use the provided postman_collection

postman_collection: storages/django_event_mgmt.postman_collection.json
