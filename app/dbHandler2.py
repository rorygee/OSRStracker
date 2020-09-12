# Imports

import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import requestsHandler


# Database Handler (SQLAlchemy/MySQL)

# Establish a 'global' connection, need to modify to use a mysql driver
engine = create_engine('sqlite:///:memory:', echo=True)

# Define a single instance to store references to database classes and tables
Base = declarative_base()

# Class for the xp records table, will likely move this to another file/directory for readability
class XpRecords(Base):

    __tablename__ = 'playerdata'

    # Database referencing
    id = Column(Integer, primary_key=True) # Remember to update the old tables to have a unique id or else the old table is worthless

    # Data referencing (?)
    username = Column(String)
    day = Column(String)

    # XP stats
    Overall = Column(Integer)
    Attack = Column(Integer)
    Defence = Column(Integer)
    Strength = Column(Integer)
    Hitpoints = Column(Integer)
    Ranged = Column(Integer)
    Prayer = Column(Integer)
    Magic = Column(Integer)
    Cooking = Column(Integer)
    Woodcutting = Column(Integer)
    Fletching = Column(Integer)
    Fishing = Column(Integer)
    Firemaking = Column(Integer)
    Crafting = Column(Integer)
    Smithing = Column(Integer)
    Mining = Column(Integer)
    Herblore = Column(Integer)
    Agility = Column(Integer)
    Thieving = Column(Integer)
    Slayer = Column(Integer)
    Farming = Column(Integer)
    Runecrafting = Column(Integer)
    Hunter = Column(Integer)
    Construction = Column(Integer)

class LastAccessed(Base):

    __tablename__ = 'playerrate'

    id = Column(Integer, primary_key=True)

    username = Column(String, ForeignKey('playerdata.username'))
    accessed = Column(String)

def connect_to_db():
    return 1


# establishes a connection, runs the query
def execute_query(query):

    return 1


# establishes a connection, executes the query and commits changes to the database
def query_commit(query):

    return 1


def initialise_user_table():
    return 1
def check_day(username,date):

    return 1

def add_new_user():

    return 1

def add_xp_record(username):

    xpData = requestsHandler.retrieve_current_xp(username)

    date = datetime.datetime.now()

    if not check_day(username, date):

        insertVars = (
            username, date.strftime("%x"), xpData[0], xpData[1], xpData[2], xpData[3], xpData[4], xpData[5], xpData[6],
            xpData[7], xpData[8], xpData[9], xpData[10], xpData[11], xpData[12], xpData[13], xpData[14], xpData[15],
            xpData[16], xpData[17], xpData[18], xpData[19], xpData[20], xpData[21], xpData[22], xpData[23])

        for x in range(24):
            print(xpData[x])

    else:
        return 1


def get_xp_records_for_user(username):

    return 1


def get_xp_record_for_skills(skill, username):

    return 1
