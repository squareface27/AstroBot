import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class day(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def day(self, ctx):
        NASA_API_KEY = os.getenv("NASA_API_KEY")
        response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
        data = response.json()
        embed = discord.Embed(title=data['title'], description=data['explanation'], color=0x00ff00)
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)

async def setup(bot):
    try:
        await bot.add_cog(day(bot))
        print("Le cog Day a été chargé avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement du cog Day: {e}")


