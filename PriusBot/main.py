import discord
import random
import os
import asyncio 
from discord.ext import commands, tasks
from dotenv import load_dotenv
load_dotenv()
bot = commands.Bot(command_prefix="=")


#ping
@bot.command()
async def ping(ctx):
    await ctx.channel.send(f'***Pong!*** Latency: {round(bot.latency *1000)}ms')

#prius
@bot.command()
async def prius(ctx):
    embed = discord.Embed(title = "about the prius:", description = "Hello, i am the toyota Prius. The hated hybrid by Toyota.")
    await ctx.channel.send(embed = embed)

#scenario
@bot.command()
async def scenario(ctx):
    embed = discord.Embed(title = "current scenario:", description = "Cars behind the Prius are angry, they are honking and screaming out of their windows because of the slow Prius.", color = (0xF85252))
    await ctx.send(embed = embed)

#speed
@bot.command(pass_conext = True)
async def speed(ctx):
    embed = discord.Embed(title = "Speed of the Prius (km/h) ", description = (random.randint(1, 30)), color = (0xF85252))
    await ctx.send(embed = embed)


#average consumption
@bot.command(pass_conext = True)
async def consumption(ctx):
    embed = discord.Embed(title = "Average fuel consumption (l/100km), the Prius is driving too slow to take up more than 7l/100km ", description = (random.randint(2, 7)), color = (0xF85252))
    await ctx.send(embed = embed)

#battery health
@bot.command()
async def battery(ctx):
    embed = discord.Embed(title = "The battery health of the Prius", description = "Bad, your prius needs to service the battery, even though it is only one year old.",  color = (0xF85252))
    await ctx.send(embed = embed)
#eco
@bot.command()
async def eco(ctx):
    embed = discord.Embed(title = "The eco status of the Prius", description = "The prius is pretty eco friendly, with low average fuel consumption and a really slow electric motor but it doesn't matter anyways because you still need to buy gas and the parts are shipped scross the world to produce the prius anyway!",  color = (0xF85252))
    await ctx.send(embed = embed)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Connected as {bot.user.id}!')



bot.run(os.getenv('TOKEN'))