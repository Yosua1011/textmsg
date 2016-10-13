from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb0980dde16552bc6988e3567fda81878"
auth_token = "fe8bfaea54fd9ea1cb860372475d098f"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body="Hello, World!",
	to="+6281281368782", #Destination phone number
	from_="+19315480502") #Twilio number
print message.sid
	