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
@commands.has_any_role("Functional Purity", "Elite Hacker")
async def clear(ctx, amount = 1):
    if amount > 0:
        await ctx.channel.purge(limit = amount + 1)   
        await ctx.send(f'Purged {amount} messages successfully.')

@client.command()
@commands.has_any_role("Functional Purity", "Elite Hacker")
async def kick(ctx, member : discord.Member, *, reason = None):
    await  member.kick(reason = reason)

@client.command()
@commands.has_any_role("Functional Purity", "Elite Hacker")
async def ban(ctx, member : discord.Member, *, reason = None):
    await  member.ban(reason = reason)

@client.command()
@commands.has_any_role("Functional Purity", "Elite Hacker")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discrinator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discrinator}')
            return

token = os.environ.get('TOKEN')

client.run(token)