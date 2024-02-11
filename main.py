import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Activer tous les intents disponibles
intents = discord.Intents.all()

# Créer une instance du bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

# Exécuter le bot avec votre token de bot
bot.run(TOKEN)
