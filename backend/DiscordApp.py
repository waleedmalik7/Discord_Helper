import sys
import requests
from time import sleep


command_line_args = sys.argv
token = command_line_args[1]
channel_id = command_line_args[2]

def sendMessage(token, channel_id, message):
    my_data = {"content": message}
    my_header = {"authorization": token}
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    
    r = requests.post(url, data=my_data, headers=my_header)
    print(r.status_code)

def deleteMessage(token, channel_id, message_id):
    url = "https://discord.com/api/v9/channels/{}/messages/{}".format(channel_id,message_id)
    print(url)
    my_header = {"authorization": token}
    r = requests.delete(url=url,headers=my_header)
    print(r.status_code)
    
def getMessageId(token, channel_id, last_message_id):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    my_header = {"authorization": token}
    params = {"before": last_message_id}
    response = requests.get(url=url, headers=my_header, params=params)
    messages = response.json()
    return messages[-1]["id"],messages

def getLatestMessageId(token, channel_id):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id) 
    my_header = {"authorization": token}
    response = requests.get(url=url,headers=my_header)
    return response.json()[0]['id']

def getUsername(token):
    url = "https://discord.com/api/v9/users/@me"
    my_header = {"authorization": token}
    response = requests.get(url=url,headers=my_header)
    return response.json()['username']

#Get Message ID's and create a file of all the message IDs with author['id'] == ''
#Each time we run the messageId we have to identify a start point as a param

#Start with current ID, returns 50 message IDs if author is 'username' and ID of the next start point

#Need to change currID

currID = getLatestMessageId(token,channel_id)
username = getUsername(token)

print(currID,username)

# while(currID != 1):
#     currID, messages = getMessageId(token,channel_id,currID)
#     for message in messages:
#         if message["author"]["username"] == username:
#             print("Deleting:", message["content"])
#             sleep(3)
#             deleteMessage(token,channel_id,message["id"])
#     print("------------------")

#Delete the 50 messages based on ID
#Update the next start point and continues 