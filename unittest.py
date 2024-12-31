import unittest

def calculate(score, attendance):
  if score >= 90 and attendance >= 75:
    return "A"
  elif score >= 80 and attendance >= 75:
    return "B"
  elif score >= 70 and attendance >= 75:
    return "C"
  else:
    return "F"

class GradeCalculatorTest(unittest.TestCase):  # Corrected inheritance
  def test_logic_coverage(self):
    self.assertEqual(calculate(95, 90), "A")
    self.assertEqual(calculate(85, 90), "B")
    self.assertEqual(calculate(75, 90), "C")
    self.assertEqual(calculate(65, 90), "F")
    self.assertEqual(calculate(95, 80), "A")
    self.assertEqual(calculate(85, 80), "B")
    self.assertEqual(calculate(75, 80), "C")
    self.assertEqual(calculate(65, 80), "F")
    self.assertEqual(calculate(95, 70), "A")
    self.assertEqual(calculate(85, 70), "B")
    self.assertEqual(calculate(75, 70), "C")

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
