from __future__ import annotations

class Player():
    """参加者

    Attributes:
        id (int): Discord ID
        is_GM (bool): GM or PL
        logs (string[]): Playerごとのログ
    """

    def __init__(self, d_id: int, d_name: string, gm: bool = False):
        self.id = d_id
        self.name = d_name
        self.is_GM = gm
        self.logs = []

    

class Players(list):
    """全参加者"""

    @property
    def players(self) -> Players:
        "PL一覧"
        return Players(p for p in self if p.is_GM == False)

    def get(self, player_id) -> Player:
        for p in self:
            if p.id == player_id:
                return p

    def is_joined(self, player_id) -> bool:
        for p in self:
            if p.id == player_id:
                return True
        return False