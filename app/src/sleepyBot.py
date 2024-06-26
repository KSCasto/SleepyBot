import os
from dotenv import load_dotenv

import disnake as discord
from disnake.ext import commands

from utils import sleepyMessages

# Load environment variables from a .env file
load_dotenv('.env')
# Retrieve the Discord bot token from the environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize a new instance of the Discord bot
bot = commands.Bot(command_prefix='/')

# Event handler for when the bot has successfully connected and is ready
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

# Define a slash command with a description
@bot.slash_command(
    name="upload-pics",  # Updated command name
    description="Upload a zip file of images to be turned into cards"
)
async def upload_card_images(interaction: discord.ApplicationCommandInteraction, file: discord.Attachment):
    # Save the file to the current directory
    await file.save(file.filename)

    # Respond to the interaction with a message confirming the received file
    await interaction.response.send_message(f"Received and saved file: {file.filename}")

# Event handler for when a message is sent in any channel the bot has access to
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return
    
    # Extract message author, content, and channel
    username = str(message.author)
    user_msg = message.content
    channel = str(message.channel)
    
    # Use a utility function to handle and possibly respond to the message
    await sleepyMessages.send_message(message, user_msg)

    # Print the message details to the console for logging
    print(f'[{channel}] {username}: "{user_msg}"')

# Main function to run the bot
def main():
    bot.run(TOKEN)

# Entry point of the script
if __name__ == '__main__':
    main()
