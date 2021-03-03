import discord
from discord.ext import commands


def log(log_type, description, ctx):
    embed = discord.Embed(
        title='',
        Description='',
        color=discord.Color.green()
    )
    embed.add_field(
        name=f'{log_type}',
        value=f'{description}',
        inline=False
    )
    embed.add_field(
        name='Moderation Fun Commands',
        value=f'Action executed by {ctx.author.mention}',
        inline=False
    )
    return embed


class Mod_Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.log_channel = self.client.get_channel(816467665128259614)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def say(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{message}')
        embed_log = log('Say', f'{message}', ctx)
        await self.log_channel.send(embed=embed_log)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def spam(self, ctx, repeat, *, message):
        spammed = 0
        role = []
        for i in ctx.author.roles:
            role.append(str(i))
        await ctx.channel.purge(limit=1)
        if "Integral's Leet Role" in role:
            spammed = int(repeat)
            for i in range(0, int(repeat)):
                await ctx.send(f'{message}')
        elif int(repeat) > 10:
            spammed = 10
            for i in range(0, 10):
                await ctx.send(f'{message}')
        else:
            spammed = int(repeat)
            for i in range(0, int(repeat)):
                await ctx.send(f'{message}')
        embed_log = log(f'Spam {spammed}', f'{message}', ctx)
        await self.log_channel.send(embed=embed_log)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def bean(self, ctx, member : discord.Member):
        bean_link = 'https://media.discordapp.net/attachments/453226342843023390/721830901004369991/You_have_been_Beaned.gif'
        await ctx.channel.purge(limit=1)

        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        embed.add_field(
            name=f'You Have Been BEANED!',
            value='Bean Bean Bean Bean Bean',
            inline=False
        )
        embed.set_image(url=bean_link)
        embed.add_field(
            name=f'Be on your best behavior from now on!',
            value=f'executed by {ctx.author.mention}',
            inline=False
        )

        await ctx.channel.send(embed=embed)

    # Error checking
    ###################################################################################################################

    @say.error
    async def say_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        if (error, commands.MissingRequiredArgument):
            embed.add_field(
                name=f'Error!',
                value='Missing argument: check help for proper usage',
                inline=False
            )

        await ctx.channel.send(embed=embed)

    @spam.error
    async def spam_parse_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        if (error, commands.ArgumentParsingError):
            embed.add_field(
                name=f'Error!',
                value='Invalid argument: check help for proper usage',
                inline=False
            )

        await ctx.channel.send(embed=embed)

    @spam.error
    async def spam_args_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        if (error, commands.MissingRequiredArgument):
            embed.add_field(
                name=f'Error!',
                value='Missing argument(s): check help for proper usage',
                inline=False
            )

        await ctx.channel.send(embed=embed)

    @bean.error
    async def bean_parse_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        if (error, commands.ArgumentParsingError):
            embed.add_field(
                name=f'Error!',
                value='Invalid argument: check help for proper usage',
                inline=False
            )

        await ctx.channel.send(embed=embed)

    @bean.error
    async def bean_args_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='',
            Description='',
            color=discord.Color.green()
        )
        if (error, commands.MissingRequiredArgument):
            embed.add_field(
                name=f'Error!',
                value='Missing argument(s): check help for proper usage',
                inline=False
            )

        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Mod_Fun(client))
