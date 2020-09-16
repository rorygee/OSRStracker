# Imports

import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import requestsHandler

# Database Handler (SQLAlchemy/MySQL) #


# Establish a 'global' connection, need to modify to use a mysql driver
engine = create_engine('mysql://root@localhost:3306/osrsdatabase', echo=True)

session = sessionmaker(bind=engine)

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

def initialise_user_table():

    return 1

def check_day(username,date):

    return 1

def add_xp_record(username):

    xpData = requestsHandler.retrieve_current_xp(username)

    date = datetime.datetime.now()

    if not check_day(username, date):

        for x in range(24):
            print(xpData[x])

        session.add(XpRecords(username=username, day=datetime.datetime.now(),
                              Overall=xpData[0],
                              Attack=xpData[1],
                              Defence=xpData[2],
                              Strength=xpData[3],
                              Hitpoints=xpData[4],
                              Ranged=xpData[5],
                              Prayer=xpData[6],
                              Magic=xpData[7],
                              Cooking=xpData[8],
                              Woodcutting=xpData[9],
                              Fletching=xpData[10],
                              Fishing=xpData[11],
                              Firemaking=xpData[12],
                              Crafting=xpData[13],
                              Smithing=xpData[14],
                              Mining=xpData[15],
                              Herblore=xpData[16],
                              Agility=xpData[17],
                              Thieving=xpData[18],
                              Slayer=xpData[19],
                              Farming=xpData[20],
                              Runecrafting=xpData[21],
                              Hunter=xpData[22],
                              Construction=xpData[23]))

    else:

        replacedRecord = session.query(XpRecords).filter_by(username=username, day=datetime.datetime.now()).first()

        session.add(XpRecords(replacedRecord(
                              Overall=xpData[0],
                              Attack=xpData[1],
                              Defence=xpData[2],
                              Strength=xpData[3],
                              Hitpoints=xpData[4],
                              Ranged=xpData[5],
                              Prayer=xpData[6],
                              Magic=xpData[7],
                              Cooking=xpData[8],
                              Woodcutting=xpData[9],
                              Fletching=xpData[10],
                              Fishing=xpData[11],
                              Firemaking=xpData[12],
                              Crafting=xpData[13],
                              Smithing=xpData[14],
                              Mining=xpData[15],
                              Herblore=xpData[16],
                              Agility=xpData[17],
                              Thieving=xpData[18],
                              Slayer=xpData[19],
                              Farming=xpData[20],
                              Runecrafting=xpData[21],
                              Hunter=xpData[22],
                              Construction=xpData[23])))


def get_xp_records_for_user(username):

    # Retrieving all records from the database
    xpRecords = session.query(XpRecords).filter_by(username=username).all()

    for row in xpRecords:
        print(1)
    return xpRecords