import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Activer tous les intents disponibles
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

async def load_extensions():
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.commands.{filename[:-3]}")
            print(f'{filename} chargé avec succès.')
            
if __name__ == "__main__":
    asyncio.run(load_extensions())
    bot.run(TOKEN)