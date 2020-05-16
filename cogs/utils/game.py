from cogs.utils.player import Player, Players
from cogs.status import Status

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
        self.logs = ["セッションの準備を始めます"]