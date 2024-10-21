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

if len(args) != 1:
    print("Incorrect amount of arguments given.\n")
    if args[1] == '-i':
        db.db_install.createDB()
    else if args[1] == '-r':
        DBInfo, DBqueries = setup()
        aunch_management_screen(DBInfo)
