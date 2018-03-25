import discord
from discord.ext import commands
import asyncio
import json
import datetime

with open('./config.json','r') as c_json:
    config = json.load(c_json)
c_json.close()

desc = '''katy bot'''
prefix = '!'
bot = commands.Bot(command_prefix = prefix, description = desc)

cogs = [
    'cogs.fortnite',
    'cogs.vote',
    'cogs.random',
]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(cog, type(e).__name__, e))

@bot.event
async def on_ready():
    for server in bot.servers:
        print("[{}] has started in server [{}] with [{:,}] members.".format(
        bot.user.name, server.name, server.member_count))


bot.run(config['disc']['token'])
