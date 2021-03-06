from discord.ext import commands
from cogs.status import Status
from cogs.utils.game import Game
from cogs.utils.player import Player
from cogs.utils.game import Game

import discord
import os

class GameStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

    @commands.command()
    async def create(self, ctx):
        """セッションを立てる"""

        if f'{ctx.guild.id}' not in self.bot.games:
            self.bot.games[f'{ctx.guild.id}'] = Game()

        if self.bot.games[f'{ctx.guild.id}'].status == Status.PLAYING:
            return await ctx.send('セッション中です')
            
        if self.bot.games[f'{ctx.guild.id}'].status == Status.WAITING:
            return await ctx.send('セッション準備中')
            
        self.bot.games[f'{ctx.guild.id}'].status = Status.WAITING
        self.bot.games[f'{ctx.guild.id}'].channel = ctx.channel
        await ctx.send('セッションの準備を開始します')
        mem = Player(ctx.author.id, ctx.author.name, True)
        self.bot.games[f'{ctx.guild.id}'].players.append(mem)
        self.bot.games[f'{ctx.guild.id}'].logs.append(f'{ctx.author.name}さんがセッションを立ち上げました ::  <{Game.get_time()}>')

    @commands.command()
    async def test(self, ctx):
        await ctx.send(ctx.guild.id)

    @commands.command()
    async def start(self, ctx):
        """セッション開始"""

        if f'{ctx.guild.id}' not in self.bot.games:
            self.bot.games[f'{ctx.guild.id}'] = Game()

        if self.bot.games[f'{ctx.guild.id}'].status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.games[f'{ctx.guild.id}'].status == Status.PLAYING:
            await ctx.send('セッション中です')
            return

        self.bot.games[f'{ctx.guild.id}'].status = Status.PLAYING

        await ctx.send('セッション開始しました')
        if ctx.author.voice is not None:
            vc = ctx.author.voice.channel
            await vc.connect()


    
    @commands.command()
    async def close(self, ctx):
        """セッション終了"""
        if f'{ctx.guild.id}' not in self.bot.games:
            self.bot.games[f'{ctx.guild.id}'] = Game()
            
        if self.bot.games[f'{ctx.guild.id}'].status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.games[f'{ctx.guild.id}'].status == Status.WAITING:
            self.bot.games[f'{ctx.guild.id}'].status = Status.NOTHING
            await ctx.send('セッションをキャンセルします')
            self.bot.games[f'{ctx.guild.id}'] = Game()
            return
        self.bot.games[f'{ctx.guild.id}'].status = Status.NOTHING
        await ctx.send('セッションを終了します')

        for p in self.bot.games[f'{ctx.guild.id}'].players:
            filename = f'{p.id}log.txt'
            with open(filename,'w') as f:
                for log in p.logs:
                    f.write(log + '\n')
            await ctx.send(file=discord.File(filename))
            os.remove(filename)
            await ctx.send(f'{p.name}さんのログを出力しました')
        with open('gamelog.txt', 'w') as f:

            for log in self.bot.games[f'{ctx.guild.id}'].logs:
                f.write(log + "\n")

        await ctx.send(file=discord.File('gamelog.txt'))
        os.remove('gamelog.txt')

        if ctx.guild.voice_client is not None:
            client = ctx.guild.voice_client
            await client.disconnect()
        self.bot.game = Game()


def setup(bot):
    bot.add_cog(GameStatus(bot))
