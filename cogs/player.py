from discord.ext import commands
from cogs.utils.player import Player
from cogs.status import Status

import discord
import os

class PlayerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """セッションに参加する"""
        if self.bot.game.status == Status.NOTHING:
            return await ctx.send('セッションが立っていません')
            
        if self.bot.game.status == Status.PLAYING:
            return await ctx.send('セッションが進行中です')
            
        player = ctx.author
        for p in self.bot.game.players:
            if p.id == player.id:
                return await ctx.send('セッション参加済みです')
        mem = Player(player.id)
        self.bot.game.players.append(mem)
        self.bot.game.logs.append(f'{player.name}さんがセッションに参加しました :: <{self.bot.game.get_time()}>')
        self.bot.game.players.get(player.id).logs.append(f'セッションに参加しました :: <{self.bot.game.get_time()}>')
        await ctx.send(f'{player.mention}さんが参加しました')

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
                self.bot.game.logs.append(f'{mem.name}さんがセッションから退出しました :: <{self.bot.game.get_time()}>')
                self.bot.game.players.get(mem.id).logs.append(f'セッションから退出しました :: <{self.bot.game.get_time()}>')
                return await ctx.send("セッションから退出しました")

    @commands.command()
    async def gamelog(self, ctx):
        """ゲーム全体のログファイルを出力"""
        with open('gamelog.txt', 'w') as f:

            for log in self.bot.game.logs:
                f.write(log + "\n")

        await ctx.send(file=discord.File('gamelog.txt'))
        os.remove('gamelog.txt')
        
        await ctx.send("ゲームログを出力しました")


    @commands.command()
    async def mylog(self, ctx):
        """自分のログファイルを出力"""
        p = self.bot.game.players.get(ctx.author.id)
        filename = f'{ctx.author.name}log.txt'
        with open(filename,'w') as f:
            for log in p.logs:
                f.write(log + '\n')
        os.remove(filename)
        await ctx.send(f'{ctx.author.name}さんのログを出力しました')


def setup(bot):
    bot.add_cog(PlayerCog(bot))
