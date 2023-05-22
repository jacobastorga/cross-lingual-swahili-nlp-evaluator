import unittest
from src.swahili_grammar_rules import verify_subject_verb_concord
from src.cross_lingual_evaluator import CrossLingualEvaluator


class TestSwahiliEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = CrossLingualEvaluator()

    def test_subject_verb_concord(self):
        # Class 1: Mtoto anasoma (The child is reading) -> True
        self.assertTrue(verify_subject_verb_concord("Mtoto", "anasoma", "Class 1 (M-)"))
        # Class 2: Watoto wanasoma (The children are reading) -> True
        self.assertTrue(verify_subject_verb_concord("Watoto", "wanasoma", "Class 2 (WA-)"))
        # Class 7: Kitabu kinasomwa (The book is read) -> True
        self.assertTrue(verify_subject_verb_concord("Kitabu", "kinasomwa", "Class 7 (KI-)"))
        # False concord: Mtoto kinasoma -> False
        self.assertFalse(verify_subject_verb_concord("Mtoto", "kinasoma", "Class 1 (M-)"))

    def test_lexical_overlap(self):
        cand = "Mhandisi huyu anajenga mfumo wa kanzidata."
        ref = "Mhandisi huyu anaunda mfumo wa kanzidata thabiti."
        overlap = self.evaluator.compute_lexical_overlap(cand, ref)
        self.assertGreater(overlap, 0.5)

    def test_unlocalized_borrowings(self):
        dirty_text = "Huu mfumo unatumia artificial intelligence na database."
        flagged = self.evaluator.detect_unlocalized_borrowings(dirty_text)
        self.assertIn("artificial intelligence", flagged)
        self.assertIn("database", flagged)


if __name__ == "__main__":
    unittest.main()
