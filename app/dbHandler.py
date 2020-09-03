import mysql.connector
import datetime
from app import requestsHandler

def connect_to_db():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")


# establishes a connection, runs the query
def execute_query(query):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()
    dbcursor.execute(query)

    result = dbcursor.fetchall()

    return result


# establishes a connection, executes the query and commits changes to the database
def query_commit(query):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()
    dbcursor.execute(query)


def initialise_user_table():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()
    query = """CREATE TABLE IF NOT EXISTS playerdata(
                    playername VARCHAR(12) NOT NULL,
                    day VARCHAR(10) NOT NULL,
                    Overall INT,
                    Attack INT,
                    Defence INT,
                    Strength INT,
                    Hitpoints INT,
                    Ranged INT,
                    Prayer INT,
                    Magic INT,
                    Cooking INT,
                    Woodcutting INT,
                    Fletching INT,
                    Fishing INT,
                    Firemaking INT,
                    Crafting INT,
                    Smithing INT,
                    Mining INT,
                    Herblore INT,
                    Agility INT,
                    Thieving INT,
                    Slayer INT,
                    Farming INT,
                    Runecrafting INT,
                    Hunter INT,
                    Construction INT
                );
            """
    dbcursor.execute(query)

def check_day(username,date):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()

    query = f"""SELECT COUNT(*) FROM playerdata WHERE day='""" \
            + date.strftime("%x") + """' AND playername='""" + username + """'"""

    dbcursor.execute(query)

    result = dbcursor.fetchone()[0]

    if result > 0:
        exists = True
    else:
        exists = False

    print(exists)

    return exists

def add_new_user():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()


def add_xp_record(username):

    xpData = requestsHandler.retrieve_current_xp(username)

    date = datetime.datetime.now()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="osrsdatabase")

    dbcursor = mydb.cursor()

    if not check_day(username, date):

        insertVars = (
            username, date.strftime("%x"), xpData[0], xpData[1], xpData[2], xpData[3], xpData[4], xpData[5], xpData[6],
            xpData[7], xpData[8], xpData[9], xpData[10], xpData[11], xpData[12], xpData[13], xpData[14], xpData[15],
            xpData[16], xpData[17], xpData[18], xpData[19], xpData[20], xpData[21], xpData[22], xpData[23])

        for x in range(24):
            print(xpData[x])

        query = query = f"""
        INSERT INTO playerdata(
        playername, day, 
        Overall,
        Attack, 
        Defence, 
        Strength, 
        Hitpoints, 
        Ranged, 
        Prayer, 
        Magic, 
        Cooking, 
        Woodcutting, 
        Fletching, 
        Fishing, 
        Firemaking, 
        Crafting, 
        Smithing, 
        Mining, 
        Herblore, 
        Agility, 
        Thieving, 
        Slayer, 
        Farming, 
        Runecrafting, 
        Hunter, 
        Construction)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        dbcursor.execute(query, insertVars)

        mydb.commit()
    else:

        insertVars = (
            xpData[0], xpData[1], xpData[2], xpData[3], xpData[4], xpData[5], xpData[6],
            xpData[7], xpData[8], xpData[9], xpData[10], xpData[11], xpData[12], xpData[13], xpData[14], xpData[15],
            xpData[16], xpData[17], xpData[18], xpData[19], xpData[20], xpData[21], xpData[22], xpData[23])

        print("Record for " + username + " already exists for today, updating existing record...")

        query = """UPDATE playerdata SET Overall = %s, Attack = %s, Defence = %s, Strength = %s, Hitpoints = %s, 
                    Ranged = %s, Prayer = %s, Magic = %s, Cooking = %s, Woodcutting = %s, Fletching = %s, Fishing = %s, Firemaking = %s, 
                    Crafting = %s, Smithing = %s, Mining = %s, Herblore = %s, Agility = %s, Thieving = %s, Slayer = %s, Farming = %s, 
                    Runecrafting = %s, Hunter = %s, Construction = %s 
                    WHERE day = '""" + date.strftime("%x") + """' AND playername = '""" + username + """'
                    """  # needs better formatting, this is borderline unreadable.

        dbcursor.execute(query, insertVars)
        mydb.commit()


def get_xp_records_for_user(username):

    query = """
            SELECT * FROM playerdata WHERE playername = '""" + username + """'"""

    result = execute_query(query)

    return result


def get_xp_record_for_skills(skill, username):

    query = """
            SELECT """+skill+""" FROM playerdata WHERE playername = '""" + username + """'"""

    result = execute_query(query)

    return result
