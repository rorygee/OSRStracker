import requests


# accepts username (string), returns the xp in each skill (array:int)
def retrieve_current_xp(username):

    stats = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='+username)
    skills = stats.text.split("\n")[0:24]

    # need to add error handling for various http codes

    xpData = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x, stats in zip(range(24), skills):
        stat = stats.split(",")
        xpData[x] = int(stat[2])

    return xpData

