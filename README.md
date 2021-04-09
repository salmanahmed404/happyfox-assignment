# happyfox-assignment

## Description

A set of python scripts that integrate with GMail API and perform some rule based operation on emails

## Libraries Used

1. SQLAlchemy: for database related operations
2. google-python-api-client: for integrating with GMail API
3. google-auth-oauthlib: for authentication
4. google-auth-httplib2: for authentication
5. python-dateutil: for date related operations

* Database Used: Postgres

## Setup

1. Clone the repository
2. [Create a Google Cloud Platform project with the GMail API enabled](https://developers.google.com/workspace/guides/create-project)
3. [Create authorization credentials for a desktop application i.e. oauth client IDs](https://developers.google.com/workspace/guides/create-credentials). Save the generated secret file as *client_credentials.json* inside the root of the repository directory.
4. Database setup
    * Create a postgres database named *maildb*
    * Export postgres user and password
        ```
        export POSTGRES_USER=<your postgres username under which the db has been created>
        export POSTGRES_PASSWORD=<your postgres password>
        ```
5. Running
    * ``` python main.py --help ``` to get a list of optional arguments
    * ``` python main.py ``` to run the script