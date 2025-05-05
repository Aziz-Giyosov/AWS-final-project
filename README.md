# Travel Destinations Web Application

A web application built with Flask to display and manage travel destinations, connected to a PostgreSQL database.

## Table of Contents

-   [Description](#description)
-   [Setup](#setup)
-   [Usage](#usage)
-   [Database Setup](#database-setup)
-   [API Endpoints](#api-endpoints)
-   [Contributing](#contributing)
-   [License](#license)

## Description

This web application provides a simple interface for viewing and managing travel destinations. It uses the Flask framework (Python) to create a web server, interacts with a PostgreSQL database to store destination data, and includes a basic HTML front-end.  Key features include:

* Displaying a list of destinations from the database.
* Adding new destinations to the database via a form.
* Deleting destinations from the database.

## Setup

### Prerequisites

* Python 3.x
* pip (Python package installer)
* PostgreSQL database
* Git (for cloning the repository)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
    cd your_repository_name
    ```

    (Replace `your_username` and `your_repository_name` with your actual GitHub information.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    * On Windows:

        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (The `requirements.txt` file should contain the following):

    ```
    Flask
    psycopg2-binary
    Flask-CORS
    ```

5.  **Database Configuration:**

    * Ensure your PostgreSQL database is running.
    * You will need to have a database named `postgres` (or change the `DB_NAME` variable in `app.py`).
    * You will need to have a user named `postgres` (or change the `DB_USER` variable in `app.py`).
    * Set the correct password for your `postgres` user in the `app.py` file.  **Important:** Do not hardcode passwords in a production environment.  Use environment variables or a configuration file.

6.  **Load the initial data:**
    * The `travel_destinations.csv` file contains the initial data.  The table should be created, and the data loaded using the `psql` commands as described in the "Database Setup" section.

7.  **Run the application:**

    ```bash
    python app.py
    ```

    The application will start running at `http://127.0.0.1:5000/`.

## Usage

1.  **Open the web application:**
    * Open your web browser and go to the address where the Flask application is running (e.g., `http://127.0.0.1:5000/`).

2.  **View Destinations:**
    * The main page (`index.html`) displays a list of destinations retrieved from the PostgreSQL database.

3.  **Add a Destination:**
    * The page contains a form to add a new destination.
    * Enter the destination details (Destination, Country, Category, Best Time to Travel) and click "Add Destination".
    * The new destination will be added to the database and displayed on the page.

4.  **Delete a Destination**
    * The page contains a form to delete a destination.
    * Enter the name of the destination you want to delete and click "Delete Destination".
    * The destination will be removed from the database and will no longer be displayed.

## Database Setup

This application uses a PostgreSQL database.  Here's how to set up the database and load the initial data:

1.  **Connect to PostgreSQL:**

    ```bash
    psql -h your_host -d your_database -U your_user
    ```

    (Replace `your_host`, `your_database`, and `your_user` with your actual PostgreSQL connection details. If you're running PostgreSQL locally with the default settings, you can often just use `psql`.)

2.  **Create the table:**

    ```sql
    CREATE TABLE travel_destinations (
        city VARCHAR(255),
        country VARCHAR(255),
        category VARCHAR(255),
        best_time_to_travel VARCHAR(255)
    );
    ```

3.  **Load the data from the CSV file:**

    ```sql
    \copy travel_destinations FROM 'travel_destinations.csv' WITH (FORMAT CSV, HEADER);
    ```
    * Ensure that the `travel_destinations.csv` file is in the same directory where you are running the `psql` command, or provide the correct path to the file.

4.  **Verify the data:**

    ```sql
    SELECT * FROM travel_destinations;
    ```
    This should display the data from the `travel_destinations` table.

5.  **Exit psql:**

    ```sql
    \q
    ```

## API Endpoints

The application exposes the following API endpoints:

* `GET /destinations`: Retrieves a list of all destinations from the database and returns them as a JSON array.  Each destination object in the array has the following keys:  `destination` (city), `country`, `category`, and `best_time_to_travel`.
* `POST /destinations`: Adds a new destination to the database.  Expects a JSON payload with the following keys: `city`, `country`, `category`, and `best_time_to_travel`.
* `DELETE /destinations/<destination_name>`: Deletes the destination with the specified city from the database.  The `destination_name` is passed as part of the URL.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).  (You should add a LICENSE file to your repository.)
