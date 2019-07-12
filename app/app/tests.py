from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):

    def test_add_whenCalled_returnSummationTwoNumbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(4, 8), 12)
