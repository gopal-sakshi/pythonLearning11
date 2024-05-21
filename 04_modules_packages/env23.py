# using envi variables in python
# python3 -m pip install python-dotenv


# the dotenv module loads environment variables from the .env file 
# to the environment Python can access with the os module. 
###### (or) 
# load_dotenv() ===> brings all environment variables from .env into os.environ



from dotenv import load_dotenv
import os

load_dotenv()
print("clubName ====> ", os.environ['clubName'])
print("manager ====> ", os.environ['manager23'])