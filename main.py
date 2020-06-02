from discord.ext import commands # Bot Commands Frameworkをインポート
import os
import traceback # エラー表示のためにインポート
from cogs.utils.game import Game

bot = commands.Bot(command_prefix='!')
bot.game = Game()
EXTENSIONS = [
    'cogs.gamestatus',
    'cogs.player'
]

for extension in EXTENSIONS:
    bot.load_extension(extension)

bot.run(os.environ["TOKEN"])
