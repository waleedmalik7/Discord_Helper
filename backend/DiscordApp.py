from time import sleep
import requests


#Need to uncomment Below:
# token = ''
# channel_id = 

def sendMessage(token, channel_id, message):
    my_data = {
        "content": message,
        "tts": True
    }
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


#Get Message ID's and create a file of all the message IDs with author['id'] == ''
#Each time we run the messageId we have to identify a start point as a param

#Start with current ID, returns 50 message IDs if author is 'waffleed' and ID of the next start point

#Need to change currID
currID = 1
error = False
while(currID != 1):
    currID, messages = getMessageId(token,channel_id,currID)
    for message in messages:
        if message["author"]["username"] == 'waffleed':
            print("Deleting:", message["content"])
            sleep(3)
            deleteMessage(token,channel_id,message["id"])
    print("------------------")

#Delete the 50 messages based on ID
#Update the next start point and continues 