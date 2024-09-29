import os
from discord import Intents, Client, Message, user 
from dotenv import load_dotenv
from responses import get_response


load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
#print(TOKEN)

intents = Intents.default()
intents.message_content = True

client = Client(intents = intents)

async def send_message(message, user_message) -> None:
    if not user_message:
        print('Message was empty because intents were not enable properly')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is active now')

@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
