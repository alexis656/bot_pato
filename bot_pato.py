import discord
from discord.ext import commands
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

# Lista de nombres de archivos de memes (sin extensiones)
meme_list = ["meme1", "meme2"]

@bot.command()
async def meme(ctx):
    img_name = random.choice(meme_list)  # Elige un nombre de archivo al azar
    with open(f'imagen/{img_name}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
meme_futbol = ["meme3", "meme4","meme5"]

@bot.command()
async def memefut(ctx):
    img_name2 = random.choice(meme_futbol)  # Elige un nombre de archivo al azar
    with open(f'imagen/{img_name2}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run("MTE1NTIwMTc5ODI0MDQ4NTUyNg.GbtSCF.fh8-kWOvc6nptU5pQOIDYYixby2F1cQt2rfuD0")
