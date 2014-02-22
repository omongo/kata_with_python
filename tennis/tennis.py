class TennisScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def get_score(self):
        pts = ('Love', 'Fifteen', 'Thirty', 'Forty')
        p1 = self.p1_score
        p2 = self.p2_score
        if (p1 + p2) >= 6:
            if p1 == p2: return 'Deuce'
            p = 'P1' if p1 > p2 else 'P2'
            return ('Game ' if abs(p1 - p2) == 2 else 'Advantage ') + p
        return pts[p1] + ' - ' + (pts[p2] if p1 != p2 or p1 == 0 else 'All')

    def won_p1(self):
        self.p1_score += 1

    def won_p2(self):
        self.p2_score += 1
