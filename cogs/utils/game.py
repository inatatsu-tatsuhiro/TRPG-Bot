from cogs.utils.player import Player, Players

class Game():
    """TRPG_GAME
    
    Attributes:
        status (str): 進行状況
        channel (discord.TextChannel): TRPGするチャンネル
        players (Players): 参加者リスト
        logs (str[]): ゲームのログ

    """

    def __init__(self):
        self.status = 'nothing'
        self.channel = None
        self.players = Players()
        self.logs = ["セッションの準備を始めます"]