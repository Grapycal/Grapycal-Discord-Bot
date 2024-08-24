import discord
from discord.ext import commands, tasks
import aiohttp
import asyncio
from bot import MyBot
import datetime
import asyncio

class Star(commands.Cog):
    def __init__(self, bot:MyBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Star cog loaded.")
        await asyncio.sleep(300)
        await self.check_star.start()

    async def fetch_repos(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.github.com/orgs/grapycal/repos") as response:
                return await response.json()    

    @tasks.loop(minutes=8)
    async def check_star(self):
        repos = await self.fetch_repos()
        for repo in repos:
            if repo["name"] == "Grapycal":
                stars = repo["stargazers_count"]
                star_channel = self.bot.get_channel(1114477938792988723)
                assert isinstance(star_channel, discord.TextChannel)
                await star_channel.edit(name=f"⭐×{stars}")
                current_time_UTC = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
                reflash_time = current_time_UTC + datetime.timedelta(minutes=8)
                await star_channel.edit(topic=f"Each star is a piece of motivation to contributors\nNext refresh: <t:{int(reflash_time.timestamp())}:R> <t:{int(reflash_time.timestamp())}:t>")

async def setup(bot):
    await bot.add_cog(Star(bot))



