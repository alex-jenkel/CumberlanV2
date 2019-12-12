import discord

TOKEN_FILE = "data/discord_bot_token.txt"

# Creating a bot instance
cumberlan = discord.Client()

# Initializing the bot
cumberlan.run(load_token())