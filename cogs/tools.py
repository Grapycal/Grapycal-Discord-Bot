import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot


class Main(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Main cog loaded.")

    @app_commands.command(name="ping", description="check ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"pong ({round(self.bot.latency*1000)}ms)")        

async def setup(bot):
    await bot.add_cog(Main(bot))
