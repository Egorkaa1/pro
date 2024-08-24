import discord
from discord.ext import commands
import os
import random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)


@bot.event
async def on_ready():
    print(f'Подключен {bot.user}')


@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def h(ctx):
    await ctx.send('''Глобальное потепление это — долгосрочное повышение средней температуры климатической системы Земли,
     происходящее уже более века, основной причиной чего, по мнению подавляющего большинства учёных, является человеческая деятельность''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def mems(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def nick(ctx):
    await ctx.send(f'My nickname is {bot.user}')

@bot.command("dog")
async def dog(ctx):
    '''По команде duck вызывает функцию get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Сохранили картинку в ./{attachment.filename}")
    else:
        await ctx.send("Вы забыли загрузить картинку :(")


    


bot.run("MTIwODc0NzA2MTc2NDE2NTY2Mg.Gi_jMq.mRPTyMnvF9sCv1Fe81g2FjGLTwMCLM049-d3Ms")
