import re                        # regex stuff
import discord
from baneposting import BIGGUY4U
from discord.ext import commands

# NEED to obtain this Discord token for the bot. Will probably not work until
# it has been obtained and placed in the below file
TOKEN_FILE = "data/discord.token"

# Creating a bot instance
#cumberlan = discord.Client()      # old initialization
cumberlan = commands.Bot(command_prefix = '$')


# Creating a list of cogs
cogz = ['bane']


# ==========
#    NOTE
# ==========
#
# You need to define some functions and other things for the bot to work. For
# example, the load_token() must be defined. Use Cumberlan as a good reference
# point for it.

# Check in upon awakening
@cumberlan.event
async def on_ready():
    print("Logged in as")
    print(cumberlan.user.name)
    print(cumberlan.user.id)
    print('------')


# Checks each message for keywords; ignores commands
@cumberlan.event
async def on_message(message):
    """Check for commands after each new message."""
    try:
        # Skips messages sent by Cumberlan
        if message.author == cumberlan.user:
            return

        # Skips commands
        if message.content.startswith("$"):
            await cumberlan.process_commands(message)

        # Checks if message is a Banepost
        else:
            # Scrub the message
            scrubbed_msg = message.content.lower().strip()
            scrubbed_msg = re.sub("([!.,'?])", "", scrubbed_msg)
            print(scrubbed_msg, flush = True)

            # Get dictionary value, is None if not available
            new_banepost = BIGGUY4U.get(scrubbed_msg, None)
            if new_banepost is not None:
                await message.channel.send(new_banepost)

    except Exception as error:
        print(error, flush = True)


#NOTE: next two commands will probably be removed later
# They are only in for testing purposes

# Loads a cog
@cumberlan.command()
async def load(cog):
    try:
        cumberlan.load_extension(cog)
        print('Test {}'.format(cog), flush = True)
    except Exception as error:
        print('Error {}'.format(cog, error), flush = True)

# Unloads a cog
@cumberlan.command()
async def unload(cog):
    try:
        cumberlan.unload_extension(cog)
        print('unTest {}'.format(cog))
    except Exception as error:
        print('Error {}'.format(cog, error), flush = True)

# Hello command
@cumberlan.command()
async def hello(message):
    msg = "Hello {0.author.mention}".format(message)
    print(msg, flush = True)
    await message.channel.send(msg)


# Loads all cogs in the list
if __name__ == '__main__':
    for cog in cogz:
        try:
            cumberlan.load_extension("scripts." + cog)
        except Exception as error:
            print('uh oh {}'.format(cog, error), flush = True)
            print(error, flush = True)


def load_token():
    """Loads the Discord API authentication token."""
    with open(TOKEN_FILE, "r") as token_file:
        return token_file.read().strip()


# Initializing the bot

cumberlan.run('NTc1MTY2NDg5ODI5NTcyNjE4.XfgNUg.KJkp_4Qc24IOgIfv9II8hkwL9bY')
