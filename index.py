import discord
from discord.ext import commands
import random

PREFIX = '$'
#Used to set a prefix
TOKEN = 'TOKEN-HERE'
#Used to set the bot token.

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

@bot.event()
async def on_ready():
    print('==================')
    print('|Basic Discord.PY Bot Example')
    print('|Copyright (C) S4qib')
    print('|Github: https://github.com/S4qib')
    print('==================')
    print('|Bot is ready.')
    print('==================')
    #Basic event to display in the console when the bot is ready
    
@bot.command()
async def test(ctx):
    await ctx.send('Bot is functional!')
    #test command to see  if bot is functional
    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
    #Latency command
    
@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    
    await ctx.send(arg)
    
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, enquiry):
    responses = [  
      "Yes",
      "No",
      "Maybe",
      "Not sure",
      "Absolutley",
      "Nah",
      "Ask me later",
      "Yup",
      "Eh, cant tell."]
    
em = discord.Embed(title = 'The Magic EightBall Answers!',colour = discord.Colour.red())
em.add_field(name=f'**Enquiry:** {enquiry}", value=f"**My outlooks:** {random.choice(responses)}')
em.set_footer(f'Requested by {ctx.author}!')
await ctx.send(embed=em) 
#Magic 8ball command

bot.run(TOKEN)
