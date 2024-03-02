all these files are same as those in python24 folder
- just we are using venv


`pyenv virtualenv 3.12 pyenv3120`
- now a venv is created ===> "pyenv3120" is its name
- cd to "python24_venv23" folder
- run this command ====> <pyenv local pyenv3120>
    a file is created ---> .python-version
- `pyenv virtualenv-delete pyenv3120`
- <pyenv virtualenvs>
- type "pyenv"  to see list of options

----------------------------------------------------------------------------

<!-- to run the python program normally -->
    python3 randomNum23.py

<!-- to run the program in venv -->
    Ctrl Shift P ---> create environment
    use requirements.txt
    .venv folder will be created...

    "source .venv/bin/activate" _____________ "deactivate"
    (.venv) krishna~$ python3 python24_venv23/numpy12.py
    (.venv) krishna~$ python3 python24_venv23/randomNum23.py

    (OR) notice there is no (.venv) --> means bash shell isnt in venv
    krishna~$ .venv/bin/python3 python24_venv23/numpy12.py
    .venv/bin/python3 ====> is the path where venv is installed
----------------------------------------------------------------------------

https://stackoverflow.com/questions/70515194/syntaxerror-future-feature-annotations-is-not-defined