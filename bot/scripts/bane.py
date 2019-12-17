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

    @commands.command()
    async def bog(self, ctx):
        await ctx.send(the_quick_rundown)


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


the_quick_rundown = """
>Rothschilds bow to Bogdanoffs

>In contact with aliens 

>Possess psychic-like abilities 

>Control france with an iron but fair fist 

>Own castles & banks globally 

>Direct descendants of the ancient royal blood line 

>Will bankroll the first cities on Mars (Bogdangrad will be be the first city) 

>Own 99% of DNA editing research facilities on Earth 

>First designer babies will in all likelihood be Bogdanoff babies 

>both brothers said to have 215+ IQ, such intelligence on Earth has only existed deep in Tibetan monasteries & Area 51 

>Ancient Indian scriptures tell of two angels who will descend upon Earth and will bring an era of enlightenment and unprecedented technological progress with them 
>They own Nanobot R&D labs around the world 

>You likely have Bogdabots inside you right now 

>The Bogdanoffs are in regular communication with the Archangels Michael and Gabriel, forwarding the word of God to the Orthodox Church. Who do you think set up the meeting between the pope & the Orthodox high command (First meeting between the two organisations in over 1000 years) and arranged the Orthodox leader's first trip to Antarctica in history literally a few days later to the Bogdanoff bunker in Wilkes land? 

>They learned fluent French in under a week 

>Nation states entrust their gold reserves with the twins. There's no gold in Ft. Knox, only Ft. Bogdanoff 

>The twins are about 7 decades old, from the space-time reference point of the base human currently accepted by our society 

>In reality, they are timeless beings existing in all points of time and space from the big bang to the end of the universe. We don't know their ultimate plans yet. We hope they're benevolent beings.

"""