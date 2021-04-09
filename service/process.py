#Standard library imports
import json
import pdb

#Third party imports
from googleapiclient.discovery import build
from sqlalchemy.orm import Query

#Local imports
from db.models import Message, Session
from service.filters import (
    date_field_filter, from_field_filter, 
    subject_field_filter
)

def process_emails(creds, rules_file):
    """
    Fetches emails from the database and performs
    actions, all based on set of rules in JSON format
    --------------------------------------------------

    arguments:
        - creds: oauth token object
        - rules_file: Json file path containing rules
    """
    service = build('gmail', 'v1', credentials=creds)
    with open(rules_file, 'r') as rf:
        rules = json.load(rf)
    
    session = Session()
    query_objects = []

    for rule in rules['rules']:
        if rule['field'].upper() == 'FROM':
            q = from_field_filter(session, rule)
            query_objects.append(q)
        elif rule['field'].upper() == 'SUBJECT':
            q = subject_field_filter(session, rule)
            query_objects.append(q)
        elif rule['field'].upper() == 'DATE':
            q = date_field_filter(session, rule)
            query_objects.append(q)

    if rules['globalPredicate'].upper() == 'ALL':
        messages = Query.intersect(*query_objects).all()
    elif rules['globalPredicate'].upper() == 'ANY':
        messages = Query.union(*query_objects).all()

    add_labels = []
    remove_labels = []

    for action in rules['actions']:
        if action['action'].upper() == 'MOVE':
           add_labels.append(action['value'].upper())
        elif (action['action'].upper() == 'MARK' and 
                action['value'].upper() == 'UNREAD'):
            add_labels.append(action['value'].upper())
        elif (action['action'].upper() == 'MARK' and
                action['value'].upper() == 'READ'):
            remove_labels.append('UNREAD')

    for message in messages:
        result = service.users().messages().modify(
            userId='me', id=message.message_id,
            body={
                'addLabelIds': add_labels,
                'removeLabelIds': remove_labels
            }
        ).execute()        
        message.labels = result['labelIds']
    session.commit() 
    session.close()
    print(f'Actions performed on {len(messages)} matching messages')
