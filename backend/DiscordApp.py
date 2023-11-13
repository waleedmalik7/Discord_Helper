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
    response = requests.post(url, data=my_data, headers=my_header)
    return response.status_code

def deleteMessage(token, channel_id, message_id):
    url = "https://discord.com/api/v9/channels/{}/messages/{}".format(channel_id,message_id)
    my_header = {"authorization": token}
    response = requests.delete(url=url,headers=my_header)
    return response.status_code
    
def getMessageId(token, channel_id, last_message_id):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    my_header = {"authorization": token}
    params = {"before": last_message_id}
    response = requests.get(url=url, headers=my_header, params=params)
    messages = response.json()
    return messages[-1]["id"], messages

def getLatestMessageId(token, channel_id):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id) 
    my_header = {"authorization": token}
    response = requests.get(url=url,headers=my_header)
    message = response.json()
    return message[0]['id'], message[0]['content']

def getUsername(token):
    url = "https://discord.com/api/v9/users/@me"
    my_header = {"authorization": token}
    response = requests.get(url=url,headers=my_header)
    return response.json()['username']

#Get Message ID's and create a file of all the message IDs with author['id'] == ''
#Each time we run the messageId we have to identify a start point as a param

#Start with current ID, returns 50 message IDs if author is 'username' and ID of the next start point

#Need to change currID
counter = 0
username = getUsername(token)
currID,latest_message = getLatestMessageId(token,channel_id)
status = deleteMessage(token,channel_id,currID)

with open('deleted_messages.txt', 'w') as file:
    file.write("STATUS: {}, Deleting: {} \n".format(status,latest_message))
    file.flush()   
    # while(currID != 1):
    while(counter < 20):
        counter += 1
        currID, messages = getMessageId(token, channel_id, currID)
        for message in messages:
            if message["author"]["username"] == username:
                status = deleteMessage(token,channel_id,message["id"])
                sleep(3)
                file.write("STATUS: {}, Deleting: {} \n".format(status,message["content"]))
                file.flush()   

#Delete the 50 messages based on ID
#Update the next start point and continues 