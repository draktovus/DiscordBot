import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discordbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Load environment vars using a library
load_dotenv()
TOKEN = os.environ.get('BOT-TOKEN')
GUILD = os.environ.get('BOT-GUILD')

# Create the bot client class
bot = commands.Bot(command_prefix='!', 
        description='My prefix is \'!\'.', 
        owner_id=91253654056624128,
        activity=discord.CustomActivity(name='Doing maid things!'))

# This is how to get a different function name from the command
@bot.command(name='copycat')
async def test(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

@bot.event
async def on_ready():
    bot_status = discord.Activity(name="you. 😊", type=discord.ActivityType.watching)
    await bot.change_presence(activity=bot_status, status=discord.Status.idle)
    print('Logged in as {0.user}'.format(bot), '\nMy master\'s guild is:')
    for guild in bot.guilds:
        if guild.name == GUILD:
            print(f'{guild}')

# add new commands, can only do it once
try:
    bot.add_command(test)
except Exception as e:
    print(e)
bot.run(TOKEN)