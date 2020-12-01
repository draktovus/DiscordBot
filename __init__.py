import os
import discord
# see https://discordpy.readthedocs.io/en/latest/logging.html
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discordbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# environment variables are useful for hiding important bits of info like api-tokens
# DOCUMENTATION: https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# load_dotenv() does not overwrite system environment variables, so its safe.
# DOCUMENTATION: https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get('BOT-TOKEN')
GUILD = os.environ.get('BOT-GUILD')
# ugly hack in comparison :(
# read in token from separate file called 'token'
#token = 'the token'
#with open('token','r') as f:
#    token = f.readline()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client), '\nI am in the following servers:')
    for guild in client.guilds:
        if guild == GUILD:
            print(f'{guild}')

@client.event
async def on_message(message):
    # client.user is the bot itself
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)