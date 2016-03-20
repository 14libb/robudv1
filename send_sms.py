from twilio.rest import TwilioRestClient
import random
import time

d = ["Your smile is contagious","You look great today","I love you",
     "You're a smart cookie","You're better than a triple-scoop ice cream cone. With sprinkles",
     "Is that your picture next to 'charming' in the dictionary?"]

for i in range(1):
    random.shuffle(d)
    time.sleep(float(random.randint(1,6)))
    print d[0]
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe6184b9f6756e195a776511a3d781c6b"
auth_token  = "b16d4a0b445027ac689c8620a3a8b81f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body=d[0],
    to="+12079076406",    # Replace with your phone number
    from_="+12084953908") # Replace with your Twilio number
print message.sid

# Code that doesn't work yet...

# import random
# import time
# from twilio.rest import TwilioRestClient

# d = ["Your smile is contagious","You look great today","I love you",
#      "You're a smart cookie","You're better than a triple-scoop ice cream cone. With sprinkles",
#      "Is that your picture next to 'charming' in the dictionary?"]

# while True:
#     random.shuffle(d)
#     time.sleep(float(random.randint(1,6)))
#     print d[0]
 
# # Your Account Sid and Auth Token from twilio.com/user/account
# account_sid = "AC2f85abeec7c12f097e9701a706fb8aed"
# auth_token  = "8941c1260090a8b95dcddcd9a822e1bf"
# client = TwilioRestClient(account_sid, auth_token)
 
# message = client.messages.create(body= d)
#     to="+12079076406",    # Replace with your phone number
#     from_="+2897685961") # Replace with your Twilio number
# print message.sid