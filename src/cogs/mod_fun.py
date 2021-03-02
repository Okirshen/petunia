import discord
from discord.ext import commands

class Mod_Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Integral's Leet Role")
    async def say(self, ctx, *, message):
        await ctx.channel.purge(limit = 1) 
        await ctx.send(f'{message}')

def setup(client):
    client.add_cog(Mod_Fun(client))