

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='_')

@bot.event
async def on_ready():
    print ("Jsem ready hochu")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Porn!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))
    
@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("Sup.") 

@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("Yes, I'm here but my owner cannot work on me right now")
    
bot.run("NDY1MjI5MDc4MTQ5MDcwODcw.DiKd3g.z1EtK8yTxNn9kHyUuNwRNUQbS1Y")