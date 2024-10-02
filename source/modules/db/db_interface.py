import psycopg2
from psycopg2 import connect, Error
import contextlib
from getpass import getpass
import json
from string import Formatter

def initQueries():
  with opne("SQL.json") as query_file:
    query_dict = json.load(query_file)
  return query_dict

def getQuery(queryName, query_dict):
  query = query_dict[name]
  parameters = [pname for _, pname, _, _ in Formatter().parse(query) if pname]
  parameters_dict = []
  for param in parameters:
    parameters_dict[i] = "NULL"
  return query, parameters_dict

