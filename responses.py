def get_response(user_message: str) -> str:
    user_message = user_message.lower()

    if user_message == "hello":
        return "Hello! How can I assist you?"
    elif user_message == "help":
        return "Sure! Here's what I can do: Type 'hello' to greet me or 'help' to see this message."
    else:
        return "Sorry, I didn't understand that. Type 'help' for available commands."
