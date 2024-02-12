import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
import base64
import json
from datetime import date

load_dotenv()

class moonphase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def moon(self, ctx):
        appID = os.getenv("ASTRONOMY_APP_ID")
        appSecret = os.getenv("ASTRONOMY_APP_SECRET")
        userpass = "{}:{}".format(appID, appSecret)
        authString = base64.b64encode(userpass.encode()).decode()
                
        # sérialization de l'objet JSON envoyé à l'API
        
        headers = {
            'Authorization': f'Basic {authString}',
            'Content-Type': 'application/json'
        }
        
        body = {
            'format': 'png',
            'style': {
                'moonStyle': 'default',
                'backgroundStyle': 'stars',
                'backgroundColor': '#000000',
                'headingColor': '#ffffff',
                'textColor': '#ffffff',
            },
            'observer': {
                'latitude': 48.0,
                'longitude': 2.0,
                'date': date.today().strftime("%Y-%m-%d"),
            },
            'view': {
                'type': 'portrait-simple',
            },
        }
        
        response = requests.post('https://api.astronomyapi.com/api/v2/studio/moon-phase', headers=headers, data=json.dumps(body))
        
        if response.status_code == 200:
            data = response.json()        
            embed=discord.Embed(title="Lune Actuelle", color=0x00ff00)
            embed.set_image(url=data['data']['imageUrl'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Désolé, je n'ai pas pu obtenir la phase de la lune.")
            print("Erreur: ", response.status_code, response.text)
        
        
async def setup(bot):
    try:
        await bot.add_cog(moonphase(bot))
        print("Le cog Moonphase a été chargé avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement du cog Moonphase: {e}")


