from __future__ import annotations

class Player():
    """参加者

    Attributes:
        id (int): Discord ID
        is_GM (bool): GM or PL
    """

    def __init__(self, d_id: int, gm: bool):
        self.id = d_id
        self.is_GM = gm

    

class Players(list):
    """全参加者"""

    @property
    def players(self) -> Players:
        "PL一覧"
        return Players(p for p in self if p.is_GM)

    def get(self, player_id) -> Player:
        for p in self:
            if p.id == player_id:
                return p
