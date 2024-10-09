import psycopg2, contextlib, json
from psycopg2 import connect, Error
from getpass import getpass
from string import Formatter

def initQueries():
    with open('modules/db/files/SQL.json', 'r') as queryFile:
        queryDict = json.load(queryFile)
    return queryDict

def initDBInfo(userName, userPsswd):
    DBinfo = {}
    with open('modules/db/files/DB_config.json' 'r') as infile:
        dbParms = json.load(infile)
        DBinfo["DB"] = dbParms["Database"]
        DBinfo["port"] = dbParms["Port"]
        DBinfo["host"] = dbParms["Host"]
        DBinfo["user"] = userName
        DBinfo["passwd"] = userPsswd
    return DBinfo

def testConnection(DBinfo):
    try:
        with contextlib.closing(connect(
            host=DBinfo["host"],
            user=DBinfo["user"],
            password=DBinfo["passwd"],
            port=DBinfo["port"],
            database=DBinfo["DB"],
        )) as connection:
            return 0
    except Error as e:
        print("Failed login: ", e)
        return 1

def getQuery(queryName, queryDict):
    query = queryDict[queryName]
    parameters = [pname for _, pname, _, _ in Formatter().parse(query) if pname]
    parametersDict = {}
    for param in parameters:
        parametersDict[param] = "NULL"
    return query, parametersDict

def setParameters(key, value, parametersDict):
    parametersDict[key] = "'" + value + "'"
    return parametersDict

def buildExecSQL(query, parametersDict):
    execSQL = query.format(**parametersDict)
    return execSQL

def execSQL(DBinfo, execSQL):
    try:
        with contextlib.closing(connect(
            host=DBinfo["host"],
            user=DBinfo["user"],
            password=DBinfo["passwd"],
            port=DBinfo["port"],
            database=DBinfo["DB"],
        )) as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(execSQL)
                if cursor.description is not None:
                    results = cursor.fetchall()
                else:
                    results = None
    except Error as e:
        print("Error: ", e)
    
    return results
