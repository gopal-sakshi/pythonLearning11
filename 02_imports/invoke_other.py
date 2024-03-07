# this imports the file which is in different folder

import sys, os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'03_functions'))
from invoke_function1 import *

# add_numbers(4,65)

# https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files

'''
to disable generating __pycache__
try this later
    (A) export PYTHONDONTWRITEBYTECODE=1
    (B) import sys
        sys.dont_write_bytecode = True
'''