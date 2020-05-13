from discord.ext import commands # Bot Commands Frameworkをインポート
import os
import traceback # エラー表示のためにインポート


INITIAL_EXTENSIONS = [
    'cogs.cthulhucog'
]

class MyBot(commands.Bot):


    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')


if __name__ == '__main__':
    bot = MyBot(command_prefix='!')
    bot.run(os.environ["TOKEN"]) # botトークンを環境変 TOKEN を使う