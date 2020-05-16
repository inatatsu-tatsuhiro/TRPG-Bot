from discord.ext import commands
from cogs.utils.player import Player
from cogs.status import Status

class PlayerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """セッションに参加する"""
        if self.bot.game.status == Status.NOTHING:
            await ctx.send('セッションが立っていません')
            return
        if self.bot.game.status == Status.PLAYING:
            await ctx.send('セッションが進行中です')
            return
        # if 既に参加している場合（未実装）


        await ctx.send(f'{ctx.author.mention}さんが参加しました')

    # @commands.command()
    # async def leave(self, ctx):
        """セッションへの参加をやめる（脱退）"""
