#Third party imports
from dateutil import parser
from googleapiclient.discovery import build

#Local imports
from db.models import Message, Session

def fetch_emails(creds, max_results, fetch_label):
    """
    Fetches a list of emails from the
    authenticated user's mail
    ----------------------------------

    arguments:
        - creds: oauth token object
        - fetch_label: label for filtered fetch 
    """
    service = build('gmail', 'v1', credentials=creds)   
    result = service.users().messages().list(
        userId='me', labelIds=fetch_label, 
        maxResults=max_results
    ).execute()

    message_ids = result.get('messages', [])
    if not message_ids:
        print(f'No new {fetch_label} messages!')
    else:
        print(f'{len(message_ids)} {fetch_label} messages were fetched!')
        s = Session()
        count = 0
        for message_id in message_ids:
            result = service.users().messages().get(
                userId='me', id=message_id['id'],
                format='metadata'
            ).execute()
            headers = result['payload']['headers']
            record = {
                'message_id': result['id'],
                'labels': result['labelIds']
            }
            for header in headers:
                if header['name'] == 'From':
                    record['sender'] = header['value']
                elif header['name'] == 'To':
                    record['recipient'] = header['value']
                elif header['name'] == 'Subject':
                    record['subject'] = header['value']
                elif header['name'] == 'Date':
                    record['date'] = parser.parse(header['value']).date()

            message = Message(**record)
            q = s.query(Message).filter_by(message_id=message.message_id)
            if not s.query(q.exists()).scalar():
                s.add(message)
                count += 1
        s.commit()
        s.close()
        print(f'{count} new {fetch_label} messages were added!')