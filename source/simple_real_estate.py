import modules, sys
from modules import db
DB = db.db_interface
install = db.db_install

def setup():
    DBInfo = DB.initDBInfo()
    queries = DB.initQueries()
    return DBInfo, queries

def launch_management_screen(DBInfo):
    # Code to launch the initial GUI screen
    print("Launching...")

args = sys.argv

if len(args) != 2:
    print("Incorrect amount of arguments given.\n")
elif len(args) == 2:
    if args[1] == "-i":
        install.createDB()
    elif args[1] == "-r":
        DBInfo, DBqueries = setup()
        launch_management_screen(DBInfo)
