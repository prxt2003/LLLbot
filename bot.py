import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='you L'))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author.name == 'azraxel5':
        await message.channel.send('<@722427790871363584> L')

    if message.author.name == 'Roro' or message.author.name == 'ElectricMercenary':
        await message.channel.send('<@416173367649894400> L')
        await message.delete()

client.run(os.environ['TOKEN'])