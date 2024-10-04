#init-db_real_estate.sql
import psycopg2
from psycopg2 import connect, Error
from getpass import getpass
from string import Formatter

DBinfo = {}
adminDBinfo = {}
adminDBinfo["DB"] = "postgres"
adminDBinfo["port"] = input("Enter install database port (default: 5432): ")
adminDBinfo["host"] = "localhost"
adminDBinfo["user"] = "postgres"
adminDBinfo["passwd"] = getpass("Enter install database admin (postgres) password: ")

print("Creating new login user, this will be the username/password that will be used to login to the application:")
DBinfo["DB"] = adminDBinfo["DB"]
DBinfo["port"] = adminDBinfo["port"]
DBinfo["host"] = adminDBinfo["host"]
DBinfo["user"] = input("Enter new database username: ")
DBinfo["passwd"] = getpass("Enter new database password: ")

createUsrSQL = "CREATE USER {newUser} WITH PASSWORD '{newPasswd}'".format(newUser = DBinfo["user"], newPasswd = DBinfo["passwd"])
grant1SQL = "GRANT CONNECT ON DATABASE real_estate TO {newUser}".format(newUser = DBinfo["user"])
grant2SQL = "GRANT ALL PRIVILEGES ON DATABASE real_estate to {newUser}".format(newUser = DBinfo["user"])


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
          cursor.execute(createUsrSQL)
          cursor.execute(grant1SQL)
          cursor.execute(grant2SQL)
  except Error as e:
    print("Error: ", e)

with open('init-db_real_estate.sql') as infile:
  lines = infile.readlines()
  for line in lines:
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
    except Error as e:
      print("Error: ", e)

with open('DB_config.json', 'w') as outfile:
  jsonFile = json.dumps(DBinfo, indent=4)
  outfile.write(jsonFile)
