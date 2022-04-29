from twilio.rest import Client 
 
account_sid = 'SID' 
auth_token = '[AUTH_TOKEN]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='M_SID', 
                              body='Hi Saikat. Have a good day.',
                              from_= 'SENDER',      
                              to='RECEIVER' 
                          ) 
 
print(message.sid)