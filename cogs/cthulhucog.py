from discord.ext import commands # Bot Commands Frameworkのインポート
import random

class CthulhuCog(commands.Cog):

    def __init__(self, bot):
        
        self.bot = bot

    @commands.group()
    async def coc(self, ctx):
        if ctx.invoked_subcommand is None:
           await ctx.send('正しいサブコマンドを入力してください。')
    
    # @commands.command()
    # async def dice(self, ctx, args):
    #     await ctx.send('ダイス')


    @coc.command(aliases=['d'])
    async def dice(self, ctx, d_count=3, d_max=6):
        await ctx.send(ctx.author.name + "さんの" + str(d_count) + "D" + str(d_max) +"\n" + diceroll(d_count,d_max))

    @coc.command(aliases=['h'])
    async def help(self, ctx):
        await ctx.send(printhelp())
    
    @coc.command(aliases=['dd'])
    async def d100(self, ctx, limit=-1):
        r = _random(100)
        # ctx.send(ctx.author.name + "さんの1D100の結果は : " + str(r))
        if limit == -1:
            await ctx.send(ctx.author.name + "さんの 1D100の結果は" + str(r) + "です")
        else:
            if r <= limit and r <= 5:
                await ctx.send(ctx.author.name + "さんの 1D100の結果は" + str(r) + "でクリティカルです")
            elif r <= limit:
                await ctx.send(ctx.author.name + "さんの 1D100の結果は" + str(r) + "で成功です")
            elif limit < r and 96 <= r:
                await ctx.send(ctx.author.name + "さんの 1D100の結果は" + str(r) + "でファンブルです")
            else :
                await ctx.send(ctx.author.name + "さんの 1D100の結果は" + str(r) + "で失敗です")
            
            


def setup(bot):
    bot.add_cog(CthulhuCog(bot))


def diceroll(d_count, d_max):
    result = ""
    num = 0
    for i in range(int(d_count)):
        rand = _random(d_max)
        msg = str(i+1) + "回目：" + str(rand) + "\n"
        num += rand
        result += msg
    result += "結果:" + str(num)
    return result

def _random(d_max):
    return int(random.random() * int(d_max) + 1)


def printhelp():
    return "```[botのヘルプ]\n\n!coc help [h] : ヘルプの表示 \n!coc dice [d] <dice_count> <dice_max> : dice_count D dice_max を実行する、初期値(省略時)3D6 ex) !coc d -> 3D6 , !coc dice 2 6 -> 2D6 \n!coc d100 [dd] <limit> : 1D100を実行しlimitを指定した場合成功判定を行う \n\n[]はコマンドの省略記法, <>は引数が省略可能であることを示す```"