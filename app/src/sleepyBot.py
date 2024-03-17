import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from flask import Flask, request
# from responses import get_response

load_dotenv('.env')

TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True #Careful with this
client = Client(intents=intents)

async def send_message(message,user_message) -> None:
    if not user_message:
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # replace this with a call to the cardMaker API
        response = "Hello"
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as error:
        print(error)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_msg = message.content
    channel = str(message.content)

    print(f'[{channel}] {username}: "{user_msg}"')

def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()