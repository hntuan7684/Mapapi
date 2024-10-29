# Installation Guide

This section provides instructions on how to install and set up the Mapapi project using Docker.

## Prerequisites

-   Docker
-   Docker Compose

## Installation Steps

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/223MapAction/Mapapi.git
    ```

2. **Navigate to the Project Directory**: Move into the project directory:

    ```bash
    cd Mapapi
    ```

3. **Build and Run the Containers**: Use Docker Compose to build and run the services:

    ```bash
    docker-compose -f _cd_pipeline.yml up --build
    ```

    This command will build the Docker images and start the containers for the application, including the database, API server, Redis, and other services.

4. **Access the Application**: Once the containers are up and running, you can access the application at `http://localhost`.

5. **Stopping the Services**: To stop the running services, use:

    ```bash
    docker-compose -f _cd_pipeline.yml down
    ```

This setup leverages Docker to manage dependencies and services, ensuring a consistent environment across different systems.
