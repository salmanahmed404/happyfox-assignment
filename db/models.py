#Third party imports
from sqlalchemy import create_engine
from sqlalchemy import ARRAY, Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Local imports
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Message(Base):
    """
    Represents a single email message
    """
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    message_id = Column(String)
    sender = Column(String)
    recipient = Column(String)
    subject = Column(String)
    date = Column(Date)
    labels = Column(ARRAY(String))
