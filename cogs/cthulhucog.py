from discord.ext import commands # Bot Commands Frameworkのインポート
import random

# コグとして用いるクラスを定義。
class CthulhuCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.group()
    async def coc(self, ctx):
        if ctx.invoked_subcommand is None:
           await ctx.send('サブコマンドを入力してください。')


    @coc.command()
    async def dice(self, ctx):
        await ctx.send(str(diceroll(3,6)))

#     def diceroll(count, max):
#         # result = []
#         # for i in range(int(count)):
#         #     result[i] = random.random() * int(max) + 1
#         return 1
# # Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(CthulhuCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。


def diceroll(count, max):
    result = ""
    num = 0
    for i in range(int(count)):
        rand = int(random.random() * int(max) + 1)
        msg = str(i+1) + "回目：" + str(rand) + "\n"
        num += rand
        result += msg
    result += "結果:" + str(num) + "です" 
    return result