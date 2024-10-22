import sqlite3, json
from . import db
from sqlite3 import Error
from string import Formatter
DB = db.db_interface


LIST_PROPERTIES          = "LIST_PROPERTIES"
VIEW_PROPERTY            = "VIEW_PROPERTY"
LIST_UNITS               = "LIST_UNITS"
VIEW_UNIT                = "VIEW_UNIT"
LIST_RENTAL_AGREEMENTS   = "LIST_RENTAL_AGREEMENTS"
VIEW_RENTAL_AGREEMENT    = "VIEW_RENTAL_AGREEMENT"
LIST_RENTAL_INVOICES     = "LIST_RENTAL_INVOICES"
VIEW_RENTAL_INVOICE      = "VIEW_RENTAL_INVOICE"
LIST_EXP_RECORDS         = "LIST_EXP_RECORDS"
VIEW_EXP_RECORDS         = "VIEW_EXP_RECORDS"
LIST_EXP_RECORD_ITEMS    = "LIST_EXP_RECORD_ITEMS"
REPORT_VAR_EXP           = "REPORT_VAR_EXP"
REPORT_FIX_EXP           = "REPORT_FIX_EXP"

## No paramters
def init_list_properties(DBInfo, queryDict):
  query = DB.getQuery(LIST_PROPERTIES, queryDict)
  return query, parms
def list_properties(DBInfo, parms, query):
  if parms is not None:
    for key, value in parms:
      setParms = DB.setParameters(key, value, parms)
    sql = DB.buildExecSQL(query, setParms)
  else:
    sql = query
  results = DB.execSQL(DBInfo, sql)
  return results

## Parameters: {property_id}
def init_view_property(DBInfo, queryDict):
  query = DB.getQuery(VIEW_PROPERTY, queryDict)
  parms = DB.initParmDict(query)
  return query, parms
def view_property(DBInfo, parms, query):
  if parms is not None:
    for key, value in parms:
      setParms = DB.setParameters(key, value, parms)
    sql = DB.buildExecSQL(query, setParms)
  else:
    sql = query
  results = DB.execSQL(DBInfo, sql)
  return results

## Parameters: {property_id}
def init_list_units(DBInfo, queryDict):
  query = DB.getQuery(LIST_UNITS, queryDict)
  parms = DB.initParmDict(query)
  return query, parms
def list_unit(DBInfo, parms, query):
  if parms is not None:
    for key, value in parms:
      setParms = DB.setParameters(key, value, parms)
    sql = DB.buildExecSQL(query, setParms)
  else:
    sql = query
  results = DB.execSQL(DBInfo, sql)
  return results

## Parameters: {property_id}, {unit_id}
def init_view_unit(DBInfo, queryDict):
  query = DB.getQuery(VIEW_UNIT, queryDict)
  parms = DB.initParmDict(query)
  return query, parms
def view_unit(DBInfo, parms, query):
  if parms is not None:
    for key, value in parms:
      setParms = DB.setParameters(key, value, parms)
    sql = DB.buildExecSQL(query, setParms)
  else:
    sql = query
  results = DB.execSQL(DBInfo, sql)
  return results
  
