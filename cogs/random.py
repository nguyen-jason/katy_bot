import discord
from discord.ext import commands
import aiohttp
import datetime

class Random:
    def __init__(self, bot):
        """Random Shit"""
        self.session = aiohttp.ClientSession(loop=bot.loop)
        self.bot = bot
        self.start_time = datetime.datetime.now()
        print('Cog "{}" loaded.'.format(self.__class__.__name__))


    @commands.command()
    async def babypics(self, *args):
        await self.bot.say("https://imgur.com/a/a5eyO")

    def timedelta_str(self, dt):
        days = dt.days
        hours, r = divmod(dt.seconds, 3600)
        minutes, sec = divmod(r, 60)

        if minutes == 1 and sec == 1:
            return '{0} days, {1} hours, {2} minute and {3} second.'.format(days,hours,minutes,sec)
        elif minutes > 1 and sec == 1:
            return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days,hours,minutes,sec)
        elif minutes == 1 and sec > 1:
            return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days,hours,minutes,sec)
        else:
            return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days,hours,minutes,sec)


    @commands.command()
    async def uptime(self):
        """Displays bot uptime."""
        await self.bot.say(self.timedelta_str(datetime.datetime.now() - self.start_time))


def setup(bot):
    bot.add_cog(Random(bot))
