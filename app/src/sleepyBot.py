import os
from dotenv import load_dotenv

import disnake as discord
from disnake.ext import commands

from utils import sleepyMessages
from services import makeCards

# the .env file must be in the same directory as this script
load_dotenv('.env')
# go to the bot panel in the discord dev portal to get this token, store it securely
TOKEN = os.getenv('DISCORD_TOKEN')
# This integer indicates which permissions the bot has, generated from the dev portal
INTENTS_INT = int(os.getenv('PERMISSION_INT'))
bot_intents = discord.Intents(value=INTENTS_INT)
bot = commands.Bot(command_prefix='/',intents=bot_intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.slash_command(
    name="upload-pics",  # If this is not specified, the function name will be the slash command name
    description="Upload a zip file of images to be turned into cards"
)
async def upload_card_images(interaction: discord.ApplicationCommandInteraction, file: discord.Attachment):
    # Replace this stuff with a call to the cardMaker API so the response can be the resulting PDF
    # zip = await file.to_file(description="PDF generated from your images")
    zip = await file.read()
    try:
        pdfBytes = await makeCards.send_zip(zip)
        PDF = discord.File(pdfBytes, filename="output.pdf")
        # Respond to the interaction with a message confirming the received file
        await interaction.followup.send(content=f"Received and saved file: {file.filename}", file=PDF)
    except:
        await interaction.followup.send(content=f"Oops!")

# Event handler for when a message is sent in any channel the bot has access to
# This is a stand in skeleton for adding little easter eggs or auto detection of people
# struggling with using the bot. For now it just says a small greeting.
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return
    
    # Use message objects to grab any necessary details
    username = str(message.author)
    user_msg = message.content
    channel = str(message.channel)
    
    # Use a utility function to handle and possibly respond to the message
    await sleepyMessages.send_message(message, user_msg)

    # Print the message details to the console for logging
    print(f'[{channel}] {username}: "{user_msg}"')

def main():
    bot.run(TOKEN)

# Entry point of the script
if __name__ == '__main__':
    main()
