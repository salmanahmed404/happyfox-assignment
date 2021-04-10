#Standard library imports
from datetime import date

#Third party imports
from dateutil.relativedelta import relativedelta
from sqlalchemy import not_

#Local imports
from db.models import Message

def from_field_filter(s, rule):
    """
    Filters messages based on predicate
    specified on 'from' field
    -----------------------------------

    arguments:
        - s: sqlalchemy session object
        - rule: rule dictionary for this field
    """
    if rule['predicate'].upper() == 'EQUAL':
        q = s.query(Message).filter(
            Message.sender==rule['value']
        )
    elif rule['predicate'].upper() == 'CONTAINS':
        q = s.query(Message).filter(
            Message.sender.contains(rule['value'])
        )
    elif rule['predicate'].upper() == 'NOT EQUAL':
        q = s.query(Message).filter(
            Message.sender!=rule['value']
        )
    elif rule['predicate'].upper() == 'DOES NOT CONTAIN':
        q = s.query(Message).filter(
            not_(Message.sender.contains(rule['value']))
        )    
    return q

def subject_field_filter(s, rule):
    """
    Filters messages based on predicate
    specified on 'subject' field
    ------------------------------------

    arguments:
        - s: sqlalchemy session object
        - rule: rule dictionary for this field    
    """
    if rule['predicate'].upper() == 'EQUAL':
        q = s.query(Message).filter(
            Message.subject==rule['value']
        )
    elif rule['predicate'].upper() == 'CONTAINS':
        q = s.query(Message).filter(
            Message.subject.contains(rule['value'])
        )
    elif rule['predicate'].upper() == 'NOT EQUAL':
        q = s.query(Message).filter(
            Message.subject!=rule['value']
        )
    elif rule['predicate'].upper() == 'DOES NOT CONTAIN':
        q = s.query(Message).filter(
            not_(Message.subject.contains(rule['value']))
        )    
    return q

def date_field_filter(s, rule):
    """
    Filter messages based on predicate 
    specified on 'date' field
    -----------------------------------

    arguments:
        - s: sqlalchemy session object
        - rule: rule dictionary for this field    
    """
    if rule['predicate'].upper() == 'LESS THAN DAYS':
        end_date = date.today()
        start_date = end_date - relativedelta(days=rule['value'])
        q = s.query(Message).filter(
            Message.date.between(start_date, end_date)
        )
    elif rule['predicate'].upper() == 'GREATER THAN DAYS':
        filter_date = date.today() - relativedelta(days=rule['value'])
        q = s.query(Message).filter(
            Message.date <= filter_date
        )
    elif rule['predicate'].upper() == 'LESS THAN MONTHS':
        end_date = date.today()
        start_date = end_date - relativedelta(months=rule['value'])
        q = s.query(Message).filter(
            Message.date.between(start_date, end_date)
        )
    elif rule['predicate'].upper() == 'GREATER THAN MONTHS':
        filter_date = date.today() - relativedelta(days=rule['value'])
        q = s.query(Message).filter(
            Message.date <= filter_date
        )
    return q