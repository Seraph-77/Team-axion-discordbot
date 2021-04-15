import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('testcog.py online.')

    @commands.command()
    async def pin(self, ctx):
        await ctx.send('ball')


def setup(client):
    client.add_cog(Example(client))

#the whole point of this section was to test if i can make cogs/extensions
#i don't currently see what the point of using this would be, other than to save space on the main file
#maybe ill move commands into a cog, but that could take awhile