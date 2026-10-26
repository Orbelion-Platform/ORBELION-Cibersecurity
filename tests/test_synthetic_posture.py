import unittest

from examples.synthetic_posture import Control, Status, summarize


class ScoringTests(unittest.TestCase):
    def test_incomplete_evidence_reduces_coverage(self):
        result = summarize([
            Control("a", Status.PASS), Control("b", Status.FAIL),
            Control("c", Status.PARTIAL), Control("d", Status.UNAVAILABLE),
            Control("e", Status.NOT_RUN),
        ])
        self.assertEqual(result["posture"], 50)
        self.assertEqual(result["coverage"], 40)

    def test_inventory_cannot_inflate_score(self):
        result = summarize([Control("a", Status.FAIL), Control("i", Status.PASS, False)])
        self.assertEqual(result["posture"], 0)
        self.assertEqual(result["coverage"], 100)

    def test_no_evaluated_evidence(self):
        result = summarize([Control("a", Status.UNAVAILABLE)])
        self.assertIsNone(result["posture"])
        self.assertEqual(result["coverage"], 0)

    def test_no_safeguards(self):
        for controls in ([], [Control("i", Status.PASS, False)]):
            with self.subTest(controls=controls):
                result = summarize(controls)
                self.assertIsNone(result["posture"])
                self.assertIsNone(result["coverage"])

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            summarize([Control("a", Status.PASS), Control("a", Status.FAIL)])

    def test_malformed_rejected(self):
        for control in (Control("", Status.PASS), Control("a", "PASS"), Control("a", Status.PASS, "false")):
            with self.subTest(control=control), self.assertRaises(ValueError):
                summarize([control])


if __name__ == "__main__":
    unittest.main()
