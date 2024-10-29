# Usage Guide

This section provides information on how to use the Mapapi project, including details on API endpoints and features.

## API Endpoints

Mapapi provides a set of RESTful API endpoints for managing and retrieving data on environment-related incidents. Below are some of the key endpoints:

-   **GET /api/incidents/**: Retrieve a list of all incidents.
-   **POST /api/incidents/**: Create a new incident.
-   **GET /api/incidents/{id}/**: Retrieve details of a specific incident by ID.
-   **PUT /api/incidents/{id}/**: Update an existing incident by ID.
-   **DELETE /api/incidents/{id}/**: Delete an incident by ID.

## Features

-   **Incident Management**: Create, update, and delete incidents related to environmental issues.
-   **Data Retrieval**: Access detailed information about incidents, including location, description, and status.
-   **Asynchronous Processing**: Utilize Celery and Redis for handling background tasks efficiently.

## Running the Application

Once the server is running, you can access the API at `http://127.0.0.1:8000/api/`. Use tools like Postman or curl to interact with the API endpoints.

For more detailed information on each endpoint, refer to the API documentation or the source code.
