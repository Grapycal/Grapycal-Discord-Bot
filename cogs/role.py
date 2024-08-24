import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot
import requests
import discordoauth2
import json

class Role(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        with open("not_token.json", mode="r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        secret=jdata["secret"]
        self.client = discordoauth2.Client(1170736785098285106, secret=secret, redirect="http://45.32.52.126:1024/oauth2")
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Role cog loaded.")
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id != 1198502988709380146:
            return
        user_id = message.content.removeprefix("contributor: ")
        guild = self.bot.get_guild(1094532480721236041)
        role = discord.utils.get(guild.roles, id=1195357965033676830)
        try:
            user_id = int(user_id)
            member = guild.get_member(user_id)
            if role in member.roles:
                return
            else:
                await member.add_roles(role)
                thread = await self.bot.fetch_channel(1198283704758456330)
                await thread.send(f"{member.mention} got the contributor role!")
        except:
            await message.delete()
    
        
async def setup(bot: MyBot):
    await bot.add_cog(Role(bot))