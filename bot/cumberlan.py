import discord

# NEED to obtain this Discord token for the bot. Will probably not work until
# it has been obtained and placed in the below file
TOKEN_FILE = "data/discord.token"

# Creating a bot instance
cumberlan = discord.Client()

# ==========
#    NOTE
# ==========
#
# You need to define some functions and other things for the bot to work. For
# example, the load_token() must be defined. Use Cumberlan as a good reference
# point for it.

@cumberlan.event
async def on_message(message):
    """Check for commands after each new message."""

    # Skips messages sent by Cumberlan
    if message.author == cumberlan.user:
        return

    if message.content.startswith("$hello"):
        msg = "Hello {0.author.mention}".format(message)
        await cumberlan.send_message(message.channel, msg)

@cumberlan.event
async def on_ready():
    print("Logged in as")
    print(cumberlan.user.name)
    print(cumberlan.user.id)
    print('------')

def load_token():
    """Loads the Discord API authentication token."""
    with open(TOKEN_FILE, "r") as token_file:
        return token_file.read().strip()

# Initializing the bot
cumberlan.run(load_token())
