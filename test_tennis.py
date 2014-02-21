import unittest
from tennis import TennisScoreBoard
class TestTennis(unittest.TestCase):
    def setUp(self):
        self.tennisScoreBoard = TennisScoreBoard()
    
    def testLoveLove(self):
        expected = "Love Love"
        result = self.tennisScoreBoard.getScore()
        self.assertEquals(expected, result)

    def testFifteenLove(self):
        expected = "Fifteen Love"
        self.tennisScoreBoard.wonScore('p1')
        result = self.tennisScoreBoard.getScore()
        self.assertEquals(expected, result)

    def testFifteenAll(self):
        expected = "Fifteen All"
        self.tennisScoreBoard.wonScore('p1')
        self.tennisScoreBoard.wonScore('p2')
        result = self.tennisScoreBoard.getScore()
        self.assertEquals(expected, result)
    
    def testFifteenThirty(self):
        expected = "Fifteen Thirty"
        self.tennisScoreBoard.wonScore('p1')
        self.tennisScoreBoard.wonScore('p2')
        self.tennisScoreBoard.wonScore('p2')
        result = self.tennisScoreBoard.getScore()
        self.assertEquals(expected, result)
