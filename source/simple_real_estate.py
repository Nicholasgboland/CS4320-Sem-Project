import modules, sys
from modules import db
# from modules import db, gui
DB = db.db_interface

def setup():
    DBInfo = DB.initDBInfo()
    queries = DB.initQueries()
    return DBInfo, queries

def launch_management_screen(DBInfo):
    # Code to launch the initial GUI screen

args = sys.argv

if len(args) != 0:
    if len(args) > 1:
        print("Too manay arguments given.\n")
    else:
        db.db_install.createDB()
else:
    DBInfo, DBqueries = setup()
    launch_management_screen(DBInfo)
