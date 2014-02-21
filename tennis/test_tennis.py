import unittest
from tennis import TennisScoreBoard


class TestTennis(unittest.TestCase):
    def setUp(self):
        self.tennisScoreBoard = TennisScoreBoard()

    def testLoveLove(self):
        expected = "Love Love"
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testFifteenLove(self):
        expected = "Fifteen Love"
        self.tennisScoreBoard.won_p1_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testFifteenAll(self):
        expected = "Fifteen All"
        self.tennisScoreBoard.won_p1_score()
        self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testFifteenThirty(self):
        expected = "Fifteen Thirty"
        self.tennisScoreBoard.won_p1_score()
        for i in xrange(2):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testThirtyAll(self):
        expected = "Thirty All"
        for i in xrange(2):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(2):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testFirstDeuce(self):
        expected = "Deuce"
        for i in xrange(3):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(3):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testNextDeuce(self):
        expected = "Deuce"
        for i in xrange(4):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(4):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testAdvantageP1(self):
        expected = "Advantage P1"
        for i in xrange(4):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(3):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testAdvantageP2(self):
        expected = "Advantage P2"
        for i in xrange(3):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(4):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)

    def testGameP1(self):
        expected = "Game P1"
        for i in xrange(5):
            self.tennisScoreBoard.won_p1_score()
        for i in xrange(3):
            self.tennisScoreBoard.won_p2_score()
        result = self.tennisScoreBoard.get_score()
        self.assertEquals(expected, result)
