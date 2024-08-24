import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot

class Welcome(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome cog loaded.")
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(1175494166092972142)
        if member.guild.id == 1094532480721236041:
            embed = discord.Embed()
            embed.title = f"Welcome to Grapycal, {member.name}!"
            embed.description = "This is the official server for the Grapycal programming language. Have fun!"
            embed.color = discord.Color.green()
            message = await channel.send(embed=embed)
            await message.add_reaction("👋")

async def setup(bot: MyBot):
    await bot.add_cog(Welcome(bot))