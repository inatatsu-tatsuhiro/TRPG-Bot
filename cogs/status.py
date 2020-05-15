from discord.ext import commands

class GameStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx):
        