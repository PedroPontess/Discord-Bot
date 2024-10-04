from openai import OpenAI
import os
from dotenv import load_dotenv
from openai.types.chat import chat_completion

load_dotenv()

OPENAI_TOKEN = str(os.getenv('OPENAI_TOKEN'))
client = OpenAI(api_key=OPENAI_TOKEN)

def get_response(user_message: str) -> str:
    user_message = user_message.lower()

    if user_message == "hello":
        return "Hello! How can I assist you?"
    elif user_message == "help":
        return "Sure! Here's what I can do: Type 'hello' to greet me or 'help' to see this message."
    else:
        return "Sorry, I didn't understand that. Type 'help' for available commands."

def get_chatGPT_response(user_message: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        model="gpt-3.5-turbo"
    )
    return str(chat_completion)

