import os
from dotenv import load_dotenv
from bot import bot
#from bot import client  

load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
