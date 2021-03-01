import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role('Script Kiddie')
    async def ping(self, ctx):
        embed = discord.Embed(
            title='Pong!',
            Description='',
            color = discord.Color.green()
        )
        embed.add_field(name='latency', value=f'{round(self.client.latency * 1000)} ms', inline = False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(General(client))