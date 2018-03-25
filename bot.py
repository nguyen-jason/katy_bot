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

    #embed = discord.Embed(color = 6592175)
    #embed.title = 'katybot'
    #embed.description = "like a paper bag..."
    #embed.timestamp = datetime.datetime.utcnow()
    #embed.set_image(url = "https://i.imgur.com/DlWek4q.jpg")
    #await bot.send_message(discord.Object(id='277385875183370260'),embed=embed)


bot.run(config['disc']['token'])
