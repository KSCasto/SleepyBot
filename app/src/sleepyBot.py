import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from utils import sleepyMessages

load_dotenv('.env')

TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True #Careful with this
bot = commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    username = str(message.author)
    user_msg = message.content
    channel = str(message.channel)
    await sleepyMessages.send_message(message,user_msg)

    print(f'[{channel}] {username}: "{user_msg}"')

def main():
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()