import psycopg2, json, contextlib
from psycopg2 import connect, Error, sql
from getpass import getpass
from string import Formatter

def getAdminDBParms():
    adminDBinfo = {}
    adminDBinfo["DB"] = "postgres"
    adminDBinfo["port"] = input("Enter install database port (default: 5432): ")
    adminDBinfo["host"] = "localhost"
    adminDBinfo["user"] = "postgres"
    adminDBinfo["passwd"] = getpass("Enter install database admin (postgres) password: ")

    return adminDBinfo

def getDBParms(adminDBinfo):
    DBinfo = {}
    print("Creating new login user, this will be the username/password that will be used to login to the application:")
    DBinfo["DB"] = "real_estate"
    DBinfo["port"] = adminDBinfo["port"]
    DBinfo["host"] = "localhost"
    DBinfo["user"] = input("Enter new database username: ")
    DBinfo["passwd"] = getpass("Enter new database password: ")

    return DBinfo

def initSQL(adminDBinfo, DBinfo):
    try:
        with contextlib.closing(connect(
            host=adminDBinfo["host"],
            user=adminDBinfo["user"],
            password=adminDBinfo["passwd"],
            port=adminDBinfo["port"],
            database=adminDBinfo["DB"],
        )) as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                dataDirectory = []
                cursor.execute("SHOW data_directory")
                if cursor.description is not None:
                    dataDirectory = cursor.fetchall()
                    DBinfo["directory"] = dataDirectory
                cursor.execute("CREATE DATABASE real_estate")
    except Error as e:
        print("Error: ", e)

def execSQL(execSQL, DBparms):
    try:
        with contextlib.closing(connect(
            host=DBparms["host"],
            user=DBparms["user"],
            password=DBparms["passwd"],
            port=DBparms["port"],
            database=DBparms["DB"],
        )) as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(execSQL)
    except Error as e:
        print("Error: ", e)

def createDB(DBinfo):
    with open('files/init-db_real_estate.sql') as infile:
        sqlFile = infile.read()
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
                    cursor.execute(sqlFile)
        except Error as e:
            print("Error: ", e)


adminDBparms = getAdminDBParms()
DBparms = getDBParms(adminDBparms)
initSQL(adminDBparms, DBparms)

createUsrSQL = "CREATE ROLE {newUser} LOGIN PASSWORD '{newPasswd}'".format(newUser = DBparms["user"], newPasswd = DBparms["passwd"])
grant1SQL = "GRANT CONNECT ON DATABASE real_estate TO {newUser}".format(newUser = DBparms["user"])
grant2SQL = "GRANT ALL PRIVILEGES ON DATABASE real_estate to {newUser}".format(newUser = DBparms["user"])
grant3SQL = "GRANT USAGE, CREATE ON SCHEMA public TO {newUser}".format(newUser = DBparms["user"])

execSQL(createUsrSQL, adminDBparms)
execSQL(grant1SQL, adminDBparms)
execSQL(grant2SQL, adminDBparms)
execSQL(grant3SQL, adminDBparms)
adminDBparms["DB"] = "real_estate"
execSQL(grant3SQL, adminDBparms)
createDB(DBparms)

with open('files/DB_config.json', 'w') as outfile:
    jsonFile = json.dumps(DBparms, indent=4)
    outfile.write(jsonFile)
