#import os
#from dotenv import load_dotenv, find_dotenv
import json

with open('app.json') as json_file:
    data = json.load(json_file)
#load_dotenv(find_dotenv())


class cred:
    #BOT_NAME = os.getenv("BOT_NAME")
    #BOT_TOKEN = os.getenv("BOT_TOKEN") 
    #API_ID = os.getenv( "API_ID") 
    #API_HASH = os.getenv("API_HASH")  
    #DB_URL = os.getenv("DB_URL")  
    DB_URL=data['env']['DB_URL']['value']
    BOT_TOKEN=data['env']['BOT_TOKEN']['value']
    API_ID=data['env']['API_ID']['value']
    API_HASH=data['env']['API_HASH']['value']
    BOT_NAME=data['env']['BOT_NAME']['value']
