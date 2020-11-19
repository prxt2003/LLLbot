import discord
import os

client = discord.Client()


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f'Hi {member.name}, in this server, I take executive decisions')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='you L'))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author == 'azraxel5':
        await message.channel.send('<@722427790871363584 L')

    if message.author == 'ElectricMercenary':
        await message.channel.send('<@416173367649894400 L')

client.run(os.environ['TOKEN'])