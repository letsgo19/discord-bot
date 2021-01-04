import discord
# import os
from discord.activity import Game
from discord.enums import Status
from discord.ext import commands
# from discord.ext.commands.core import bot_has_any_role

# token_path = os.path.dirname(os.path.abspath(__file__))+"/token.txt"
# t = open(token_path,'r',encoding='utf-8')
# token =t.read().split()[0]

game = discord.Game('!Hello')

client = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game,help_command=None)


@client.event
async def on_ready():
    await client.change.presence(Status.discord.Status.online, activity=Game)
    print('I am ready')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None


    if  message.content ==('!hi'):
        await message.channel.send('응답')
        await message.author.send('응답')

client.run('Nzk0NzQzNTMwMDU2MDU2ODYz.X-_Qlw.40HmvhMniORauq4rJOvR4qP9ZlI')
