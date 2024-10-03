#init-db_real_estate.sql
import psycopg2
from psycopg2 import connect, Error
from getpass import getpass

DBinfo ={}
DBinfo["DB"] = "postgres"
DBinfo["port"] = input("Enter install database port (default: ###): ")
DBinfo["host"] = input("Enter install database port (default: ###): ")
DBinfo["user"] = input("Enter install database username (default: postgres): ")
DBinfo["passwd"] = getpass("Enter install database password: ")

with open('init-db_real_estate.sql') as infile:
  for row in infile:
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
