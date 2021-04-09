from os import environ, path

#Oauth configurations
SCOPES = ['https://mail.google.com/']
TOKENFILE = 'token.json'

#General configurations
MAX_RESULTS = 5
FETCH_LABEL = 'INBOX'
DIR_NAME = path.dirname(path.realpath(__file__))
RULES_FILE = path.join(DIR_NAME, 'rules/rule1.json')

#Postgres Configurations
POSTGRES_USER = environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD', 'postgres')

#SQLAlchemy configurations
DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/maildb'