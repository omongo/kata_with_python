class TennisScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def getScore(self):
        p1_wording = "Love"
        p2_wording = "Love"
        if self.p1_score == 1: 
            p1_wording = "Fifteen"
            if self.p2_score == 1: 
                p2_wording = "All"
            if self.p2_score == 2:
                p2_wording = "Thirty"
        return "%s %s" % ( p1_wording, p2_wording)

    def wonScore(self, name):
        if name=="p1": self.p1_score += 1
        if name=="p2": self.p2_score += 1
