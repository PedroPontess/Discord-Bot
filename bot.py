import discord
from discord import Intents
from responses import get_response

intents = Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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

@client.event
async def on_ready():
    print(f'{client.user} is active and connected!')

# When a message is sent in a channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')  
    await send_message(message, user_message) 

