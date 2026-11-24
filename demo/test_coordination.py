import unittest
from coordination import ready

class CoordinationTests(unittest.TestCase):
    def test_dependency_order(self):
        tasks = {"plan": [], "review": ["plan"]}
        self.assertEqual(ready(tasks, set()), ["plan"])
        self.assertEqual(ready(tasks, {"plan"}), ["review"])
        self.assertEqual(ready(tasks, {"plan", "review"}), [])
    def test_cycle_blocks(self):
        self.assertEqual(ready({"a": ["b"], "b": ["a"]}, set()), [])
    def test_unknown_dependency_blocks(self):
        self.assertEqual(ready({"a": ["missing"]}, set()), [])

if __name__ == "__main__":
    unittest.main()
