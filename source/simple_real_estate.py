import modules
from modules import db
DB = db.db_interface

def login():
  # Call to GUI code here
    DBInfo = initDBInfo(username, password)
    testCon = DB.testConnection(DBInfo)
    if testCon != 0:
        return 1
