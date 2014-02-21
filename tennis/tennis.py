class TennisScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def get_score(self):
        score = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}
        deuce = self.p1_score == self.p2_score
        if deuce:
            next_deuce = self.p1_score + self.p2_score == 8
            if next_deuce:
                self.p1_score = self.p2_score = 3
            if self.p1_score == 3:
                return "Deuce"
            elif self.p1_score != 0:
                return "{} All".format(score[self.p1_score])
        else:
            p1_advantage = cmp(self.p1_score, self.p2_score)
            sum_of_score = self.p1_score + self.p2_score


            if (self.p1_score - self.p2_score >= 2) and (sum_of_score == 8):
                return "Game P1"
            elif sum_of_score >7:
                return "Game P2"

            if ( p1_advantage==1 ) and (sum_of_score == 7):
                return "Advantage P1"
            elif sum_of_score >=7 :
                return "Advantage P2"
        return "{} {}".format(score[self.p1_score], score[self.p2_score])

    def won_p1_score(self):
        self.p1_score += 1

    def won_p2_score(self):
        self.p2_score += 1