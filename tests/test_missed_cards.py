import unittest
from features import core


class TestMissedCards(unittest.TestCase):

    def test_missed_cards(self):
        cards = [
            {"question": "2 + 2?", "answer": "4"},
            {"question": "3 + 3?", "answer": "6"}
        ]

        answers = iter(["4", "wrong"])
        missed = []

        score = core.run_quiz(
            cards,
            ask=lambda prompt: next(answers),
            show=lambda message: None,
            missed=missed
        )

        self.assertEqual(score, 1)
        self.assertEqual(len(missed), 1)
        self.assertEqual(missed[0]["question"], "3 + 3?")


if __name__ == "__main__":
    unittest.main()