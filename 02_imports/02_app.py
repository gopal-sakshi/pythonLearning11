# execfile("./02lib23.py")             # execfile is python2

### with block safely closes the file that it opened
with open("02_lib23.py", "r") as f:
    exec(f.read())
    
exec(open("02_lib23.py").read())

