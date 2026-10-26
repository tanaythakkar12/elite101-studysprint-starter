import unittest
from features import reports

class TestAverageScore(unittest.TestCase):

    def test_empty_history(self):
        data = {"history": []}
        self.assertEqual(reports.average_score(data), 0.0)

    def test_one_score(self):
        data = {"history": [8]}
        self.assertEqual(reports.average_score(data), 8.0)

    def test_several_scores(self):
        data = {"history": [5, 6, 4]}
        self.assertEqual(reports.average_score(data), 5.0)