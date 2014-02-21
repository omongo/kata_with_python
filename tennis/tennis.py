class TennisScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def get_score(self):
        scores = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}
        deuce = (self.p1_score + self.p2_score) >= 6
        score_can_game = max(self.p1_score, self.p2_score) >= 4
        if score_can_game:
            score_diff = self.p1_score - self.p2_score
            if score_diff == 2:
                return "Game P1"
            elif score_diff == -2:
                return "Game P2"
        if deuce:
            if self.p1_score > self.p2_score:
                return "Advantage P1"
            elif self.p1_score < self.p2_score:
                return "Advantage P2"
            else:
                return "Deuce"
        else:
            if self.p1_score != self.p2_score or self.p1_score == 0:
                return "{} - {}".format(scores[self.p1_score], scores[self.p2_score])
            else:
                return "{} - All".format(scores[self.p1_score])

    def won_p1_score(self):
        self.p1_score += 1

    def won_p2_score(self):
        self.p2_score += 1
