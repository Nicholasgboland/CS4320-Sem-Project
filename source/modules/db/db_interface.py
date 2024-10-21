import sqlite3, json
from sqlite3 import Error
from string import Formatter

def initQueries():
    with open('modules/db/files/SQL.json', 'r') as queryFile:
        queryDict = json.load(queryFile)
    return queryDict

def initDBInfo():
    DBinfo = {}
    with open('modules/db/files/DB_config.json' 'r') as infile:
        dbParms = json.load(infile)
        DBinfo["DB"] = dbParms["DB"]
    return DBinfo

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
        with sqlite3.connect(DBinfo["DB"]) as connection:
            cursor = connection.cursor()
            cursor.execute(execSQL)
            results = cursor.fetchall()
            cursor.close()
    except Error as e:
        print("Error: ", e)
    
    return results
