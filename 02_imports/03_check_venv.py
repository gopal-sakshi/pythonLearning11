# to check if python is running in venv

import sys
def in_venv():
    print(sys.prefix)
    print(sys.base_prefix)
    return sys.prefix != sys.base_prefix

in_venv()


'''
"using venv"              python3 02_imports/03_check_venv.py
    /home/gopal/Desktop/repos23/others23/pythonLearning11/.venv 
    /home/gopal/.pyenv/versions/3.12.2

"not using venv"      /usr/bin/python3 02_imports/03_check_venv.py
    /usr 
    /usr

'''
