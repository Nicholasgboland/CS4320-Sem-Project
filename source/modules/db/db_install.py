import sqlite3, json
from sqlite3 import Error
from string import Formatter

def createDB():
    DBinfo = {"DB": 'modules/db/files/real_estate.db'}
    with open('modules/db/files/init-db_real_estate.sql') as infile:
        sqlFile = infile.read()
        try:
            with sqlite3.connect(DBinfo["DB"]) as connection:
                with connection.cursor() as cursor:
                    cursor.executescript(sqlFile)
        except Error as e:
            print("Error: ", e)
            
    with open('modules/db/files/DB_config.json', 'w') as outfile:
        jsonFile = json.dumps(DBinfo, indent=4)
        outfile.write(jsonFile)
