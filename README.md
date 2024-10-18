# Discord Bot with GPT Integration

## Description

This project is a Discord bot built using Python and the `discord.py` library. The bot includes several functionalities, such as:
- Moderation
- Integration with OpenAI's GPT for natural language responses, where users can ask the bot questions and receive AI-generated answers.

## Features
- **Mute Command**: Temporarily mutes users by restricting their permissions in all text channels.
- **Unban Command**: Unbans users using their unique Discord ID.
- **Ban Command**: Bans users using their unique Discord ID.
- **Kick Command**: Kicks users using their unique Discord ID.
- **Ask GPT**: Allows users to interact with the GPT model for responses directly from Discord.

## Requirements

- Python 3.8 or higher
- Libraries:
  - `discord.py`
  - `openai` 
  - Any other required dependencies

You can install these with:
```bash
pip install -r requirements.txt
```

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Environment Variables

This project requires environment variables for secure access to Discord and OpenAI APIs. Create a `.env` file in the root directory of the project and add the following keys:

- `DISCORD_TOKEN`: This is the bot token from your [Discord Developer Portal](https://discord.com/developers/applications).
- `OPENAI_API_KEY`: This is the API key from your [OpenAI account](https://platform.openai.com/account/api-keys).

#### Steps to Set Up the `.env` File:

1. In the root of your project directory, create a new file named `.env`.
2. Open the file and paste in the environment variables as shown above.
3. Replace `your_discord_bot_token` with the actual token from Discord and `your_openai_api_key` with your actual OpenAI API key.

