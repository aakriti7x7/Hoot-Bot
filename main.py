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
client.run('ODU0MDM5NzgwMTM1MjcyNDY4.YMeIhg.r9x1axXQ57vojllfMq0-DTUwLmo')






  


# @client.command(aliases =["c"])
# async def countdown(ctx, tim = 2):
#   message = await ctx.send(f'**Timer: 0{tim} : 00**')
#   tim = tim*60
#   while tim!=0:
#     time.sleep(5)
#     tim = tim - 5
#     if(tim>=60):
#       min=math.floor(tim/60)
#       sec= tim - min*60

#     await message.edit(content= f'**Timer: 0{min} : {sec} **')





      

#yeloooooooooooooooooooooooooooooooooooooo

# message = await ctx.send(f'**Timer: 0{min} : 00**')

# await message.edit(content= f'**Timer: 00 : 00 **' )




'''
while (time != 0)

time.sleep(5s)
await ctx.send


'''


"Impact of COVID-19 (Coronavirus) on Global economy"
"How prepared is India to tackle the COVID-19 outbreak?"
" Farm Bills 2020 – Pros, Cons & Challenges"
# Lessons for the world from COVID-19 pandemic
# Atmanirbhar Bharat Abhiyan
# National Education Policy 2020
# National Recruitment Agency – Pros & Challenges
# National Health ID – Pros, Cons & Challenges
# How to revive Indian economy?
# Ban on Chinese Apps in India
# E-learning – Pros & Challenges
# E-Learning: A substitute for classroom learning?
# Work from home – Pros & Cons
# Balance between Profession and Family
# Private trains in India – Benefits & Challenges
# How will 2020 shape 2021?
# Impact of Coronavirus/COVID-19 on Environment
# Union Budget – 2020-21
# Does Nepotism exist in Bollywood?
# Should mother tongue be the medium of instruction in schools?
# Data Localisation – Benefits & Challenges
# Bad bank – Is it a good idea?
# India-China relations
# Affordable Healthcare in India
# Commercialization of health care : Good or Bad ?
# Digital payments in India
# Ever growing air pollution levels – Where does the problem lie?
# How can we deal with increasing Cyber Crimes?
# Censorship of Web series – Pros & Cons
# # Unemployment in India
# How to prevent COVID third wave in India?
# Net Zero
# Biomedical waste crisis
# Post-Covid world
# Impact of COVID-19 on Indian economy
# India’s COVID-19 vaccination program
# The second wave of COVID-19
# Development Finance Institution
# How can we prevent the next pandemic?
# Union Budget 2021-22
# The Future of Artificial Intelligence
# Impact of COVID-19 on the education sector
# The Future of work
# Quad
# The rise of the Gig economy
# Is the United Nations still relevant?
# Farm Bills 2020 – Pros, Cons & Challenges
# National Recruitment Agency – Pros & Challenges
# National Education Policy 2020
# Atmanirbhar Bharat Abhiyan
# Open book exams – Pros, Cons & Challenges
# National Health ID – Pros, Cons & Challenges
# How to revive Indian economy?
# E-learning – Pros & Challenges
# Private trains in India – Benefits & Challenges
# How will 2020 shape 2021?
# Ban on Chinese Apps in India
# Lessons for the world from COVID-19 pandemic
# Impact of Coronavirus/COVID-19 on Environment
# How prepared is India to tackle the COVID-19 outbreak?
# Impact of COVID-19 on Global economy
# RBI’s surplus transfer to the government
# Can India become a $5 trillion economy by 2024?
# Bifurcation of Jammu & Kashmir
# Crisis in the Automobile Industry
# UAPA (Amendment) Bill, 2019
# Union Budget – 2019-20
# Syrian crisis
# Data Localisation – Benefits & Challenges
# Can illiterates be given driving licenses?
# Electric vehicles in India
# Shanghai Cooperation Organisation
# Changing relation between India and Bangladesh
# ‘Neighbourhood First’ policy
# BIMSTEC
# Does “NOTA” option in elections really make sense?
# Major challenges for the Modi government 2.0
# Mechanisms adopted to combat terrorism
# Should Andhra Pradesh be given Special Category Status?
# Defence Budget 2019-20
# BRICS
# Why Indian PSUs are in losses?
# National Register of Citizens – Merits & Demerits
# Abrogation of Article 370
# Mission Shakti – India’s Anti-satellite missile test
# Jet Airways Crisis
# NYAY – Can it eliminate poverty?
# India-China relations
# India’s fight against Terrorism | Pulwama Terror attacks
# 5 years of Modi government
# Interim Budget 2019 – Analysis
# Brexit – Impact on India?
# Citizenship (Amendment) Bill
# Universal Basic Income – Pros & Cons
# G20 – GD Topic
# Surrogacy (Regulation) Bill – GD Topic
# Is RBI’s Autonomy Under Threat?
# Gene-edited babies project – Pros & Cons
# RBI Vs Govt
# Blockchain Technology – Pros & Cons
# Statue of unity – GD Topic
# Ayushman Bharat – Will it achieve Universal Health coverage in India?
# Sabarimala verdict – Progressive OR a threat to traditions?
# #MeToo – GD Topic
# Decriminalization of Homosexuality – Road ahead for LGBTQ community of India
# Social Media – Impact on human behavior and society
# India-US relations – Impact of Trump
# One year of GST
# Relevance of WTO in today’s global scenario
# Plastic Pollution
# Facebook – Cambridge Analytica data scandal
# EU’s GDPR – Impact on India
# Flipkart-Walmart deal – Impact on India
# US withdrawal from Iran nuclear deal – Impact on India
# High fuel prices in India – What are the causes?
# Can ‘Death penalty’ deter child rapes?
# Exam paper leaks – How to restore trust in the Indian education system?
# US-China Trade war – Impact on USA, China & other countries
# Who have more chances of winning 2019 Lok Sabha elections?
# Private Universities in India – Pros and Cons
# How can banks prevent Nirav Modi-Like scams?
# Impact of Brexit on Indian Economy
# Should both developed and underdeveloped countries have equal binding in combating climate change?
# Should Uniform Civil Code be implemented?
# Cauvery River Dispute
# Significance of BRICS in world economy
# Beti Bachao Beti Padhao – a success?
# E-Commerce – Sustainable business model?
# Delhi’s Odd-Even Rule : a success?
# Corruption in India
# Challenges to Indian Banking sector
# Donald Trump’s Presidency – Pros & Cons
# Artificial intelligence (AI) – Pros & Cons
# Big Data – Pros & Cons
# Bullet trains in india – Is it a right step?
# Should India accept Rohingya refugees?
# Crimes against women in India
# New India 2022 – Will it be a reality?
# How to eliminate the threat of Nuclear war?
# Drug menace – How to fight with it?
# Can we rely on Cryptocurrencies like Bitcoin?
# How to tackle Naxalism?
# Impact of GST on Indian Economy
# Should Gorkhaland be given separate state status?
# How to reduce NPA?
# ‘Digital India’ – How far was it a success?
# Is India becoming intolerant?
# Is GST beneficial for the common man?
# Should Triple Talaq be abolished?
# Privatization of ‘Air India’ – Good or Bad?
# One Belt One Road – Impact on India
# Can ‘One Belt One Road’ improve developing world?
# Why are many startups failing in India?
# Union Budget 2017-18 – Is it beneficial for the common man?
# Union Budget just before Assembly Elections – Is it a Fair Move?
# Unique identification number for every Indian
# Donald Trump Presidency – Impact on the world
# Should India be given a permanent seat in UNSC?
# Should mother tongue be the medium of instruction in schools?
# Aadhaar Act
# Depreciation of Indian Rupee
# Is WikiLeaks a bane or a boon?
# Nuclear Energy in India – Boon or Bane?






#NICCHE CODE HAI!!!


#CODE H BAKA




#ORREY ORREY






























""""



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



"""