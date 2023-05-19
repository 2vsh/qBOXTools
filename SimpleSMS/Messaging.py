from twilio.rest import Client
import random

# Your Account SID from twilio.com/console
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
# Your Auth Token from twilio.com/console
auth_token  = 'YOUR_TWILIO_AUTH_TOKEN'

client = Client(account_sid, auth_token)

# Read quotes from file
with open("quotes.txt", "r") as file:
    quotes = file.readlines()

# Choose a random quote from the list
quote_to_send = random.choice(quotes)

message = client.messages.create(
    to="TO_PHONE_NUMBER",  # Replace with your phone number
    from_="YOUR_TWILIO_PHONE_NUMBER",  # Replace with your Twilio number
    body=quote_to_send.strip())  # strip() is used to remove newline character at the end of the quote

print(message.sid)
