import os
from dotenv import load_dotenv
from bot import client  

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
