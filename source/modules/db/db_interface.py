import psycopg2, contextlib, json
from psycopg2 import connect, Error
from getpass import getpass
from string import Formatter

def initQueries():
  with opne("SQL.json") as queryFile:
    queryDict = json.load(queryFile)
  return queryDict

def initDBInfo():
  DBinfo = {}
  with open() as infile:
    dbParms = json.load(infile)
  DBinfo["DB"] = dbParms["Database"]
  DBinfo["port"] = dbParms["Port"]
  DBinfo["host"] = dbParms["Host"]
  DBinfo["user"] = input("Enter username: ")
  DBinfo["passwd"] = getpass("Enter password: ")
  return DBinfo

def getQuery(queryName, queryDict):
  query = queryDict[queryName]
  parameters = [pname for _, pname, _, _ in Formatter().parse(query) if pname]
  parametersDict = {}
  for param in parameters:
    parametersDict[param] = "NULL"
  return query, parametersDict

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
