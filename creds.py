#import os
#from dotenv import load_dotenv, find_dotenv
import json

with open('app.json') as json_file:
    data = json.load(json_file)
#load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("BOT_NAME")
    BOT_TOKEN = os.getenv("BOT_TOKEN") 
    API_ID = os.getenv( "API_ID") 
    API_HASH = os.getenv("API_HASH")  
    DB_URL = os.getenv("DB_URL")  
    
