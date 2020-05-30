from cogs.utils.player import Player, Players
from cogs.status import Status
from datetime import datetime, timezone, timedelta

class Game():
    """TRPG_GAME
    
    Attributes:
        status (Status): 進行状況
        channel (discord.TextChannel): TRPGするチャンネル
        players (Players): 参加者リスト
        logs (str[]): ゲームのログ

    """

    def __init__(self):
        self.status = Status.NOTHING
        self.channel = None
        self.players = Players()
        self.logs = []


    def get_time(self):
        JST = timezone(timedelta(hours=+9), 'JST')
        t = str(datetime.now(JST)).split(".")[0]
        return t