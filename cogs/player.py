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
        if self.bot.game.status == Status.WAITING:
            if ctx.author.id in self.bot.game.players:
                await ctx.send('セッション参加済みです')
                return


        await ctx.send(f'{ctx.author.mention}さんが参加しました')

    @commands.command()
    async def leave(self, ctx):
        """セッションへの参加をやめる（脱退）"""
        if self.bot.game.status == Status.NOTHING:
            return await ctx.send("セッションが立っていません")
        elif self.game.bot.status == Status.PLAYING:
            return await ctx.send("セッションが既に開始されているため退出出来ません")
        mem = ctx.author
        for p in self.bot.game.players:
            if mem.id == p.id:
                return await ctx.send("セッションから退出しました")

def setup(bot):
    bot.add_cog(PlayerCog(bot))
