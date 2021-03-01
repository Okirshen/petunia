import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def purge(self, ctx, amount = 1):
        embed = discord.Embed(
            title='Purge',
            Description='',
            color = discord.Color.green()
        )
        if amount > 0:
            await ctx.channel.purge(limit = amount + 1) 
            if amount > 1:  
                embed.add_field(
                    name=f'Successfully purged {amount} messages', 
                    value=f'Action executed by {ctx.author.mention}', 
                    inline = False
                )
            else:
                embed.add_field(
                    name='Successfully purged message', 
                    value=f'Action executed by {ctx.author.mention}', 
                    inline = False
                )
        else:
            await ctx.channel.purge(limit = 1)
            embed.add_field(
                name=f'ERROR! Could not purge {amount} messages', 
                value=f'Action executed by {ctx.author.mention}', 
                inline = False
            )
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        if member != self.client:
            await member.send(f'You have been kicked for the following reason(s):\n\t{reason}')
            await member.kick(reason = reason)
            await ctx.channel.purge(limit = 1) 

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        if member != self.client:
            await member.send(f'You have been banned for the following reason(s):\n\t{reason}')
            await member.ban(reason = reason)
            await ctx.channel.purge(limit = 1) 

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return
 
    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

def setup(client):
    client.add_cog(Moderation(client))