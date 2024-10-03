#init-db_real_estate.sql
import psycopg2
from psycopg2 import connect, Error
from getpass import getpass
from string import Formatter

DBinfo ={}
adminDBinfo["DB"] = "postgres"
adminDBinfo["port"] = input("Enter install database port (default: ###): ")
adminDBinfo["host"] = input("Enter install database port (default: ###): ")
adminDBinfo["user"] = input("Enter install database username (default: postgres): ")
adminDBinfo["passwd"] = getpass("Enter install database password: ")

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
          directory = []
          cursor.execute("SHOW data_directory")
          if cursor.definition is not None:
            directory = cursor.fetchall()
            DBinfo["directory"] = directory
          cursor.execute("CREATE DATABASE real_estate")
          cursor.execut(createUsrSQL)
          cursor.execut(grant1SQL)
          cursor.execut(grant2SQL)
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
