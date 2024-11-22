import discord
from discord.ext import commands
#from keep_alive import keep_alive
import random


client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

meow_enabled = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  
    global meow_enabled 
  
    if message.author == client.user:
        return

    if message.content.startswith('$meow_turn_off'):
      meow_enabled = False
      await message.channel.send('Meow功能已經關閉')
    elif message.content.startswith('$meow_turn_on'):
      meow_enabled = True
      await message.channel.send('Meow功能已經開啟')
    else:
      if meow_enabled == True:
        meows = ['Meow!' for _ in range(random.randint(1, 15))]
        await message.channel.send(' '.join(meows))
      await client.process_commands(message)



@client.command(help="Say Hi", brief="Say Hi")
async def hi(ctx):  
  await ctx.send('hihi!')


# 啟動 Bot
# If you don't have your own machine that is always on, you have to turn the third line and below on and search the turorial about that.
#keep_alive()
client.run('TOKEN')