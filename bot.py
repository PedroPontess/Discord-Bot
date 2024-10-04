import discord
from discord import Intents
from responses import get_response
from discord.ext import commands

intents = Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents = intents)

async def send_message(message, user_message: str) -> None:
    if not user_message:
        print('Message was empty.')
        return

    is_private = user_message.startswith('?')  
    if is_private:
        user_message = user_message[1:] 

    try:
        response = get_response(user_message)  
        if is_private:
            await message.author.send(response)  
        else:
            await message.channel.send(response)  
    except Exception as e:
        print(f"Error sending message: {e}")

@bot.event
async def on_ready():
    print(f'{bot.user} is active and connected!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    if not user_message.startswith("!"):
        await send_message(message, user_message)

    await bot.process_commands(message)

### MODERATION COMMANDS ###
@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kick a member from the server."""
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} has been kicked for: {reason}')


@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """Ban a member from the server."""
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been banned for: {reason}')


@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: int):
    """Unban a user from the server by their unique username"""
    banned_users =ctx.guild.bans()

    async for ban_entry in banned_users:
        user = ban_entry.user
        if (user.id):
            print(user.id)
        if user.id == member:
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name} has been unbanned.')
            return
    await ctx.send(f'User {member} was not found in the ban list.')


@bot.command(name='mute')
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    """Muted a member by adding a 'Muted' role.."""
    
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')

    if not mute_role:
        mute_role = await ctx.guild.create_role(name='Muted')

        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.set_permissions(mute_role, send_messages=False)
            if isinstance(channel, discord.VoiceChannel):
                await channel.set_permissions(mute_role, speak=False)
    await member.add_roles(mute_role, reason=reason)
    await ctx.send(f'{member.mention} has been muted for: {reason}')


@bot.command(name='unmute')
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    """Unmute a member by removing the 'Muted' role."""
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(mute_role)
    await ctx.send(f'{member.mention} has been unmuted.')

@bot.event
async def on_command_error(ctx, error):
    """Handles missing permissions or other command errors."""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to run this command.")
    else:
        raise error
