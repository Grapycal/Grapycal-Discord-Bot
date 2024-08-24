import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot
import requests
import discordoauth2
import json

class Linked_Role(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        with open("not_token.json", mode="r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        secret=jdata["secret"]
        token=jdata["TOKEN"]
        self.client = discordoauth2.Client(1170736785098285106, secret=secret, redirect="http://45.32.52.126:2048/oauth2", bot_token=token)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Linked Role cog loaded.")

    @app_commands.command(name="update_linked_roles_metadata")
    async def update_linked_roles_metadata(self, interaction: discord.Interaction):
        if interaction.user.id != 1022080471506624545:
            await interaction.response.send_message("You are not the owner of this bot.", ephemeral=True)
            return
        response =  self.client.update_linked_roles_metadata([
            {
                "type": 7,
                "key": "contributor",
                "name": "Contributor",
                "description": "Must have contributed to the Grapycal"
            }
        ])
        print(response.content)
        await interaction.response.send_message("Linked roles metadata updated.", ephemeral=True)

async def setup(bot: MyBot):
    await bot.add_cog(Linked_Role(bot))