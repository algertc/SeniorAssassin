#SMS Stuff
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv() #Required to load env vars into python virtualenv
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#Create Matchups
import Bracket
matchups = Bracket.createMatchups()

#Notify Teams
for team in matchups:
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
            .create(
            body=str(team.name) + ", You are hunting: " + team.getTarget(),
            from_='+19257019524',
            to=team.number
        )
        print(message.sid)
    except:
        print(team.name + ": Invalid Phone number")



