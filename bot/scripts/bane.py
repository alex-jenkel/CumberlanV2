import discord
from discord.ext import commands


class Bane(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Online Big Guy', flush = True)

    @commands.command()
    async def bane(self, ctx):
        await ctx.send(the_big_bad_banepost)


def setup(client):
    client.add_cog(Bane(client))


#TODO: Move this to a text file
the_big_bad_banepost = """
CIA: Dr. Pavel, I'm CIA.

Masketta Man: He wasn't alone.

CIA: Uh, you don't get to bring friends.

Dr. Pavel: They're not my friends.

Masketta Man: Don't worry, no charge for them.

CIA: And why would I want them?

Masketta Man: They were trying to grab your prize. They work for the mercenary... the masked man.

CIA: Bane? Get 'em on board, I'll call it in.

CIA: The Flight Plan I just filled with the Agency lists me, my men, and Dr. Pavel here but only one of you!

CIA: FIRST ONE TO TALK GETS TO STAY ON MY AIRCRAFT!

CIA: WHO PAID YOU TO GRAB DR. PAVEL?

CIA: HE DIDN'T FLY SO GOOD! WHO WANTS TO TRY NEXT?

CIA: TELL ME ABOUT BANE! WHY DOES HE WEAR THE MASK?

CIA: LOT OF LOYALTY FOR A HIRED GUN!

Bane: Or perhaps he's wondering why someone would shoot a man before throwing him out of a plane...

CIA: At least you can talk, who are you?

Bane: It doesn't matter who we are... What matters is our plan.

Bane: No one cared who I was 'till I put on the mask.

CIA: If I pull that off will you die?

Bane: It would be extremely painfull...

CIA: You're a big guy!

Bane: For you.

CIA: Was getting caught part of your plan?

Bane: Of course!

Bane: Dr. Pavel refused our offer in favor of yours, we had to find out what he told you.

Dr. Pavel: Nothing! I said nothing!

CIA: Well congratulations, you got yourself caught!

Sir: Sir?

CIA: Now what's the next step of your master plan?

Bane: Crashing this plane... WITH NO SURVIVORS!!!!!!

Dr. Pavel: [Incoherent screaming] AAAAAAAHHH STAY AWAY, MY ARM!!!! OH HAH!!! NOOOOOLAN BRAVO! OH HAAAAAAAH! [More incoherent screaming]

Bane: No! They expect one of us in the wreckage, brother!

Juan: Have we started the fire?

Bane: Yes! The fire rises!

Dr. Pavel: [Incoherent screaming]

Bane: Calm down, Doctor. Now is not the time for fear... That comes later!
"""
