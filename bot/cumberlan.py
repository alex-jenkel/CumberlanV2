import discord

# NEED to obtain this Discord token for the bot. Will probably not work until
# it has been obtained and placed in the below file
TOKEN_FILE = "data/discord_bot_token.txt"

# Creating a bot instance
cumberlan = discord.Client()

# ==========
#    NOTE
# ==========
#
# You need to define some functions and other things for the bot to work. For
# example, the load_token() must be defined. Use Cumberlan as a good reference
# point for it.

# Initializing the bot
cumberlan.run(load_token())