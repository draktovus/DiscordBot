import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # client.user is the bot itself
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NDY4OTc3NjE5MTM2ODA2OTEy.W06vcQ.QR_5vMb-NP146j-IMQ2eDMBGYrs')