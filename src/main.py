import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Starting {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')
    await ctx.send('Pong!')

@client.command(aliases = ['purge'])
async def clear(ctx, amount = 1):
    if amount > 0:
        await ctx.channel.purge(limit = amount + 1)   
        await ctx.send('Purged ' + str(amount) + ' messages successfully.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await  member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await  member.ban(reason = reason)

token = os.environ.get('TOKEN')

client.run(token)