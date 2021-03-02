import discord
from discord.ext import commands
from discord.utils import get

import os

client = commands.Bot(command_prefix='.')


def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename}')


def unload():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to unload {filename}')


@client.event
async def on_ready():
    print('Starting {0.user}'.format(client))


@client.command()
@commands.has_any_role("Functional Purity", "Elite Hacker")
async def reload(ctx):
    unload()
    load()
    embed = discord.Embed(
        title='Reloaded extensions',
        Description='',
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)


load()

token = os.environ.get('TOKEN')

client.run(token)
