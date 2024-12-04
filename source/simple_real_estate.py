import os
import sys

args = sys.argv

if len(args) != 2:
    print("Incorrect amount of arguments given.\n")
elif len(args) == 2:
    if args[1] == "-i":
        os.system('python simple_real_estate_1/manage.py makemigrations')
        os.system('python simple_real_estate_1/manage.py migrate')
    elif args[1] == "-r":
        os.system('python simple_real_estate_1/manage.py runserver')
