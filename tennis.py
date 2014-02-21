class TennisScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def get_score(self):
        score = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}
        if self.p1_score == self.p2_score:
            if self.p1_score == 3:
                return "Deuce"
            elif self.p1_score != 0:
                return "{} All".format(score[self.p1_score])
        if (self.p1_score - self.p2_score ==1) and (self.p1_score + self.p2_score > 6):
            return "Advantage P1"
        if (self.p1_score - self.p2_score ==2) and (self.p1_score + self.p2_score > 7):
            return "Game P1"
        return "{} {}".format(score[self.p1_score], score[self.p2_score])

    def won_p1_score(self):
        self.p1_score += 1

    def won_p2_score(self):
        self.p2_score += 1
