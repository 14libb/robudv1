from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe6184b9f6756e195a776511a3d781c6b"
auth_token  = "b16d4a0b445027ac689c8620a3a8b81f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Eliza, this is Betsy's computer that's not imessage",
    to="+12079076575",    # Replace with your phone number
    from_="+12084953908") # Replace with your Twilio number
print message.sid