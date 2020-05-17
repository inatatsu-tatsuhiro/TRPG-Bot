from discord.ext import commands
from enum import Enum, auto

class Status(Enum):
    NOTHING = auto()
    WAITING = auto()
    PLAYING = auto()

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

        if self.bot.game.status == Status.PLAYING:
            await ctx.send('セッション中です')
            return
        if self.bot.game.status == Status.WAITING:
            await ctx.send('セッション準備中')
            return
        
        self.bot.game.status = Status.WAITING
        self.bot.game.channel = ctx.channel
        await ctx.send('セッションの準備を開始します')


    @commands.command()
    async def start(self, ctx):
        """セッション開始"""
        if self.bot.game.status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.game.status == Status.PLAYING:
            await ctx.send('セッション中です')
            return
        await ctx.send(f'{self.bot.game.status=}')
        await ctx.send(f'{Status.NOTHING=}')
        await ctx.send(f'{type(self.bot.game.status)=}')
        await ctx.send(f'{type(Status.NOTHING)=}')
        tmp = Status.NOTHING
        await ctx.send(f'{tmp=}')
        await ctx.send(f'{id(tmp)=}')
        await ctx.send(f'{id(self.bot.game.status)=}')
        await ctx.send(f'{id(Status.NOTHING)=}')
        await ctx.send(f'{self.bot.game.status.value == Status.NOTHING=}')
        await ctx.send(f'{Status.NOTHING == self.bot.game.status=}')
        await ctx.send(f'{self.bot.game.status == Status.WAITING=}')
        await ctx.send(f'{Status.NOTHING == Status.WAITING=}')
        await ctx.send(f'{Status.NOTHING == Status.NOTHING=}')

        self.bot.game.status = Status.PLAYING
        await ctx.send('セッション開始しました')

    
    @commands.command()
    async def close(self, ctx):
        """セッション終了"""
        if self.bot.game.status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.game.status == Status.WAITING:
            self.bot.game.status = Status.NOTHING
            await ctx.send('セッションをキャンセルします')
            return
        self.bot.game.status = Status.NOTHING
        await ctx.send('セッションを終了します')



def setup(bot):
    bot.add_cog(GameStatus(bot))
