import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def purge(self, ctx, amount=1):
        embed = discord.Embed(
            title='Purge',
            Description='',
            color=discord.Color.green()
        )
        if amount > 0:
            await ctx.channel.purge(limit=amount + 1)
            if amount > 1:
                embed.add_field(
                    name=f'Successfully purged {amount} messages',
                    value=f'Action executed by {ctx.author.mention}',
                    inline=False
                )
            else:
                embed.add_field(
                    name='Successfully purged message',
                    value=f'Action executed by {ctx.author.mention}',
                    inline=False
                )
        else:
            await ctx.channel.purge(limit=1)
            embed.add_field(
                name=f'ERROR! Could not purge {amount} messages',
                value=f'Action executed by {ctx.author.mention}',
                inline=False
            )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.purge(limit=1)
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted User Role')
        embed = discord.Embed(
            title='Mute',
            Description='',
            color=discord.Color.green()
        )

        mem_roles = member.roles

        can_ban = True
        for role in mem_roles:
            if (str(role) == "Functional Purity") or (str(role) == "Elite Hacker"):
                can_ban = False
                break

        print(can_ban)

        if ((member != self.client) or (member != ctx.author)) and can_ban:
            for role in mem_roles[1:]:
                await member.remove_roles(role)
            await member.add_roles(mute_role)
            embed.add_field(
                name='You have been muted for the following reason(s):',
                value=f'{reason}',
                inline=False
            )

        elif not can_ban:
            embed.add_field(
                name='Mute Failure',
                value='You cannot be muted another admin.',
                inline=False
            )

        await member.send(embed=embed)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='Kick',
            Description='',
            color=discord.Color.green()
        )

        mem_roles = member.roles

        can_ban = True
        for role in mem_roles:
            if (str(role) == "Functional Purity") or (str(role) == "Elite Hacker"):
                can_ban = False
                break

        if ((member != self.client) or (member != ctx.author)) and can_ban:
            embed.add_field(
                name='You have been kicked for the following reason(s):',
                value=f'{reason}',
                inline=False
            )
            await member.send(embed=embed)
            await member.kick(reason=reason)
        elif not can_ban:
            embed.add_field(
                name='You have been attempted to be kicked',
                value='Kick unsuccessful because you have an admin role',
                inline=False
            )
            await member.send(embed=embed)



    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='Ban',
            Description='',
            color=discord.Color.green()
        )

        mem_roles = member.roles

        can_ban = True
        for role in mem_roles:
            if (str(role) == "Functional Purity") or (str(role) == "Elite Hacker"):
                can_ban = False
                break

        if ((member != self.client) or (member != ctx.author)) and can_ban:
            embed.add_field(
                name='You have been banned for the following reason(s):',
                value=f'{reason}',
                inline=False
            )
            await member.send(embed=embed)
            await member.ban(reason=reason)
        elif not can_ban:
            embed.add_field(
                name='You have been attempted to be banned',
                value='Ban unsuccessful because you have an admin role',
                inline=False
            )
            await member.send(embed=embed)

    @commands.command()
    @commands.has_any_role("Functional Purity", "Elite Hacker")
    async def unban(self, ctx, *, member):
        embed = discord.Embed(
            title='Removed Ban',
            Description='',
            color=discord.Color.green()
        )
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        embed.add_field(
            name=f'{member_name}#{member_discriminator} has been unbanned.',
            value='',
            inline=False
        )

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.purge(limit=1)
                await ctx.send(embed=embed)
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
