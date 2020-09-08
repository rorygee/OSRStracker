import mysql.connector
import datetime
from app import requestsHandler

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
