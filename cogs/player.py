from discord.ext import commands
from cogs.utils.player import Player
from cogs.status import Status

import discord
import random
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
        self.bot.game.players.append(player)
        self.bot.game.logs.append(f'{player.mention}さんがセッションに参加しました')
        # self.bot.game.players.get(player.id).logs.append("セッションに参加しました")
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
                self.bot.game.logs.append(f'{mem.mention}さんがセッションから退出しました')
                # self.bot.game.players.get(mem.id).logs.append("セッションから退出しました")
                return await ctx.send("セッションから退出しました")

    @commands.command()
    async def gamelog(self, ctx):
        await ctx.send("hi")
        """ゲーム全体のログファイルを出力"""
        with open('test.txt', 'w') as f:
            f.write('hogehoge')
        await ctx.send(file=discord.File('test.txt'))
        os.remove('test.txt')

    @commands.command()
    async def dice(self, ctx, d_count=3, d_max=6):
        msg, num = diceroll(d_count,d_max)
        await ctx.send(f'{ctx.author.name}さんの{d_count}D{d_max}\n{msg}')
        



def setup(bot):
    bot.add_cog(PlayerCog(bot))

def diceroll(d_count, d_max):
    result = ""
    num = 0
    for i in range(int(d_count)):
        rand = _random(d_max)
        msg = f'{i+1}回目：{rand}\n'
        num += rand
        result += msg
    result += f'結果:{num}'
    return result, num

def _random(d_max):
    return int(random.random() * int(d_max) + 1)