#Standard library imports
import argparse

#Local imports
from auth.oauth import authenticate
from config import (
    FETCH_LABEL, MAX_RESULTS, RULES_FILE, 
    SCOPES, TOKENFILE
)
from db.models import Base, engine
from client.v1.fetch import fetch_emails
from client.v1.process import process_emails

def main():

    if not engine.dialect.has_table(engine, 'message'):
        Base.metadata.create_all(engine)
    creds = authenticate(TOKENFILE, SCOPES)
    fetch_label = FETCH_LABEL
    max_results = MAX_RESULTS
    rules_file = RULES_FILE

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--fetch-label',
        help='Fetch email fiter(s), defaults to config.FETCH_LABEL',
        nargs='+', type=str
    )
    parser.add_argument(
        '--rules-file',
        help='Path to Json rules file, defaults to config.RULES_FILE'
    )
    parser.add_argument(
        '--max-results',
        help='Number of number of emails to fetch, defaults to config.MAX_RESULTS',
        type=int
    )
    args = parser.parse_args()
    if args.fetch_label:
        fetch_label = args.fetch_label
    if args.max_results:
        max_results = args.max_results
    if args.rules_file:
        rules_file = args.rules_file
    
    fetch_label = [label.upper() for label in fetch_label]
    
    fetch_emails(creds, max_results, fetch_label)
    process_emails(creds, rules_file)

if __name__ == '__main__':
    main()
