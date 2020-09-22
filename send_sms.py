# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc5444fea832cfe7262e27871e857461b'
auth_token = 'cfef47077a10129e460befc1b7600c98'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19284930567',
                     to='+14083750019'
                 )
print(message.sid)                 

message = client.messages \
                .create(
                     body="Glory Freedom  Victory.",
                     from_='+19284930567',
                     to='+14083750019'
                 )      

print(message.sid)


message = client.messages \
                .create(
                     body="Glory Freedom  Victory   2222.",
                     file="c:\twilio\sample\send_sms.py",
                     from_='+19284930567',
                     to='+14083750019'
                 )      