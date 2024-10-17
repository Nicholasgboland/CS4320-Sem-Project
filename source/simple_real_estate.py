import modules
from modules import db
# from modules import db, gui
DB = db.db_interface

def setup():
    # Call to GUI login code here (returns username, password
    DBInfo = DB.initDBInfo()
    queries = DB.initQueries()
    return DBInfo, queries

def launch_management_screen(DBInfo):
    # Code to launch the initial GUI screen
