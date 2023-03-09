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
for i in matchups:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=matchups[i].name + ", You are hunting: " + matchups[i].target,
        from_='+18776411788',
        to=matchups[i].number
    )

    print(message.sid)


