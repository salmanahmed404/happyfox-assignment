# happyfox-assignment

## Description

A set of python scripts that integrate with GMail API and perform some rule based operation on emails

* Python: Python 3.6
* Database Used: Postgres

## Libraries Used

1. SQLAlchemy: for database related operations
2. google-python-api-client: for integrating with GMail API
3. google-auth-oauthlib: for authentication
4. google-auth-httplib2: for authentication
5. python-dateutil: for date related operations

## Setup

1. Clone the repository

2. [Create a Google Cloud Platform project with the GMail API enabled](https://developers.google.com/workspace/guides/create-project)

3. [Create authorization credentials for a desktop application i.e. oauth client IDs](https://developers.google.com/workspace/guides/create-credentials). Save the generated secret file as *client_credentials.json* inside the root of the repository directory.

4. Install dependencies
    ```
    pip install -r requirements.txt
    ```

5. Database setup
    * Create a postgres database named *maildb*
    * Export postgres user and password
        ```
        export POSTGRES_USER = <your postgres username under which the db has been created>
        export POSTGRES_PASSWORD = <your postgres password>
        ```
    * Ensure the database server is running on port 5432

6. Running
    * ``` python main.py --help ``` to get a list of optional arguments
    * ``` python main.py ``` to run the program
    
**Note** The first time the program is run, complete the oauth flow according 
to the prompts. For subsequent runs, the token is fetched from the file *token.json*
generated during the first run.