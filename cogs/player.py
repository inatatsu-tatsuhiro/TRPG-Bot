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

    @commands.command()
    async def dice(self, ctx, d_count=3, d_max=6):

        if ctx.message.guild.voice_client is not None:
            voice_client = ctx.message.guild.voice_client
            ffmpeg_audio_source = discord.FFmpegPCMAudio("dice.mp3")
            voice_client.play(ffmpeg_audio_source)
            
        msg, num = diceroll(d_count,d_max)
        await ctx.send(f'{ctx.author.name}さんの{d_count}D{d_max}\n{msg}')
        self.bot.game.logs.append(f'{ctx.author.name}さんの{d_count}D{d_max} -> {num} :: <{self.bot.game.get_time()}>')
        self.bot.game.players.get(mem.id).logs.append(f'{d_count}D{d_max} -> {num} :: <{self.bot.game.get_time()}>')

    @commands.command(aliases=['dd'])
    async def d100(self, ctx, limit=-1):

        if ctx.message.guild.voice_client is not None:
            voice_client = ctx.message.guild.voice_client
            ffmpeg_audio_source = discord.FFmpegPCMAudio("dice.mp3")
            voice_client.play(ffmpeg_audio_source)

        r = _random(100)
        msg = ""
        if limit == -1:
            msg = f'1D100の結果は{r}です'
        else:
            if r <= limit and r <= 5:
                msg = f'1D100の結果は{r}でクリティカル'
            elif r <= limit:
                msg = f'1D100の結果は{r}で成功'
            elif limit < r and 96 <= r:
                msg = f'1D100の結果は{r}でファンブル'
            else :
                msg = f'1D100の結果は{r}で失敗'
        await ctx.send(f'{ctx.author.name}さんの{msg}')
        self.bot.game.logs.append(f'{ctx.author.name}さんの{msg}')
        self.bot.game.players.get(mem.id).logs.append(msg)


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
