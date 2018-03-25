import discord
from discord.ext import commands
import json
import aiohttp
import datetime

# GET https://api.fortnitetracker.com/v1/profile/{platform}/{epic-nickname}

class Fortnite:
    def __init__(self, bot):
        """Gets data from fortnitetracker.com"""
        
        with open('./config.json', 'r') as c_json:
            config = json.load(c_json)
        c_json.close()

        self.session = aiohttp.ClientSession(loop=bot.loop)
        self.bot = bot
        self.url = config['ft']['url']
        self.header = {"TRN-Api-Key" : config['ft']['key']}
        print('Cog "{}" loaded.'.format(self.__class__.__name__))


    @commands.cooldown(1, 2.0, commands.BucketType.default)
    @commands.command()
    async def lifestats(self, user_id, platform):
        """{player} {platform}"""
        async with aiohttp.get(self.url + platform.lower() + '/' + user_id.lower(), headers = self.header) as r:
            if r.status == 200:
                js = await r.json()
            else:
                await self.bot.say("Error connecting to fortnitetracker.com")
                return
        
        # checks if fortnitetracker.com tells us if we hit our rate limit
        # which shouldn't happen because we have a cooldown on the command
        # but if it does, we respect it
        if int(r.headers['X-Ratelimit-Remaining-Minute']) <= 0:
            await self.boy.say("Hit ratelimit unexpectedly... Try again in a minute")
            return

        if len(js) < 2:
            await self.bot.say("Player not found.")
        else:
            lines = []
            for i in js['lifeTimeStats']:
                lines.append(i['key'] + ": " + i['value'])

            embed = discord.Embed()
            embed.title = "{}'s Lifetime Statistics in Fortnite ({})".format(user_id, platform.lower())
            embed.description = '\n'.join(lines)
            embed.color = 4915330
            footer_text = "fortnitetracker.com/profile/" + platform + "/" + user_id
            embed.set_footer(text = footer_text, icon_url = 'https://i.imgur.com/7fCOdEO.png')
            await self.bot.say(embed = embed)
    

def setup(bot):
    bot.add_cog(Fortnite(bot))
