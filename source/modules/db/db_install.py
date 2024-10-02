#init-db_real_estate.sql
import psycopg2
from psycopg2 import connect, Error
from getpass import getpass

DBinfo ={}
DBinfo["DB"] = input("Enter install database name (default: postgres): ")
DBinfo["port"] = input("Enter install database port (default: ###): ")
DBinfo["host"] = input("Enter install database port (default: ###): ")
DBinfo["user"] = input("Enter install database username (default: postgres): ")
DBinfo["passwd"] = getpass("Enter install database password: ")
