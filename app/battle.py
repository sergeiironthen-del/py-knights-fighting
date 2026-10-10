class Battle:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2

    def battle_result(self) -> None:
        self.player1.hp -= self.player2.power - self.player1.protection
        self.player2.hp -= self.player1.power - self.player2.protection
        
        if self.player1.hp <= 0:
            self.player1.hp = 0
        
        if self.player2.hp <= 0:
            self.player2.hp = 0
