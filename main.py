from keep_alive import keep_alive

import discord
from discord.ext import commands, tasks
from database import *
from allmotion import motions,shipwrecks,turncoat_devil,jams
import time
import random
import math
import requests
import json

intents = discord.Intents(messages = True , guilds = True ,  reactions = True , members = True , presences = True)
client  = commands.Bot(command_prefix = "*", intents = intents)



@client.event
async def on_ready():
  print('yo m here')

# general debated

@client.command(aliases = ["m"])
async def motion(ctx):
  await ctx.send(random.choice(motions))

# shipwreck

@client.command(aliases = ["sw","s"])
async def shipwreck(ctx):
  await ctx.send(random.choice(shipwrecks))

#turncoat_devil

@client.command(aliases = ["t","td","d","a"])
async def tda(ctx):
  await ctx.send(random.choice(turncoat_devil))

#jam

@client.command(aliases = ["j"])
async def jam(ctx):
  await ctx.send(random.choice(jams))


keep_alive()
client.run('ODU0MDM5Nzgfhhhhhhhhjfygjggvchgjfj7vojllfMq0-DTUwLmo') 
# not my Token DuH






  


@client.command(aliases = ["timer" , "stopwatch" , "clock" , "time" , "watch" , "minutes" , "sw"] )
async def st(ctx , min = 2):
  #yooo!!!
  t = 60
  message = await ctx.send(f'**Timer: 0{min} : 00**')
  min = min - 1
  while min >= 0:
    time.sleep(5)

    if t == 60:
      await message.edit(content= f'**Timer: 0{min} : 55 **' )


    elif t >= 10:
      await message.edit(content= f'**Timer: 0{min} : {t} **' )
    elif (t <= 10 and t >= 0):
      await message.edit(content= f'**Timer: 0{min} : 0{t} **' )

    t = t - 5

    if t == 0 and min >= 0:
      t=60
      min = min-1
      time.sleep(5)
    if min < 0:
      print (min)
      await message.edit(content= f'**Timer: 00 : 00 **' )
      time.sleep(1)  
      await ctx.send("**TIMES UP!!**")  



  # EXTRA TIME


@client.command(aliases = ["extra","extratime","moretime","more","increase","inc","xtra"])
async def et(ctx , secs = 30):
  if secs == 1:
    message = await ctx.send(f'EXTRA TIME OF {secs} second HAVE BEEN ADDED')

  else:
    message = await ctx.send(f'EXTRA TIME OF {secs} seconds HAVE BEEN ADDED')
  while secs >= 0:
    await message.edit(content= f'**Time Left : {secs} seconds **')
    time.sleep(5)
    secs = secs - 5
    while secs <= 5 :
      if secs > 1:
        await message.edit(content= f'**Time Left : {secs} seconds **')
        time.sleep(1)
      elif secs == 1:
        await message.edit(content= f'**Time Left : {secs} second **')
        time.sleep(1)
      secs = secs-1
      if secs == 0:
        await message.edit(content= f'**Time Left : {secs} seconds **')
        await ctx.send("***EXTRA TIME IS UP!!***")
        secs = -1
        break

