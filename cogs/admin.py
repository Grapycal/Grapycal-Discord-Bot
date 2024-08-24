import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot


class Admin(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin cog loaded.")

    @commands.is_owner()
    @commands.command()
    async def sync(self, ctx: commands.Context):
        app_commands = await self.bot.tree.sync()
        await ctx.reply(f"synced {len(app_commands)} commands")

async def setup(bot):
    await bot.add_cog(Admin(bot))
