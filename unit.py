import unittest
class test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(0, 0)
	def test_2(self):
		self.assertEqual(0, 1)
	def test_3(self):
		self.assertEqual(1, 0)
	def test_4(self):
		self.assertEqual(1, 1)
unittest.main()
